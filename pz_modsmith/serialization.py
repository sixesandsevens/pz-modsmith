from __future__ import annotations

from dataclasses import asdict

from .models import AnalysisResult, DependencyFinding, DiagnosticFinding, ModInfo, WorkshopItem


def result_to_dict(result: AnalysisResult) -> dict:
    return {
        "workshop_ids": result.workshop_ids,
        "workshop_path": result.workshop_path,
        "missing_ids": result.missing_ids,
        "workshop_line": result.workshop_line,
        "mods_line": result.mods_line,
        "single_count": result.single_count,
        "multi_count": result.multi_count,
        "missing_count": result.missing_count,
        "active_mod_ids": result.active_mod_ids,
        "items": [asdict(item) for item in result.items],
        "diagnostics": [asdict(f) for f in result.diagnostics],
    }


def dict_to_result(data: dict) -> AnalysisResult:
    items: list[WorkshopItem] = []
    for raw_item in data["items"]:
        mods: list[ModInfo] = []
        for raw_mod in raw_item.get("mods", []):
            dependency_findings = [
                DependencyFinding(
                    required_mod_id=d.get("required_mod_id", ""),
                    status=d.get("status", ""),
                    provider_workshop_ids=d.get("provider_workshop_ids", []),
                    provider_mod_ids=d.get("provider_mod_ids", []),
                    message=d.get("message", ""),
                )
                for d in (raw_mod.get("dependency_findings") or [])
            ]
            mod_data = dict(raw_mod)
            mod_data["dependency_findings"] = dependency_findings
            mods.append(ModInfo(**mod_data))
        items.append(
            WorkshopItem(
                workshop_id=raw_item["workshop_id"],
                mods=mods,
                selected_mod_id=raw_item.get("selected_mod_id"),
                status=raw_item["status"],
                needs_review=raw_item.get("needs_review", False),
            )
        )
    diagnostics = [
        DiagnosticFinding(
            severity=d.get("severity", "info"),
            category=d.get("category", ""),
            raw_value=d.get("raw_value", ""),
            message=d.get("message", ""),
            evidence_line=d.get("evidence_line", ""),
            likely_mod_ids=d.get("likely_mod_ids", []),
            likely_workshop_ids=d.get("likely_workshop_ids", []),
            recommendation=d.get("recommendation", ""),
            scan_result=d.get("scan_result", ""),
        )
        for d in data.get("diagnostics", [])
    ]
    return AnalysisResult(
        workshop_ids=data["workshop_ids"],
        items=items,
        missing_ids=data.get("missing_ids", []),
        workshop_path=data.get("workshop_path", ""),
        active_mod_ids=data.get("active_mod_ids", []),
        diagnostics=diagnostics,
    )
