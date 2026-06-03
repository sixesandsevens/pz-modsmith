from __future__ import annotations

from pathlib import Path

from .models import AnalysisResult, DependencyFinding, DiagnosticFinding, ModInfo, WorkshopItem
from .utils import dedupe_keep_order
from .scanner import scan_workshop_item, choose_best_guess, parse_mod_info_file, collapse_to_highest_version
from .diagnostics import extract_diagnostic_findings, enrich_findings


def _normalize_mod_id(value: str) -> str:
    return " ".join(value.split()).casefold()


def _with_dependency_findings(
    mod: ModInfo,
    dependency_findings: list[DependencyFinding],
) -> ModInfo:
    return ModInfo(
        workshop_id=mod.workshop_id,
        mod_id=mod.mod_id,
        name=mod.name,
        path=mod.path,
        score=mod.score,
        notes=mod.notes,
        confirmed_from_log=mod.confirmed_from_log,
        description=mod.description,
        poster=mod.poster,
        url=mod.url,
        requires_raw=mod.requires_raw,
        flags=mod.flags,
        dependency_findings=dependency_findings,
    )


def analyze_dependencies(items: list[WorkshopItem]) -> None:
    mod_id_to_workshop_ids: dict[str, list[str]] = {}
    mod_id_to_mod_ids: dict[str, list[str]] = {}
    selected_mod_ids: set[str] = set()

    for item in items:
        for selected in item.selected_mod_ids:
            key = _normalize_mod_id(selected)
            if key:
                selected_mod_ids.add(key)
        for mod in item.mods:
            key = _normalize_mod_id(mod.mod_id)
            if not key:
                continue
            mod_id_to_workshop_ids.setdefault(key, [])
            mod_id_to_mod_ids.setdefault(key, [])
            if mod.workshop_id not in mod_id_to_workshop_ids[key]:
                mod_id_to_workshop_ids[key].append(mod.workshop_id)
            if mod.mod_id not in mod_id_to_mod_ids[key]:
                mod_id_to_mod_ids[key].append(mod.mod_id)

    for item in items:
        updated_mods: list[ModInfo] = []
        for mod in item.mods:
            findings: list[DependencyFinding] = []
            for raw_required in mod.requires_raw:
                required_mod_id = " ".join(raw_required.split())
                required_key = _normalize_mod_id(required_mod_id)
                if not required_key:
                    continue

                provider_workshop_ids = mod_id_to_workshop_ids.get(required_key, [])
                provider_mod_ids = mod_id_to_mod_ids.get(required_key, [])

                if required_key in selected_mod_ids:
                    status = "selected"
                    message = "Dependency is selected."
                elif provider_workshop_ids:
                    status = "present_unselected"
                    message = "Dependency exists locally but is not selected."
                else:
                    status = "missing"
                    message = "Dependency was not found in scanned Workshop downloads."

                findings.append(
                    DependencyFinding(
                        required_mod_id=required_mod_id,
                        status=status,
                        provider_workshop_ids=provider_workshop_ids,
                        provider_mod_ids=provider_mod_ids,
                        message=message,
                    )
                )

            updated_mods.append(_with_dependency_findings(mod, findings))
        item.mods = updated_mods


def analyze(
    workshop_ids: list[str],
    workshop_path: Path,
    active_mod_ids: list[str] | None = None,
    console_text: str = "",
    prefer_highest_version: bool = False,
) -> AnalysisResult:
    active_mod_ids = active_mod_ids or []
    inferred_from_active_mod_ids = False
    unmatched_active_mod_ids: list[str] = []
    if active_mod_ids:
        inferred_ids, unmatched_active_mod_ids = infer_workshop_ids_from_active_mod_ids_detailed(workshop_path, active_mod_ids)
        if inferred_ids:
            inferred_from_active_mod_ids = True
            workshop_ids = dedupe_keep_order([*workshop_ids, *inferred_ids])
        elif not workshop_ids:
            # Keep legacy behavior: if no workshop ids were provided and inference
            # found nothing, still mark inference as attempted.
            inferred_from_active_mod_ids = True

    items: list[WorkshopItem] = []
    missing_ids: list[str] = []
    active_mod_id_set = set(active_mod_ids)

    for workshop_id in workshop_ids:
        mods = scan_workshop_item(workshop_path, workshop_id)
        if prefer_highest_version:
            mods = collapse_to_highest_version(mods)
        if active_mod_id_set:
            boosted_mods: list[ModInfo] = []
            for mod in mods:
                confirmed = mod.mod_id in active_mod_id_set
                boosted_mods.append(
                    ModInfo(
                        workshop_id=mod.workshop_id,
                        mod_id=mod.mod_id,
                        name=mod.name,
                        path=mod.path,
                        score=mod.score + (100 if confirmed else 0),
                        notes=(["+confirmed-from-log"] if confirmed else []) + mod.notes,
                        confirmed_from_log=confirmed,
                        description=mod.description,
                        poster=mod.poster,
                        url=mod.url,
                        requires_raw=mod.requires_raw,
                        flags=mod.flags,
                        dependency_findings=mod.dependency_findings,
                    )
                )
            mods = boosted_mods
            if prefer_highest_version:
                mods = collapse_to_highest_version(mods)
        unique_mod_ids = dedupe_keep_order(mod.mod_id for mod in mods)
        confirmed_unique_ids = dedupe_keep_order(mod.mod_id for mod in mods if mod.confirmed_from_log)

        if not mods:
            missing_ids.append(workshop_id)
            items.append(
                WorkshopItem(
                    workshop_id=workshop_id,
                    mods=[],
                    selected_mod_ids=[],
                    status="missing",
                    needs_review=True,
                )
            )
            continue

        if len(unique_mod_ids) == 1:
            items.append(
                WorkshopItem(
                    workshop_id=workshop_id,
                    mods=mods,
                    selected_mod_ids=[unique_mod_ids[0]],
                    status="single",
                    needs_review=False,
                )
            )
            continue

        if confirmed_unique_ids:
            items.append(
                WorkshopItem(
                    workshop_id=workshop_id,
                    mods=mods,
                    selected_mod_ids=list(confirmed_unique_ids),
                    status="multi",
                    needs_review=False,
                )
            )
            continue

        best = choose_best_guess(mods)
        items.append(
            WorkshopItem(
                workshop_id=workshop_id,
                mods=mods,
                selected_mod_ids=[best.mod_id] if best else [],
                status="multi",
                needs_review=True,
            )
        )

    analyze_dependencies(items)

    diagnostics: list[DiagnosticFinding] = []
    if console_text:
        diagnostics = extract_diagnostic_findings(console_text)
        enrich_findings(diagnostics, workshop_path, items)

    return AnalysisResult(
        workshop_ids=workshop_ids,
        items=items,
        missing_ids=missing_ids,
        workshop_path=str(workshop_path),
        active_mod_ids=active_mod_ids,
        diagnostics=diagnostics,
        inferred_from_active_mod_ids=inferred_from_active_mod_ids,
        unmatched_active_mod_ids=unmatched_active_mod_ids,
    )


def infer_workshop_ids_from_active_mod_ids(workshop_path: Path, active_mod_ids: list[str]) -> list[str]:
    found, _unmatched = infer_workshop_ids_from_active_mod_ids_detailed(workshop_path, active_mod_ids)
    return found


def infer_workshop_ids_from_active_mod_ids_detailed(
    workshop_path: Path, active_mod_ids: list[str]
) -> tuple[list[str], list[str]]:
    """Infer Workshop item IDs by scanning local downloads for active Mod IDs.

    This is a fallback for console logs that include many active mod IDs but do
    not include Workshop ID lines. It only uses local workshop content; no
    network calls.
    """
    target_keys = {_normalize_mod_id(mid) for mid in active_mod_ids if _normalize_mod_id(mid)}
    if not target_keys:
        return ([], [])

    found_workshop_ids: list[str] = []
    found_keys: set[str] = set()

    try:
        children = list(workshop_path.iterdir())
    except OSError:
        return ([], list(active_mod_ids))

    for item_dir in children:
        if not item_dir.is_dir():
            continue
        workshop_id = item_dir.name
        if not workshop_id.isdigit():
            continue

        for mod_info_path in item_dir.rglob("mod.info"):
            info = parse_mod_info_file(mod_info_path, workshop_id)
            if not info:
                continue
            candidate_keys = {_normalize_mod_id(info.mod_id)}
            if info.name:
                candidate_keys.add(_normalize_mod_id(info.name))
            hit = next((k for k in candidate_keys if k in target_keys), None)
            if hit:
                if workshop_id not in found_workshop_ids:
                    found_workshop_ids.append(workshop_id)
                found_keys.add(hit)
                if len(found_keys) >= len(target_keys):
                    unmatched = [
                        mid for mid in active_mod_ids if _normalize_mod_id(mid) and _normalize_mod_id(mid) not in found_keys
                    ]
                    return (found_workshop_ids, unmatched)

    unmatched = [
        mid for mid in active_mod_ids if _normalize_mod_id(mid) and _normalize_mod_id(mid) not in found_keys
    ]
    return (found_workshop_ids, unmatched)


def apply_selection(result: AnalysisResult, selected: dict[str, list[str]]) -> AnalysisResult:
    for item in result.items:
        if item.workshop_id in selected:
            values = [v.strip() for v in (selected[item.workshop_id] or []) if v and v.strip()]
            item.selected_mod_ids = values
    analyze_dependencies(result.items)
    return result
