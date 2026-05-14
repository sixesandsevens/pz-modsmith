from __future__ import annotations

from dataclasses import dataclass, field

from .utils import dedupe_keep_order


@dataclass(frozen=True)
class DependencyFinding:
    required_mod_id: str
    status: str
    provider_workshop_ids: list[str] = field(default_factory=list)
    provider_mod_ids: list[str] = field(default_factory=list)
    message: str = ""


@dataclass(frozen=True)
class ModInfo:
    workshop_id: str
    mod_id: str
    name: str
    path: str
    score: int
    notes: list[str]
    confirmed_from_log: bool = False
    description: str = ""
    poster: str = ""
    url: str = ""
    requires_raw: list[str] = field(default_factory=list)
    flags: list[str] = field(default_factory=list)
    dependency_findings: list[DependencyFinding] = field(default_factory=list)


@dataclass
class WorkshopItem:
    workshop_id: str
    mods: list[ModInfo]
    status: str
    needs_review: bool
    selected_mod_ids: list[str] = field(default_factory=list)


@dataclass
class DiagnosticFinding:
    severity: str  # "error" | "warning" | "info"
    category: str  # "world_dict_fatal" | "world_dictionary" | "missing_client_script" | "lua_runtime" | "lua_file_error"
    raw_value: str  # the key/name/path extracted from the log line
    message: str
    evidence_line: str  # raw log line (truncated)
    likely_mod_ids: list[str]
    likely_workshop_ids: list[str]
    recommendation: str = ""
    scan_result: str = ""  # populated by enrich_findings() after local file scan


@dataclass
class AnalysisResult:
    workshop_ids: list[str]
    items: list[WorkshopItem]
    missing_ids: list[str]
    workshop_path: str
    active_mod_ids: list[str]
    diagnostics: list[DiagnosticFinding] = field(default_factory=list)

    @property
    def selected_mod_ids(self) -> list[str]:
        selected: list[str] = []
        for item in self.items:
            for mod_id in item.selected_mod_ids:
                if mod_id:
                    selected.append(mod_id)
        return dedupe_keep_order(m for m in selected if m)

    @property
    def workshop_line(self) -> str:
        return "WorkshopItems=" + ";".join(self.workshop_ids)

    @property
    def mods_line(self) -> str:
        return "Mods=" + ";".join(self.selected_mod_ids)

    @property
    def single_count(self) -> int:
        return sum(1 for item in self.items if item.status == "single")

    @property
    def multi_count(self) -> int:
        return sum(1 for item in self.items if item.status == "multi")

    @property
    def missing_count(self) -> int:
        return len(self.missing_ids)
