from __future__ import annotations

from pathlib import Path

from .models import AnalysisResult, DiagnosticFinding, ModInfo, WorkshopItem
from .utils import dedupe_keep_order
from .scanner import scan_workshop_item, choose_best_guess
from .diagnostics import extract_diagnostic_findings, enrich_findings


def analyze(
    workshop_ids: list[str],
    workshop_path: Path,
    active_mod_ids: list[str] | None = None,
    console_text: str = "",
) -> AnalysisResult:
    items: list[WorkshopItem] = []
    missing_ids: list[str] = []
    active_mod_ids = active_mod_ids or []
    active_mod_id_set = set(active_mod_ids)

    for workshop_id in workshop_ids:
        mods = scan_workshop_item(workshop_path, workshop_id)
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
                    )
                )
            mods = boosted_mods
        unique_mod_ids = dedupe_keep_order(mod.mod_id for mod in mods)
        confirmed_unique_ids = dedupe_keep_order(mod.mod_id for mod in mods if mod.confirmed_from_log)

        if not mods:
            missing_ids.append(workshop_id)
            items.append(
                WorkshopItem(
                    workshop_id=workshop_id,
                    mods=[],
                    selected_mod_id=None,
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
                    selected_mod_id=unique_mod_ids[0],
                    status="single",
                    needs_review=False,
                )
            )
            continue

        if len(confirmed_unique_ids) == 1:
            items.append(
                WorkshopItem(
                    workshop_id=workshop_id,
                    mods=mods,
                    selected_mod_id=confirmed_unique_ids[0],
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
                selected_mod_id=best.mod_id if best else None,
                status="multi",
                needs_review=True,
            )
        )

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
    )


def apply_selection(result: AnalysisResult, selected: dict[str, str]) -> AnalysisResult:
    for item in result.items:
        if item.workshop_id in selected:
            value = selected[item.workshop_id].strip()
            item.selected_mod_id = value or None
    return result
