from __future__ import annotations

import json
import os
import secrets
import socket
import tempfile
import threading
import time
import webbrowser
from importlib import resources as importlib_resources

from .constants import APP_NAME, DEFAULT_PORT
from .utils import dedupe_keep_order, expand_path, detect_default_workshop_path
from .models import AnalysisResult
from .log_parser import (
    extract_workshop_ids_from_console_text,
    extract_active_mod_ids_from_console_text,
    extract_workshop_ids_from_free_text,
)
from .analysis import analyze, apply_selection
from .serialization import result_to_dict, dict_to_result
from .reports import zip_reports
from .steam_api import (
    QUERY_TYPE_RANKED_BY_LAST_UPDATED_DATE,
    QUERY_TYPE_RANKED_BY_PUBLICATION_DATE,
    QUERY_TYPE_RANKED_BY_TEXT_SEARCH,
    QUERY_TYPE_RANKED_BY_TOTAL_UNIQUE_SUBSCRIPTIONS,
    QUERY_TYPE_RANKED_BY_TREND,
    SteamApiKeyMissing,
    expand_workshop_ids_with_collections_and_required_items,
    get_workshop_item_summaries,
    query_workshop,
)
from .server_ini import parse_pzserver_ini, apply_pzserver_ini_edits, get_first_ini_value
from .sandbox_lua import parse_sandbox_vars_lua, apply_sandbox_vars_edits


INDEX_HTML = r"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PZ Modsmith</title>
  <style>
    :root {
      --bg: #10141c;
      --panel: #171d29;
      --panel2: #202839;
      --text: #e8edf7;
      --muted: #aeb8ca;
      --accent: #7aa2ff;
      --danger: #ff7878;
      --warn: #ffc66d;
      --good: #78d98b;
      --border: #324057;
      --shadow: rgba(0,0,0,.35);
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: radial-gradient(circle at top, #1a2332 0, var(--bg) 45%);
      color: var(--text);
    }
    header {
      padding: 32px 24px 12px;
      max-width: 1180px;
      margin: 0 auto;
    }
    h1 { margin: 0; font-size: clamp(2rem, 5vw, 4rem); letter-spacing: -.04em; }
    .subtitle { color: var(--muted); margin-top: 8px; max-width: 780px; line-height: 1.5; }
    main { max-width: 1180px; margin: 0 auto; padding: 16px 24px 64px; }
    .card {
      background: linear-gradient(180deg, rgba(255,255,255,.03), rgba(255,255,255,.015));
      border: 1px solid var(--border);
      border-radius: 18px;
      box-shadow: 0 20px 50px var(--shadow);
      padding: 20px;
      margin: 18px 0;
    }
    label { display: block; font-weight: 700; margin: 12px 0 6px; }
    input[type="text"], textarea, input[type="file"] {
      width: 100%;
      background: #0d121a;
      color: var(--text);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 12px 14px;
      font: inherit;
    }
    textarea { min-height: 150px; resize: vertical; }
    button, .button {
      border: 0;
      background: var(--accent);
      color: #07101f;
      font-weight: 800;
      border-radius: 12px;
      padding: 12px 16px;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      gap: 8px;
      align-items: center;
      margin-top: 14px;
    }
    button.secondary, .button.secondary { background: var(--panel2); color: var(--text); border: 1px solid var(--border); }
    .grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; }
    .stat { background: var(--panel); border: 1px solid var(--border); border-radius: 16px; padding: 14px; }
    .stat strong { display: block; font-size: 1.8rem; }
    .muted { color: var(--muted); }
    .pill { display: inline-flex; border-radius: 999px; padding: 3px 9px; font-size: .8rem; font-weight: 800; margin-right: 6px; border: 1px solid var(--border); }
    .pill.good { color: var(--good); }
    .pill.warn { color: var(--warn); }
    .pill.danger { color: var(--danger); }
    .item { border: 1px solid var(--border); border-radius: 16px; margin: 12px 0; overflow: hidden; background: rgba(0,0,0,.15); }
    .item-head { padding: 14px 16px; background: var(--panel2); display: flex; justify-content: space-between; gap: 12px; align-items: center; }
    .item-left { display: flex; gap: 12px; align-items: center; min-width: 0; }
    .thumb { width: 64px; height: 64px; border-radius: 12px; border: 1px solid var(--border); background: #0d121a; object-fit: cover; flex: 0 0 auto; }
    .item-title { font-weight: 900; overflow-wrap: anywhere; }
    .subline { color: var(--muted); font-size: .85rem; margin-top: 2px; overflow-wrap: anywhere; }
    .item-body { padding: 12px 16px; }
    .mod-option { padding: 10px; border-radius: 12px; border: 1px solid var(--border); margin: 8px 0; background: #111722; }
    .mod-option.selected { outline: 2px solid var(--accent); }
    .mod-title { font-weight: 800; }
    .path { color: var(--muted); font-size: .83rem; overflow-wrap: anywhere; margin-top: 4px; }
    code, pre { background: #0b1018; color: #d8e2f4; border: 1px solid var(--border); border-radius: 12px; }
    pre { padding: 12px; white-space: pre-wrap; overflow-wrap: anywhere; }
    .toolbar { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; }
    .filters { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 10px; }
    .hidden { display: none; }
    .copy-row { display: grid; grid-template-columns: 1fr auto; gap: 8px; align-items: start; }
    .tiny { font-size: .85rem; }
    @media (max-width: 820px) { .grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } .copy-row { grid-template-columns: 1fr; } }
    .finding { border: 1px solid var(--border); border-radius: 12px; padding: 12px 14px; margin: 10px 0; background: rgba(0,0,0,.2); }
    .finding.sev-error { border-color: var(--danger); }
    .finding.sev-warning { border-color: var(--warn); }
    .finding-head { display: flex; gap: 8px; align-items: baseline; flex-wrap: wrap; margin-bottom: 6px; }
    .finding-body { font-size: .88rem; line-height: 1.6; }
    .finding-body .evidence { font-family: monospace; background: #0b1018; border-radius: 6px; padding: 4px 8px; font-size: .82rem; overflow-wrap: anywhere; color: var(--muted); margin: 4px 0; }
    .finding-body .recommendation { color: var(--text); margin-top: 6px; }
    .finding-body .scan-result { color: var(--good); }
    .dependency-line { margin-top: 6px; }
  </style>
</head>
<body>
<header>
  <h1>PZ Modsmith</h1>
  <p class="subtitle">A local Project Zomboid server mod-list helper. Feed it a console log or Workshop IDs, review the messy multi-ID mods, then copy clean <code>WorkshopItems=</code> and <code>Mods=</code> lines.</p>
  <div class="toolbar">
    <a class="button secondary tiny" href="/">Mods</a>
    <a class="button secondary tiny" href="/workshop">Workshop</a>
    <a class="button secondary tiny" href="/server">Server Settings</a>
    <a class="button secondary tiny" href="/sandbox">SandboxVars</a>
  </div>
</header>
<main>
  {% if error %}
    <section class="card"><span class="pill danger">Error</span> {{ error }}</section>
  {% endif %}

  <section class="card">
    <div class="toolbar">
      <a class="button secondary" href="/server/template">Load `pzserver.ini` template</a>
      <a class="button secondary" href="/sandbox/template">Load `pzserver_SandboxVars.lua` template</a>
    </div>
    <form method="post" action="/analyze" enctype="multipart/form-data">
      <label>Workshop content path</label>
      <input type="text" name="workshop_path" value="{{ workshop_path }}">
      <p class="muted tiny">Usually something like <code>/mnt/storage/SteamLibrary/steamapps/workshop/content/108600</code>.</p>

      <label>Optional: load your current <code>pzserver.ini</code></label>
      <input type="file" name="server_ini_file" accept=".ini,.txt">
      <p class="muted tiny">If provided, Modsmith will use <code>WorkshopItems=</code> (preferred) or extract Workshop IDs from the INI. It will also offer an updated INI download on the results page.</p>

      <label>Upload console.txt</label>
      <input type="file" name="console_file" accept=".txt,.log">

      <label>Or paste console log / Workshop IDs / Steam URLs</label>
      <textarea name="pasted_text" placeholder="Paste ~/Zomboid/console.txt snippets, Workshop IDs, or Steam Workshop URLs here..."></textarea>

      <label class="tiny" style="font-weight:700; margin-top: 10px;">
        <input type="checkbox" name="fetch_steam_deps" value="1">
        Fetch Steam "required items" (online) and include them
      </label>
      <p class="muted tiny">Optional. Uses Steam Web API to fetch Workshop dependencies; still requires the items to be downloaded locally to scan <code>mod.info</code>.</p>

      <label class="tiny" style="font-weight:700; margin-top: 10px;">
        Steam Web API key (optional; stored in this browser)
      </label>
      <input type="password" id="steam_api_key_ui" placeholder="Paste your Steam Web API key (not required unless you want required-item expansion to be reliable)">
      <input type="hidden" name="steam_api_key" id="steam_api_key_form">
      <div class="muted tiny" style="margin-top: 6px;">
        Saved to <code>localStorage</code> on this device. Sent only with this form submit. Leave blank to run without a key.
      </div>

      <label class="tiny" style="font-weight:700; margin-top: 10px;">
        <input type="checkbox" name="prefer_highest_version" value="1" checked>
        Prefer highest version when the same Mod ID appears multiple times
      </label>
      <p class="muted tiny">Collapses multiple <code>mod.info</code> variants like <code>42.0</code>/<code>42.15</code> to the newest one.</p>

      <button type="submit">Analyze mods</button>
    </form>
  </section>

	  {% if result %}
	    {% if result.inferred_from_active_mod_ids and result.unmatched_active_mod_ids %}
	    <section class="card">
	      <span class="pill warn">Heads up</span>
	      <strong>Only {{ result.workshop_ids|length }} Workshop IDs could be inferred from {{ result.active_mod_ids|length }} active Mod IDs.</strong>
	      <div class="muted tiny" style="margin-top:6px;">
	        This usually means your <code>Workshop content path</code> doesn’t point at the same Steam library where the mods are downloaded, or the mods aren’t downloaded yet.
	      </div>
	      <details style="margin-top:10px;">
	        <summary class="muted tiny">Show unmatched active Mod IDs ({{ result.unmatched_active_mod_ids|length }})</summary>
	        <pre class="tiny">{{ result.unmatched_active_mod_ids | join('\n') }}</pre>
	      </details>
	    </section>
	    {% endif %}
	    <section class="card">
	      <div class="grid">
	        <div class="stat"><strong>{{ result.workshop_ids|length }}</strong><span class="muted">Workshop IDs</span></div>
	        <div class="stat"><strong>{{ result.single_count }}</strong><span class="muted">Single-ID items</span></div>
        <div class="stat"><strong>{{ result.multi_count }}</strong><span class="muted">Need review</span></div>
        <div class="stat"><strong>{{ result.missing_count }}</strong><span class="muted">Missing</span></div>
        <div class="stat"><strong>{{ result.active_mod_ids|length }}</strong><span class="muted">Active Mod IDs from log</span></div>
        <div class="stat"><strong {% if result.diagnostics|length > 0 %}style="color:var(--danger)"{% endif %}>{{ result.diagnostics|length }}</strong><span class="muted">Failure findings</span></div>
      </div>
    </section>

    {% if result.diagnostics %}
    <section class="card">
      <h2>Connection Failure Diagnosis</h2>
      <p class="muted tiny">Patterns extracted from the console log. Wording is deliberately hedged — these are likely causes, not certainties.</p>
      {% for f in result.diagnostics %}
        <div class="finding sev-{{ f.severity }}">
          <div class="finding-head">
            <span class="pill {% if f.severity == 'error' %}danger{% elif f.severity == 'warning' %}warn{% endif %}">{{ f.severity }}</span>
            <span class="pill">{{ f.category }}</span>
            <strong>{{ f.message }}</strong>
          </div>
          <div class="finding-body">
            {% if f.evidence_line %}<div class="evidence">{{ f.evidence_line }}</div>{% endif %}
            {% if f.scan_result %}<div class="scan-result">&#128269; Scan: {{ f.scan_result }}</div>{% endif %}
            {% if f.likely_mod_ids %}<div class="muted">Possibly related: {{ f.likely_mod_ids | join(', ') }}</div>{% endif %}
            {% if f.recommendation %}<div class="recommendation">&#8594; {{ f.recommendation }}</div>{% endif %}
          </div>
        </div>
      {% endfor %}
    </section>
    {% endif %}

	    <form method="post" action="/generate">
	      <input type="hidden" name="state_token" value="{{ state_token | e }}">
	      <input type="hidden" name="server_ini_token" value="{{ server_ini_token | e }}">
	      <section class="card">
        <h2>Review multi-ID Workshop items</h2>
        <p class="muted">Selections marked +confirmed-from-log came from active runtime mod-load lines, so they are much stronger than guesses. Anything marked B41, SP, legacy, disable, no MP, patch, or optional still deserves side-eye.</p>
        <div class="filters">
          <button class="secondary" type="button" onclick="filterItems('all')">Show all</button>
          <button class="secondary" type="button" onclick="filterItems('multi')">Needs review</button>
          <button class="secondary" type="button" onclick="filterItems('single')">Single-ID</button>
          <button class="secondary" type="button" onclick="filterItems('missing')">Missing</button>
        </div>

	        {% for item in result.items %}
	          <div class="item" data-status="{{ item.status }}">
		            <div class="item-head">
		              <div class="item-left">
	                {% set meta = workshop_meta.get(item.workshop_id) if workshop_meta else None %}
	                {% if meta and meta.preview_url %}
	                  <img class="thumb" alt="" src="{{ meta.preview_url }}">
	                {% endif %}
	                <div>
	                  <div class="item-title">
	                    <strong>Workshop {{ item.workshop_id }}</strong>
	                    {% if meta and meta.title %} — {{ meta.title }}{% endif %}
	                  </div>
		                  {% if meta and (meta.subscriptions or meta.visibility is not none) %}
		                    <div class="subline">
		                      {% if meta.subscriptions %}{{ meta.subscriptions }} subs{% endif %}
		                      {% if meta.visibility is not none %}{% if meta.subscriptions %} • {% endif %}visibility {{ meta.visibility }}{% endif %}
		                    </div>
		                  {% endif %}
		                  <div class="subline">
		                    <label class="tiny" style="display:inline-flex; gap:8px; align-items:center;">
		                      <input type="checkbox" name="include_workshop_id" value="{{ item.workshop_id }}" checked>
		                      Include in <code>WorkshopItems=</code>
		                    </label>
		                  </div>
		                {% if item.status == 'single' %}<span class="pill good">single</span>{% endif %}
	                {% if item.status == 'multi' %}<span class="pill warn">review</span>{% endif %}
	                {% if item.status == 'missing' %}<span class="pill danger">missing</span>{% endif %}
	                {% for mod in item.mods if mod.mod_id in item.selected_mod_ids %}
	                  {% if 'likely-library' in mod.flags or 'tiles' in mod.flags or 'vehicle-framework' in mod.flags %}
                    <span class="pill warn">&#9888; likely dependency — be careful removing</span>
                  {% endif %}
                  {% if 'has-requires' in mod.flags %}
                    <span class="pill warn">declares requires</span>
                  {% endif %}
                  {% for dep in mod.dependency_findings %}
                    {% if dep.status == 'missing' %}
                      <span class="pill danger">missing dependency: {{ dep.required_mod_id }}</span>
                    {% elif dep.status == 'present_unselected' %}
                      <span class="pill warn">unselected dependency: {{ dep.required_mod_id }}</span>
                    {% endif %}
	                  {% endfor %}
	                {% endfor %}
	                </div>
	              </div>
	              <a class="button secondary tiny" target="_blank" href="https://steamcommunity.com/sharedfiles/filedetails/?id={{ item.workshop_id }}">Steam page</a>
	            </div>
	            <div class="item-body">
	              {% if not item.mods %}
	                <p class="muted">No downloaded mod.info found for this Workshop item.</p>
	                <div class="muted tiny">Quick manual workflow:</div>
	                <div class="toolbar">
	                  <button class="secondary tiny" type="button" onclick="copyValue('{{ item.workshop_id }}')">Copy Workshop ID</button>
	                  <a class="button secondary tiny" target="_blank" href="https://steamcommunity.com/sharedfiles/filedetails/?id={{ item.workshop_id }}">Open Steam page</a>
	                </div>
	                <label class="tiny" style="font-weight:700; margin-top: 10px;">
	                  Optional: paste Mod ID(s) for <code>Mods=</code> (semicolon/comma separated)
	                </label>
	                <input type="text" name="manual_modids_{{ item.workshop_id }}" placeholder="e.g. MyModID;MyOtherModID">
	                <div class="muted tiny" style="margin-top: 6px;">
	                  If the author doesn’t list Mod IDs on Steam, you’ll need to download the mod so Modsmith can read <code>mod.info</code>.
	                </div>
	              {% else %}
                {% for mod in item.mods %}
                  <label class="mod-option {% if mod.mod_id in item.selected_mod_ids %}selected{% endif %}">
                    <input type="checkbox" name="selected_{{ item.workshop_id }}" value="{{ mod.mod_id }}" {% if mod.mod_id in item.selected_mod_ids %}checked{% endif %}>
                    <span class="mod-title">{{ mod.mod_id }}</span> — {{ mod.name }}
                    <span class="pill {% if mod.score >= 2 %}good{% elif mod.score < 0 %}danger{% else %}warn{% endif %}">score {{ mod.score }}</span>
                    {% if mod.confirmed_from_log %}<span class="pill good">confirmed from log</span>{% endif %}
                    {% for note in mod.notes %}
                      <span class="pill {% if note.startswith('+') %}good{% else %}danger{% endif %}">{{ note }}</span>
                    {% endfor %}
                    {% if 'likely-library' in mod.flags %}<span class="pill warn">library/framework</span>{% endif %}
                    {% if 'tiles' in mod.flags %}<span class="pill warn">tile pack</span>{% endif %}
                    {% if 'vehicle-framework' in mod.flags %}<span class="pill warn">vehicle framework</span>{% endif %}
                    {% if 'patch-or-addon' in mod.flags %}<span class="pill">patch/addon</span>{% endif %}
                    {% if 'has-requires' in mod.flags %}<span class="pill warn">has requires</span>{% endif %}
                    <div class="path">{{ mod.path }}</div>
                    {% if mod.requires_raw %}
                      <div class="path">Declares requires: {{ mod.requires_raw | join(', ') }}</div>
                    {% endif %}
                    {% for dep in mod.dependency_findings %}
                      <div class="path dependency-line">
                        <span class="pill {% if dep.status == 'selected' %}good{% elif dep.status == 'present_unselected' %}warn{% elif dep.status == 'missing' %}danger{% endif %}">
                          {{ dep.status }}
                        </span>
                        Requires {{ dep.required_mod_id }} — {{ dep.message }}
                        {% if dep.provider_workshop_ids %}
                          Provider Workshop: {{ dep.provider_workshop_ids | join(', ') }}
                        {% endif %}
                      </div>
                    {% endfor %}
                  </label>
                {% endfor %}
              {% endif %}
            </div>
          </div>
        {% endfor %}
      </section>

      <section class="card">
        <button type="submit">Generate final lines</button>
      </section>
    </form>
  {% endif %}
</main>
<script>
function filterItems(status) {
  document.querySelectorAll('.item').forEach(el => {
    if (status === 'all' || el.dataset.status === status) el.classList.remove('hidden');
    else el.classList.add('hidden');
  });
}

async function copyValue(v) {
  try { await navigator.clipboard.writeText(v); } catch (_) {}
}

// Persist Steam API key locally (browser-only) to avoid requiring server-side config.
(function () {
  const storageKey = "pz_modsmith_steam_api_key";
  const el = document.getElementById("steam_api_key_ui");
  const formEl = document.getElementById("steam_api_key_form");
  if (!el) return;
  try {
    const saved = localStorage.getItem(storageKey);
    if (saved && !el.value) el.value = saved;
    if (formEl && saved) formEl.value = saved;
  } catch (_) {}
  el.addEventListener("input", () => {
    try {
      if (el.value) localStorage.setItem(storageKey, el.value);
      else localStorage.removeItem(storageKey);
      if (formEl) formEl.value = el.value || "";
    } catch (_) {}
  });
})();
</script>
</body>
</html>
"""

WORKSHOP_HTML = r"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PZ Modsmith - Workshop</title>
  <style>
    :root { --bg:#10141c; --panel:#171d29; --panel2:#202839; --text:#e8edf7; --muted:#aeb8ca; --accent:#7aa2ff; --border:#324057; }
    * { box-sizing: border-box; }
    body { margin:0; font-family: system-ui, sans-serif; background: radial-gradient(circle at top, #1a2332 0, var(--bg) 45%); color: var(--text); }
    header { padding: 28px 24px 10px; max-width: 1180px; margin: 0 auto; }
    main { max-width: 1180px; margin: 0 auto; padding: 16px 24px 64px; }
    .toolbar { display:flex; gap:10px; flex-wrap:wrap; align-items:center; }
    .card { background: linear-gradient(180deg, rgba(255,255,255,.03), rgba(255,255,255,.015)); border: 1px solid var(--border); border-radius: 18px; padding: 20px; margin: 18px 0; }
    label { display:block; font-weight: 800; margin: 10px 0 6px; }
    input[type="text"], input[type="password"], textarea, select { width: 100%; background: #0d121a; color: var(--text); border: 1px solid var(--border); border-radius: 12px; padding: 12px 14px; font: inherit; }
    textarea { min-height: 160px; resize: vertical; }
    button, .button { border:0; background: var(--accent); color:#07101f; font-weight: 900; border-radius: 12px; padding: 12px 16px; cursor:pointer; text-decoration:none; display:inline-flex; gap: 8px; align-items:center; margin-top: 12px; }
    .secondary { background: var(--panel2); color: var(--text); border: 1px solid var(--border); }
    .muted { color: var(--muted); }
    .tiny { font-size: .85rem; }
    .results { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
    @media (max-width: 900px) { .results { grid-template-columns: 1fr; } }
    .res { border: 1px solid var(--border); border-radius: 16px; padding: 12px; background: rgba(0,0,0,.15); display:flex; gap: 12px; align-items: flex-start; }
    .thumb { width: 84px; height: 84px; border-radius: 14px; border: 1px solid var(--border); background: #0d121a; object-fit: cover; flex: 0 0 auto; }
    .title { font-weight: 900; }
    .sub { color: var(--muted); font-size: .85rem; margin-top: 4px; }
    code { background:#0b1018; border:1px solid var(--border); border-radius: 10px; padding: 2px 6px; }
    .hidden { display: none; }
    .tabs { display:flex; gap: 8px; flex-wrap: wrap; margin-top: 12px; }
    .tab { border: 1px solid var(--border); background: rgba(0,0,0,.12); color: var(--text); font-weight: 900; border-radius: 999px; padding: 8px 12px; cursor: pointer; }
    .tab.active { background: var(--accent); color: #07101f; border-color: rgba(0,0,0,0); }
  </style>
</head>
<body>
<header>
  <h1>Workshop</h1>
  <p class="muted">Search the PZ Steam Workshop and build an updated <code>WorkshopItems=</code> line. <code>Mods=</code> still requires downloaded content to read <code>mod.info</code>.</p>
  <div class="toolbar">
    <a class="button secondary tiny" href="/">Mods</a>
    <a class="button secondary tiny" href="/workshop">Workshop</a>
    <a class="button secondary tiny" href="/server">Server Settings</a>
    <a class="button secondary tiny" href="/sandbox">SandboxVars</a>
  </div>
</header>
<main>
  {% if error %}
    <section class="card"><strong>Error:</strong> {{ error }}</section>
  {% endif %}
 
  <div class="tabs">
    <button id="tabbtn_browse" class="tab active" type="button" onclick="showWorkshopTab('browse')">Browse</button>
    <button id="tabbtn_ini" class="tab" type="button" onclick="showWorkshopTab('ini')">In Your INI ({{ ini_ids|length }})</button>
  </div>

  <div id="tab_ini" class="hidden">
    <section class="card">
      <h2>In Your INI ({{ ini_ids|length }})</h2>
      <p class="muted tiny">This list updates as you add items. Use this tab to remove items quickly.</p>
      {% if not ini_ids %}
        <div class="muted">Nothing yet. Add items from the Browse tab.</div>
      {% else %}
        <form method="post" action="/workshop/remove">
          <input type="hidden" name="workshop_items" value="{{ workshop_items | e }}">
          <input type="hidden" name="mods" value="{{ mods | e }}">
          <input type="hidden" name="q" value="{{ q | e }}">
          <input type="hidden" name="sort" value="{{ sort | e }}">
          <input type="hidden" name="tags" value="{{ tags | e }}">
          <input type="hidden" name="page" value="{{ page or 1 }}">
          <input type="hidden" name="cursor" value="{{ cursor or '*' }}">

          <div class="muted tiny">Select Workshop items to remove from <code>WorkshopItems=</code>:</div>
          <div class="results" style="margin-top: 12px;">
            {% for wid in ini_ids|list|sort %}
              {% set m = ini_meta.get(wid) if ini_meta else None %}
              <label class="res">
                <input type="checkbox" name="remove_wid" value="{{ wid }}">
                {% if m and m.preview_url %}<img class="thumb" alt="" src="{{ m.preview_url }}">{% endif %}
                <div style="min-width:0;">
                  <div class="title">{% if m and m.title %}{{ m.title }}{% else %}Workshop {{ wid }}{% endif %}</div>
                  <div class="sub">id {{ wid }}{% if m and m.subscriptions %} • {{ m.subscriptions }} subs{% endif %}</div>
                  <div class="sub" style="margin-top:6px;">
                    <a class="button secondary tiny" target="_blank" href="https://steamcommunity.com/sharedfiles/filedetails/?id={{ wid }}">Steam page</a>
                  </div>
                </div>
              </label>
            {% endfor %}
          </div>

          <label class="tiny" style="font-weight:800; margin-top: 10px;">Optional: remove Mod ID(s) from <code>Mods=</code></label>
          <input type="text" name="remove_modids" placeholder="e.g. ModA;ModB">
          <button class="secondary" type="submit">Remove selected</button>
        </form>
      {% endif %}
    </section>
  </div>

  <div id="tab_browse">

  <section class="card">
    <form method="post" action="/workshop/search">
      <label>Steam Web API key (stored in this browser)</label>
      <input type="password" id="steam_api_key_ui" placeholder="Required for Workshop search">
      <input type="hidden" name="steam_api_key" id="steam_api_key_form">
      <div class="muted tiny" style="margin-top:6px;">Saved to <code>localStorage</code>. Not stored on the server. Without a key, Workshop browsing/search won’t work.</div>

      <label>Search</label>
      <input type="text" name="q" value="{{ q or '' }}" placeholder="Search the Workshop...">

      <label>Sort</label>
      <select name="sort">
        <option value="relevance" {% if sort == 'relevance' %}selected{% endif %}>Relevance</option>
        <option value="popular" {% if sort == 'popular' %}selected{% endif %}>Popular</option>
        <option value="subscribed" {% if sort == 'subscribed' %}selected{% endif %}>Most subscribed</option>
        <option value="trending" {% if sort == 'trending' %}selected{% endif %}>Trending</option>
        <option value="new" {% if sort == 'new' %}selected{% endif %}>New</option>
        <option value="updated" {% if sort == 'updated' %}selected{% endif %}>Recently updated</option>
      </select>

      <label>Browse by tag</label>
      <div class="muted tiny" style="margin-top:-2px;">Pick tags from Steam's list. Stored as a comma-separated filter.</div>
      <div class="toolbar" style="gap:8px; margin-top: 8px;">
        {% for t in all_tags %}
          <label class="tiny" style="display:inline-flex; gap:8px; align-items:center; padding:6px 10px; border:1px solid var(--border); border-radius:999px; background: rgba(0,0,0,.12);">
            <input type="checkbox" class="tagcb" value="{{ t }}" {% if (selected_tags and (t in selected_tags)) %}checked{% endif %}>
            {{ t }}
          </label>
        {% endfor %}
      </div>
      <input type="hidden" name="tags" id="tags_hidden" value="{{ tags or '' }}">

      <label>WorkshopItems</label>
      <input type="text" name="workshop_items" id="workshop_items_ui" value="{{ workshop_items or '' }}" placeholder="e.g. 123;456;789">

      <label>Mods</label>
      <input type="text" name="mods" id="mods_ui" value="{{ mods or '' }}" placeholder="e.g. ModA;ModB;ModC">
      <div class="muted tiny" style="margin-top:6px;">
        Stored in this browser so you can keep browsing and adding quickly. Download a minimal INI when you’re done.
      </div>

      <input type="hidden" name="page" value="{{ page or 1 }}">
      <input type="hidden" name="cursor" value="{{ cursor or '*' }}">
      <button type="submit">Search Workshop</button>
    </form>
  </section>

  {% if results %}
    <section class="card">
	      <form method="post" action="/workshop/add">
	        <input type="hidden" name="workshop_items" value="{{ workshop_items | e }}">
	        <input type="hidden" name="mods" value="{{ mods | e }}">
	        <input type="hidden" name="q" value="{{ q | e }}">
	        <input type="hidden" name="sort" value="{{ sort | e }}">
	        <input type="hidden" name="tags" value="{{ tags | e }}">
	        <input type="hidden" name="steam_api_key" id="steam_api_key_add">
	        <input type="hidden" name="page" value="{{ page or 1 }}">
	        <input type="hidden" name="cursor" value="{{ cursor or '*' }}">

        <div class="toolbar" style="justify-content: space-between; margin-top: 6px;">
          <div class="muted tiny">
            Showing {{ results|length }} results{% if total %} of ~{{ total }}{% endif %} (page {{ page or 1 }})
          </div>
          <div class="toolbar">
            {% if has_prev %}
              <button class="secondary tiny" type="submit" formaction="/workshop/search" name="page" value="{{ (page or 1) - 1 }}">Prev</button>
            {% endif %}
            {% if has_next %}
              <button class="secondary tiny" type="submit" formaction="/workshop/search" name="page" value="{{ (page or 1) + 1 }}">Next</button>
            {% endif %}
          </div>
        </div>

        <div class="muted tiny">
          Select mods to add to <code>WorkshopItems=</code>. Optionally paste Mod ID(s) if the author lists them on the Steam page.
          If not listed, you’ll need to download the mod and use the Analyze flow to extract Mod IDs from <code>mod.info</code>.
        </div>
        <div class="results" style="margin-top: 12px;">
          {% for r in results %}
            <label class="res">
              <input type="checkbox" name="wid" value="{{ r.publishedfileid }}" {% if ini_ids and (r.publishedfileid in ini_ids) %}checked{% endif %}>
              {% if r.preview_url %}<img class="thumb" alt="" src="{{ r.preview_url }}">{% endif %}
              <div style="min-width:0;">
                <div class="title">{{ r.title }}</div>
                <div class="sub">
                  id {{ r.publishedfileid }}{% if r.subscriptions %} • {{ r.subscriptions }} subs{% endif %}
                  {% if ini_ids and (r.publishedfileid in ini_ids) %} • <strong>already in INI</strong>{% endif %}
                </div>
                <div class="sub" style="margin-top: 6px;">
                  <a class="button secondary tiny" target="_blank" href="https://steamcommunity.com/sharedfiles/filedetails/?id={{ r.publishedfileid }}">Open Steam page</a>
                </div>
                <div class="sub" style="margin-top: 8px;">
                  <input type="text" name="modids_{{ r.publishedfileid }}" placeholder="Optional: Mod ID(s) for Mods= (semicolon or comma separated)">
                </div>
              </div>
            </label>
          {% endfor %}
        </div>
        <button type="submit">Add selected to INI</button>
      </form>
    </section>
  {% endif %}

	  {% if searched and not results %}
	    <section class="card">
	      <div class="muted">No results returned.</div>
	      {% if debug %}
	        <pre class="tiny">{{ debug }}</pre>
	      {% endif %}
	    </section>
	  {% endif %}

  </div>

  {% if updated_ini_text is not none %}
	    <section class="card">
	      <h2>Updated Lines</h2>
	      <p class="muted tiny">Copy these into your <code>pzserver.ini</code> (or download a minimal INI).</p>
	      <div class="muted tiny"><code>WorkshopItems=</code></div>
	      <textarea readonly>{{ updated_workshop_items_line }}</textarea>
	      <div class="muted tiny" style="margin-top:10px;"><code>Mods=</code></div>
	      <textarea readonly>{{ updated_mods_line }}</textarea>
	      <form method="post" action="/download-ini-token">
	        <input type="hidden" name="text_token" value="{{ updated_ini_token | e }}">
	        <button type="submit">Download minimal pzserver.ini</button>
	      </form>
	      {% if analyze_text %}
	      <form method="post" action="/analyze" style="margin-top: 10px;">
	        <input type="hidden" name="workshop_path" value="{{ default_workshop_path }}">
	        <input type="hidden" name="pasted_text" value="{{ analyze_text | e }}">
	        <input type="hidden" name="server_ini_token" value="{{ updated_ini_token | e }}">
	        <button class="secondary" type="submit">Analyze these WorkshopItems</button>
	      </form>
	      {% endif %}
	    </section>
	  {% endif %}
</main>
<script>
(function () {
  const storageKey = "pz_modsmith_steam_api_key";
  const el = document.getElementById("steam_api_key_ui");
  const formEl = document.getElementById("steam_api_key_form");
  if (el) {
    try {
      const saved = localStorage.getItem(storageKey);
      if (saved && !el.value) el.value = saved;
      if (formEl && saved) formEl.value = saved;
    } catch (_) {}
    el.addEventListener("input", () => {
      try {
        if (el.value) localStorage.setItem(storageKey, el.value);
        else localStorage.removeItem(storageKey);
        if (formEl) formEl.value = el.value || "";
      } catch (_) {}
    });
  }
  const addHidden = document.getElementById("steam_api_key_add");
  if (addHidden) {
    try { addHidden.value = localStorage.getItem(storageKey) || ""; } catch (_) { addHidden.value = ""; }
  }

  // Tag checkbox -> hidden comma-separated tags field.
  const tagsHidden = document.getElementById("tags_hidden");
  const tagCbs = Array.from(document.querySelectorAll(".tagcb"));
  function syncTags() {
    if (!tagsHidden) return;
    const tags = tagCbs.filter(cb => cb.checked).map(cb => cb.value);
    tagsHidden.value = tags.join(", ");
  }
  tagCbs.forEach(cb => cb.addEventListener("change", syncTags));
  syncTags();

  // Persist selection lines locally for quick browsing/add workflow.
  const wsKey = "pz_modsmith_workshopitems_line";
  const modsKey = "pz_modsmith_mods_line";
  const wsEl = document.getElementById("workshop_items_ui");
  const modsEl = document.getElementById("mods_ui");
  try {
    if (wsEl && !wsEl.value) wsEl.value = localStorage.getItem(wsKey) || "";
    if (modsEl && !modsEl.value) modsEl.value = localStorage.getItem(modsKey) || "";
  } catch (_) {}
  function persistLines() {
    try {
      if (wsEl) localStorage.setItem(wsKey, wsEl.value || "");
      if (modsEl) localStorage.setItem(modsKey, modsEl.value || "");
    } catch (_) {}
  }
  if (wsEl) wsEl.addEventListener("input", persistLines);
  if (modsEl) modsEl.addEventListener("input", persistLines);

  // Reset cursor/page when starting a new search so we don't reuse a cursor from
  // a different query/sort/tag filter (which produces irrelevant/empty results).
  const searchForm = document.querySelector('form[action="/workshop/search"]');
  if (searchForm) {
    searchForm.addEventListener("submit", () => {
      const cursorEl = searchForm.querySelector('input[name="cursor"]');
      const pageEl = searchForm.querySelector('input[name="page"]');
      if (cursorEl) cursorEl.value = "*";
      if (pageEl) pageEl.value = "1";
    });
  }

  // Auto-load "Most Popular" (or selected sort) when landing on /workshop,
  // but only if the user has an API key stored and there are no results yet.
  const hasResults = {{ 'true' if results else 'false' }};
  const hasError = {{ 'true' if error else 'false' }};
	  if (!hasResults && !hasError && el) {
	    let savedKey = "";
	    try { savedKey = localStorage.getItem(storageKey) || ""; } catch (_) {}
	    if (savedKey) {
      // Submit once (avoid loops if server errors).
      const onceKey = "pz_modsmith_workshop_autoloaded";
      let did = false;
      try { did = sessionStorage.getItem(onceKey) === "1"; } catch (_) {}
      if (!did) {
        try { sessionStorage.setItem(onceKey, "1"); } catch (_) {}
        const form = el.closest("form");
        if (form) form.submit();
      }
	    }
	  }

	  window.showWorkshopTab = function (which) {
	    const tabBrowse = document.getElementById("tab_browse");
	    const tabIni = document.getElementById("tab_ini");
	    const btnBrowse = document.getElementById("tabbtn_browse");
	    const btnIni = document.getElementById("tabbtn_ini");
	    if (!tabBrowse || !tabIni || !btnBrowse || !btnIni) return;
	    if (which === "ini") {
	      tabBrowse.classList.add("hidden");
	      tabIni.classList.remove("hidden");
	      btnBrowse.classList.remove("active");
	      btnIni.classList.add("active");
	    } else {
	      tabIni.classList.add("hidden");
	      tabBrowse.classList.remove("hidden");
	      btnIni.classList.remove("active");
	      btnBrowse.classList.add("active");
	    }
	  };
	})();
</script>
</body>
</html>
"""

SERVER_HTML = r"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PZ Modsmith - Server Settings</title>
  <style>
    body { margin: 0; font-family: system-ui, sans-serif; background: #10141c; color: #e8edf7; }
    main { max-width: 1100px; margin: 0 auto; padding: 24px 24px 64px; }
    .card { background: #171d29; border: 1px solid #324057; border-radius: 18px; padding: 20px; margin: 18px 0; }
    .muted { color: #aeb8ca; }
    button, .button { border: 0; background: #7aa2ff; color: #07101f; font-weight: 800; border-radius: 12px; padding: 12px 16px; cursor: pointer; text-decoration: none; display: inline-flex; margin: 6px 6px 6px 0; }
    .secondary { background: #202839; color: #e8edf7; border: 1px solid #324057; }
    input[type="file"], textarea { width: 100%; background: #0d121a; color: #e8edf7; border: 1px solid #324057; border-radius: 12px; padding: 12px 14px; font: inherit; }
    textarea { min-height: 170px; resize: vertical; }
    .setting { border: 1px solid #324057; border-radius: 14px; padding: 12px 14px; margin: 10px 0; background: rgba(0,0,0,.2); }
    .setting.changed { outline: 2px solid #ffc66d; }
    .setting-head { display: flex; gap: 10px; align-items: baseline; flex-wrap: wrap; }
    .pill { display: inline-flex; border-radius: 999px; padding: 3px 9px; font-size: .8rem; font-weight: 800; border: 1px solid #324057; color: #aeb8ca; }
    code { background: #0b1018; color: #d8e2f4; border: 1px solid #324057; border-radius: 10px; padding: 2px 6px; }
    .k { font-weight: 900; }
    .v { color: #d8e2f4; }
    select, input[type="text"] { width: 100%; background: #0d121a; color: #e8edf7; border: 1px solid #324057; border-radius: 12px; padding: 12px 14px; font: inherit; }
  </style>
</head>
<body>
<main>
  <h1>Server Settings</h1>
  <p class="muted">Editor for <code>pzserver.ini</code>. Saves as a downloadable file (does not overwrite your server automatically).</p>

  {% if error %}
    <section class="card"><strong>Error:</strong> {{ error }}</section>
  {% endif %}

  <section class="card">
    <form method="post" action="/server" enctype="multipart/form-data">
      <label class="k">Upload <code>pzserver.ini</code></label>
      <input type="file" name="server_ini_file" accept=".ini,.txt">

      <div style="margin-top: 12px;" class="muted">Or paste contents</div>
      <textarea name="server_ini_text" placeholder="Paste pzserver.ini here...">{{ server_ini_text or '' }}</textarea>

	      <button type="submit">Parse settings</button>
	      <a class="button secondary" href="/server/template">Load example template</a>
	      <a class="button secondary" href="/workshop">Workshop</a>
	      <a class="button secondary" href="/">Back to Mods</a>
	    </form>
  </section>

  {% if settings %}
    <section class="card">
      <form method="post" action="/server/save">
        <input type="hidden" name="server_ini_text" value="{{ server_ini_text }}">
        {% for s in settings %}
          <input type="hidden" name="key" value="{{ s.key }}">
          <input type="hidden" name="val_{{ s.key }}" value="{{ s.value }}">
        {% endfor %}
        <button type="submit">Save edited INI</button>
      </form>
    </section>

    <section class="card">
      <h2>Parsed Settings ({{ settings|length }})</h2>
      <form method="post" action="/server/save">
        <input type="hidden" name="server_ini_text" value="{{ server_ini_text }}">
        {% for s in settings %}
          <div class="setting" data-default="{{ (loaded_defaults.get(s.key, '') if loaded_defaults else '') }}">
            <div class="setting-head">
              <span class="k">{{ s.key }}</span>
              <span class="pill">{{ s.value_type }}</span>
              {% if s.min_value is not none %}<span class="pill">min {{ s.min_value }}</span>{% endif %}
              {% if s.max_value is not none %}<span class="pill">max {{ s.max_value }}</span>{% endif %}
              {% if loaded_defaults and loaded_defaults.get(s.key) is not none %}<span class="pill">loaded {{ loaded_defaults.get(s.key) }}</span>{% endif %}
              {% if s.default %}<span class="pill">game default {{ s.default }}</span>{% endif %}
            </div>
            <div style="margin-top:8px;">
              <input type="hidden" name="key" value="{{ s.key }}">
              {% if s.value_type == 'bool' %}
                <select name="val_{{ s.key }}">
                  <option value="true" {% if s.value|lower == 'true' %}selected{% endif %}>true</option>
                  <option value="false" {% if s.value|lower == 'false' %}selected{% endif %}>false</option>
                </select>
              {% elif s.value_type in ['int','float'] %}
                <input type="text" name="val_{{ s.key }}" value="{{ s.value }}">
              {% elif s.value_type in ['semicolon_list','comma_list'] or s.key in ['Mods','WorkshopItems','Map'] %}
                <textarea name="val_{{ s.key }}">{{ s.value }}</textarea>
              {% else %}
                <input type="text" name="val_{{ s.key }}" value="{{ s.value }}">
              {% endif %}
            </div>
            {% if s.comments %}
              <div class="muted" style="margin-top:8px; line-height:1.5;">
                {% for c in s.comments %}<div>{{ c }}</div>{% endfor %}
              </div>
            {% endif %}
          </div>
        {% endfor %}
        <button type="submit">Save edited INI</button>
      </form>
    </section>
  {% endif %}
</main>
<script>
function markChanged(root) {
  const cards = root.querySelectorAll('.setting[data-default]');
  cards.forEach(card => {
    const def = (card.getAttribute('data-default') || '').trim();
    if (!def) return;
    const input = card.querySelector('input[name^="val_"], textarea[name^="val_"], select[name^="val_"]');
    if (!input) return;
    const current = (input.value || '').trim();
    card.classList.toggle('changed', current !== def);
    const pill = card.querySelector('.pill._changed');
    if (pill) pill.remove();
    if (current !== def) {
      const p = document.createElement('span');
      p.className = 'pill _changed';
      p.textContent = 'changed';
      const head = card.querySelector('.setting-head');
      if (head) head.appendChild(p);
    }
  });
}
document.addEventListener('input', () => markChanged(document));
document.addEventListener('change', () => markChanged(document));
markChanged(document);
</script>
</body>
</html>
"""

SANDBOX_HTML = r"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PZ Modsmith - SandboxVars</title>
  <style>
    body { margin: 0; font-family: system-ui, sans-serif; background: #10141c; color: #e8edf7; }
    main { max-width: 1100px; margin: 0 auto; padding: 24px 24px 64px; }
    .card { background: #171d29; border: 1px solid #324057; border-radius: 18px; padding: 20px; margin: 18px 0; }
    .muted { color: #aeb8ca; }
    button, .button { border: 0; background: #7aa2ff; color: #07101f; font-weight: 800; border-radius: 12px; padding: 12px 16px; cursor: pointer; text-decoration: none; display: inline-flex; margin: 6px 6px 6px 0; }
    .secondary { background: #202839; color: #e8edf7; border: 1px solid #324057; }
    input[type="file"], textarea, input[type="text"], select { width: 100%; background: #0d121a; color: #e8edf7; border: 1px solid #324057; border-radius: 12px; padding: 12px 14px; font: inherit; }
    textarea { min-height: 170px; resize: vertical; }
    .setting { border: 1px solid #324057; border-radius: 14px; padding: 12px 14px; margin: 10px 0; background: rgba(0,0,0,.2); }
    .setting.changed { outline: 2px solid #ffc66d; }
    .setting-head { display: flex; gap: 10px; align-items: baseline; flex-wrap: wrap; }
    .pill { display: inline-flex; border-radius: 999px; padding: 3px 9px; font-size: .8rem; font-weight: 800; border: 1px solid #324057; color: #aeb8ca; }
    code { background: #0b1018; color: #d8e2f4; border: 1px solid #324057; border-radius: 10px; padding: 2px 6px; }
    .k { font-weight: 900; }
  </style>
</head>
<body>
<main>
  <h1>SandboxVars</h1>
  <p class="muted">Editor for <code>pzserver_SandboxVars.lua</code>. Saves as a downloadable file.</p>

  {% if error %}
    <section class="card"><strong>Error:</strong> {{ error }}</section>
  {% endif %}

  <section class="card">
    <form method="post" action="/sandbox" enctype="multipart/form-data">
      <label class="k">Upload <code>pzserver_SandboxVars.lua</code></label>
      <input type="file" name="sandbox_file" accept=".lua,.txt">

      <div style="margin-top: 12px;" class="muted">Or paste contents</div>
      <textarea name="sandbox_text" placeholder="Paste pzserver_SandboxVars.lua here...">{{ sandbox_text or '' }}</textarea>

	      <button type="submit">Parse settings</button>
	      <a class="button secondary" href="/sandbox/template">Load example template</a>
	      <a class="button secondary" href="/workshop">Workshop</a>
	      <a class="button secondary" href="/server">Server Settings</a>
	      <a class="button secondary" href="/">Back to Mods</a>
	    </form>
  </section>

  {% if settings %}
    <section class="card">
      <h2>Parsed Settings ({{ settings|length }})</h2>
      <form method="post" action="/sandbox/save">
        <input type="hidden" name="sandbox_text" value="{{ sandbox_text }}">
        {% for s in settings %}
          <div class="setting" data-default="{{ (loaded_defaults.get(s.key, '') if loaded_defaults else '') }}">
            <div class="setting-head">
              <span class="k">{{ s.key }}</span>
              <span class="pill">{{ s.value_type }}</span>
              {% if s.options %}<span class="pill">{{ s.options|length }} options</span>{% endif %}
              {% if loaded_defaults and loaded_defaults.get(s.key) is not none %}<span class="pill">loaded {{ loaded_defaults.get(s.key) }}</span>{% endif %}
              {% if s.default_raw %}<span class="pill">game default {{ s.default_raw }}</span>{% endif %}
            </div>
            <div style="margin-top:8px;">
              <input type="hidden" name="key" value="{{ s.key }}">
              {% if s.options %}
                <select name="val_{{ s.key }}">
                  {% for opt in s.options %}
                    <option value="{{ opt[0] }}" {% if (s.value_raw|string)|trim == (opt[0]|string) %}selected{% endif %}>{{ opt[0] }} - {{ opt[1] }}</option>
                  {% endfor %}
                </select>
              {% elif s.value_type == 'bool' %}
                <select name="val_{{ s.key }}">
                  <option value="true" {% if s.value_raw == 'true' %}selected{% endif %}>true</option>
                  <option value="false" {% if s.value_raw == 'false' %}selected{% endif %}>false</option>
                </select>
              {% elif s.value_type == 'int' %}
                <input type="text" name="val_{{ s.key }}" value="{{ s.value_raw }}">
              {% elif s.value_type == 'float' %}
                <input type="text" name="val_{{ s.key }}" value="{{ s.value_raw }}">
              {% else %}
                <input type="text" name="val_{{ s.key }}" value="{{ s.value_raw }}">
              {% endif %}
            </div>
            {% if s.comments %}
              <div class="muted" style="margin-top:8px; line-height:1.5;">
                {% for c in s.comments %}<div>{{ c }}</div>{% endfor %}
              </div>
            {% endif %}
          </div>
        {% endfor %}
        <button type="submit">Save edited SandboxVars</button>
      </form>
    </section>
  {% endif %}
</main>
<script>
function markChanged(root) {
  const cards = root.querySelectorAll('.setting[data-default]');
  cards.forEach(card => {
    const def = (card.getAttribute('data-default') || '').trim();
    if (!def) return;
    const input = card.querySelector('input[name^="val_"], textarea[name^="val_"], select[name^="val_"]');
    if (!input) return;
    const current = (input.value || '').trim();
    card.classList.toggle('changed', current !== def);
    const pill = card.querySelector('.pill._changed');
    if (pill) pill.remove();
    if (current !== def) {
      const p = document.createElement('span');
      p.className = 'pill _changed';
      p.textContent = 'changed';
      const head = card.querySelector('.setting-head');
      if (head) head.appendChild(p);
    }
  });
}
document.addEventListener('input', () => markChanged(document));
document.addEventListener('change', () => markChanged(document));
markChanged(document);
</script>
</body>
</html>
"""

RESULT_HTML = r"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PZ Modsmith Results</title>
  <style>
    body { margin: 0; font-family: system-ui, sans-serif; background: #10141c; color: #e8edf7; }
    main { max-width: 1100px; margin: 0 auto; padding: 32px 24px 64px; }
    .card { background: #171d29; border: 1px solid #324057; border-radius: 18px; padding: 20px; margin: 18px 0; }
    pre { white-space: pre-wrap; overflow-wrap: anywhere; background: #0b1018; border: 1px solid #324057; border-radius: 12px; padding: 14px; }
    button, .button { border: 0; background: #7aa2ff; color: #07101f; font-weight: 800; border-radius: 12px; padding: 12px 16px; cursor: pointer; text-decoration: none; display: inline-flex; margin: 6px 6px 6px 0; }
    .secondary { background: #202839; color: #e8edf7; border: 1px solid #324057; }
    .muted { color: #aeb8ca; }
  </style>
</head>
<body>
<main>
  <h1>PZ Modsmith Results</h1>
  <p class="muted">Copy these into your server config after one last sanity check. Zomboid mod configs are legally required to be a little haunted.</p>

  <section class="card">
    <h2>WorkshopItems</h2>
    <button onclick="copyText('workshop')">Copy WorkshopItems</button>
    <pre id="workshop">{{ result.workshop_line }}</pre>
  </section>

  <section class="card">
    <h2>Mods</h2>
    <button onclick="copyText('mods')">Copy Mods</button>
    <pre id="mods">{{ result.mods_line }}</pre>
  </section>

	  {% if updated_ini %}
	  <section class="card">
    <h2>Updated pzserver.ini</h2>
    <p class="muted">Includes refreshed <code>WorkshopItems=</code> and <code>Mods=</code> based on your selections.</p>
	    <form method="post" action="/download-ini-token">
	      <input type="hidden" name="text_token" value="{{ updated_ini_token | e }}">
	      <button type="submit">Download pzserver.ini</button>
	    </form>
	    <pre>{{ updated_ini }}</pre>
	  </section>
	  {% endif %}

	  <section class="card">
	    <form method="post" action="/download-zip">
	      <input type="hidden" name="state_token" value="{{ state_token | e }}">
	      <button type="submit">Download report ZIP</button>
	      <a class="button secondary" href="/">Start over</a>
	    </form>
	  </section>
</main>
<script>
async function copyText(id) {
  const text = document.getElementById(id).innerText;
  await navigator.clipboard.writeText(text);
}
</script>
</body>
</html>
"""


def find_available_port(host: str, start_port: int) -> int:
    port = start_port
    while port <= 65535:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind((host, port))
            except OSError:
                port += 1
                continue
            return port
    raise SystemExit(f"No available port found at or above {start_port}.")


def browser_url_for_host(host: str, port: int) -> str:
    browser_host = "127.0.0.1" if host in {"0.0.0.0", "::"} else host
    return f"http://{browser_host}:{port}"


def open_browser(url: str) -> None:
    threading.Timer(0.5, webbrowser.open, args=(url,)).start()


def run_app(host: str = "127.0.0.1", port: int = DEFAULT_PORT) -> None:
    available_port = find_available_port(host, port)
    url = browser_url_for_host(host, available_port)
    print(f"Opening {url}")
    open_browser(url)
    run_web(host, available_port)


def run_web(host: str = "127.0.0.1", port: int = DEFAULT_PORT) -> None:
    try:
        from flask import Flask, Response, render_template_string, request, send_file
    except ImportError as exc:
        raise SystemExit(
            "Flask is required for the web UI. Install it with:\n\n"
            "  python3 -m venv .venv\n"
            "  source .venv/bin/activate\n"
            "  pip install flask\n"
        ) from exc

    app = Flask(__name__)
    app.secret_key = secrets.token_hex(16)

    # In-memory store for large text blobs (INI text, etc.) so we don't exceed
    # request size limits by stuffing big content into hidden form fields.
    _TEXT_STORE: dict[str, tuple[float, str]] = {}
    _TEXT_STORE_TTL_SECONDS = 60 * 30  # 30 minutes
    _TEXT_STORE_MAX_ITEMS = 500

    def _store_text(text: str) -> str:
        now = time.time()
        expired = [k for k, (ts, _) in _TEXT_STORE.items() if (now - ts) > _TEXT_STORE_TTL_SECONDS]
        for k in expired:
            _TEXT_STORE.pop(k, None)

        if len(_TEXT_STORE) >= _TEXT_STORE_MAX_ITEMS:
            oldest = sorted(_TEXT_STORE.items(), key=lambda kv: kv[1][0])[: max(1, len(_TEXT_STORE) - _TEXT_STORE_MAX_ITEMS + 1)]
            for k, _ in oldest:
                _TEXT_STORE.pop(k, None)

        token = secrets.token_urlsafe(16)
        _TEXT_STORE[token] = (now, text)
        return token

    def _load_text(token: str) -> str:
        if not token:
            return ""
        item = _TEXT_STORE.get(token)
        if not item:
            return ""
        ts, text = item
        if (time.time() - ts) > _TEXT_STORE_TTL_SECONDS:
            _TEXT_STORE.pop(token, None)
            return ""
        return text

    # Small in-memory cache for Steam API calls to keep the UI responsive.
    _STEAM_CACHE: dict[tuple, tuple[float, object]] = {}
    _STEAM_CACHE_TTL_SECONDS = 60 * 10  # 10 minutes
    _STEAM_CACHE_MAX_ITEMS = 800

    def _steam_cache_get(key: tuple) -> object | None:
        item = _STEAM_CACHE.get(key)
        if not item:
            return None
        ts, value = item
        if (time.time() - ts) > _STEAM_CACHE_TTL_SECONDS:
            _STEAM_CACHE.pop(key, None)
            return None
        return value

    def _steam_cache_set(key: tuple, value: object) -> None:
        # Lazy cleanup
        now = time.time()
        expired = [k for k, (ts, _) in _STEAM_CACHE.items() if (now - ts) > _STEAM_CACHE_TTL_SECONDS]
        for k in expired:
            _STEAM_CACHE.pop(k, None)
        if len(_STEAM_CACHE) >= _STEAM_CACHE_MAX_ITEMS:
            oldest = sorted(_STEAM_CACHE.items(), key=lambda kv: kv[1][0])[: max(1, len(_STEAM_CACHE) - _STEAM_CACHE_MAX_ITEMS + 1)]
            for k, _ in oldest:
                _STEAM_CACHE.pop(k, None)
        _STEAM_CACHE[key] = (now, value)

    def cached_get_workshop_item_summaries(ids: list[str]) -> dict:
        clean = tuple(dedupe_keep_order(str(i).strip() for i in ids if str(i).strip().isdigit()))
        if not clean:
            return {}
        key = ("summaries", clean)
        cached = _steam_cache_get(key)
        if isinstance(cached, dict):
            return cached
        value = get_workshop_item_summaries(list(clean))
        _steam_cache_set(key, value)
        return value

    def cached_query_workshop(
        *,
        api_key: str,
        search_text: str,
        page: int,
        per_page: int,
        query_type: int,
        required_tags: list[str] | None,
        cursor: str,
    ) -> dict:
        tags_key = tuple(required_tags or ())
        key = ("query", search_text.strip(), int(page), int(per_page), int(query_type), tags_key, cursor)
        cached = _steam_cache_get(key)
        if isinstance(cached, dict):
            return cached
        value = query_workshop(
            api_key=api_key,
            search_text=search_text,
            page=page,
            per_page=per_page,
            query_type=query_type,
            required_tags=required_tags,
            cursor=cursor,
        )
        _steam_cache_set(key, value)
        return value

    @app.get("/")
    def index():
        return render_template_string(
            INDEX_HTML,
            workshop_path=detect_default_workshop_path(),
            result=None,
            error=None,
            state_json="",
            server_ini_text="",
            workshop_meta={},
            state_token="",
            server_ini_token="",
        )

    @app.get("/workshop")
    def workshop_get():
        all_tags = [
            "Build 40",
            "Build 41",
            "Build 42",
            "Animals",
            "Audio",
            "Balance",
            "Building",
            "Clothing/Armor",
            "Farming",
            "Food",
            "Framework",
            "Hardmode",
            "Interface",
            "Items",
            "Language/Translation",
            "Literature",
            "Map",
            "Military",
            "Misc",
            "Models",
            "Multiplayer",
            "Pop Culture",
            "QoL",
            "Realistic",
            "Silly/Fun",
            "Skills",
            "Textures",
            "Traits",
            "Vehicles",
            "Weapons",
            "WIP",
        ]
        return render_template_string(
            WORKSHOP_HTML,
            q="",
            sort="popular",
            tags="",
            all_tags=all_tags,
            selected_tags=[],
            results=None,
            searched=False,
            ini_ids=set(),
            ini_meta={},
            workshop_items="",
            mods="",
            updated_ini_text=None,
            updated_ini_token="",
            updated_workshop_items_line="",
            updated_mods_line="",
            analyze_text="",
            default_workshop_path=detect_default_workshop_path(),
            page=1,
            cursor="*",
            total=0,
            has_prev=False,
            has_next=False,
            debug="",
            error=None,
        )

    @app.post("/workshop/search")
    def workshop_search():
        q = request.form.get("q", "") or ""
        sort = request.form.get("sort", "relevance") or "relevance"
        tags = request.form.get("tags", "") or ""
        workshop_items = request.form.get("workshop_items", "") or ""
        mods = request.form.get("mods", "") or ""
        api_key = (request.form.get("steam_api_key", "") or "").strip()
        try:
            page = int(request.form.get("page", "1") or "1")
        except ValueError:
            page = 1
        page = max(page, 1)
        cursor = (request.form.get("cursor", "") or "").strip() or "*"

        sort_map = {
            "relevance": QUERY_TYPE_RANKED_BY_TEXT_SEARCH,
            "popular": QUERY_TYPE_RANKED_BY_TOTAL_UNIQUE_SUBSCRIPTIONS,
            "subscribed": QUERY_TYPE_RANKED_BY_TOTAL_UNIQUE_SUBSCRIPTIONS,
            "trending": QUERY_TYPE_RANKED_BY_TREND,
            "new": QUERY_TYPE_RANKED_BY_PUBLICATION_DATE,
            "updated": QUERY_TYPE_RANKED_BY_LAST_UPDATED_DATE,
        }
        # Steam Workshop defaults to "Most Popular" style browsing.
        query_type = sort_map.get(sort, QUERY_TYPE_RANKED_BY_TOTAL_UNIQUE_SUBSCRIPTIONS)
        all_tags = [
            "Build 40",
            "Build 41",
            "Build 42",
            "Animals",
            "Audio",
            "Balance",
            "Building",
            "Clothing/Armor",
            "Farming",
            "Food",
            "Framework",
            "Hardmode",
            "Interface",
            "Items",
            "Language/Translation",
            "Literature",
            "Map",
            "Military",
            "Misc",
            "Models",
            "Multiplayer",
            "Pop Culture",
            "QoL",
            "Realistic",
            "Silly/Fun",
            "Skills",
            "Textures",
            "Traits",
            "Vehicles",
            "Weapons",
            "WIP",
        ]
        selected_tags = [t.strip() for t in tags.split(",") if t.strip()]
        required_tags = selected_tags
        ini_ids: set[str] = set()
        for part in workshop_items.replace(",", ";").split(";"):
            p = part.strip()
            if p.isdigit():
                ini_ids.add(p)
        try:
            ini_meta = cached_get_workshop_item_summaries(sorted(ini_ids))
        except Exception:
            ini_meta = {}

        debug = f"q={q!r} sort={sort!r} tags={tags!r} query_type={query_type} cursor={cursor!r} page={page}"

        try:
            payload = cached_query_workshop(
                api_key=api_key,
                search_text=q,
                page=page,
                per_page=24,
                query_type=query_type,
                required_tags=required_tags or None,
                cursor=cursor,
            )
            response = (payload or {}).get("response") or {}
            total = int(response.get("total") or 0)
            next_cursor = response.get("next_cursor") or response.get("nextCursor") or ""
            raw = response.get("publishedfiledetails") or []
            results = []
            for d in raw:
                if not isinstance(d, dict):
                    continue
                wid = str(d.get("publishedfileid", "")).strip()
                if not wid.isdigit():
                    continue
                results.append(
                    {
                        "publishedfileid": wid,
                        "title": d.get("title") or "",
                        "preview_url": d.get("preview_url") or "",
                        "subscriptions": int(d.get("subscriptions") or 0),
                    }
                )
            return render_template_string(
                WORKSHOP_HTML,
                q=q,
                sort=sort,
                tags=tags,
                all_tags=all_tags,
                selected_tags=selected_tags,
                results=results,
                searched=True,
                ini_ids=ini_ids,
                ini_meta=ini_meta,
                workshop_items=workshop_items,
                mods=mods,
                updated_ini_text=None,
                updated_ini_token="",
                updated_workshop_items_line="",
                updated_mods_line="",
                analyze_text="",
                default_workshop_path=detect_default_workshop_path(),
                page=page,
                cursor=(next_cursor or cursor),
                total=total,
                has_prev=page > 1,
                has_next=(page * 24) < total if total else (len(results) == 24),
                debug=debug + f" total={total} returned={len(results)} next_cursor={(next_cursor or '')!r}",
                error=None,
            )
        except SteamApiKeyMissing as exc:
            return (
                render_template_string(
                    WORKSHOP_HTML,
                    q=q,
                    sort=sort,
                    tags=tags,
                    all_tags=all_tags,
                    selected_tags=selected_tags,
                    results=None,
                    searched=True,
                    ini_ids=ini_ids,
                    ini_meta=ini_meta,
                    workshop_items=workshop_items,
                    mods=mods,
                    updated_ini_text=None,
                    updated_ini_token="",
                    updated_workshop_items_line="",
                    updated_mods_line="",
                    analyze_text="",
                    default_workshop_path=detect_default_workshop_path(),
                    page=page,
                    cursor=cursor,
                    total=0,
                    has_prev=False,
                    has_next=False,
                    debug=debug,
                    error=str(exc),
                ),
                400,
            )
        except Exception as exc:
            return (
                render_template_string(
                    WORKSHOP_HTML,
                    q=q,
                    sort=sort,
                    tags=tags,
                    all_tags=all_tags,
                    selected_tags=selected_tags,
                    results=None,
                    searched=True,
                    ini_ids=ini_ids,
                    ini_meta=ini_meta,
                    workshop_items=workshop_items,
                    mods=mods,
                    updated_ini_text=None,
                    updated_ini_token="",
                    updated_workshop_items_line="",
                    updated_mods_line="",
                    analyze_text="",
                    default_workshop_path=detect_default_workshop_path(),
                    page=page,
                    cursor=cursor,
                    total=0,
                    has_prev=False,
                    has_next=False,
                    debug=debug,
                    error=f"Workshop search failed: {exc}",
                ),
                500,
            )

    @app.post("/workshop/add")
    def workshop_add():
        workshop_items = request.form.get("workshop_items", "") or ""
        mods = request.form.get("mods", "") or ""
        selected_ids = request.form.getlist("wid")
        q = request.form.get("q", "") or ""
        sort = request.form.get("sort", "relevance") or "relevance"
        tags = request.form.get("tags", "") or ""
        try:
            page = int(request.form.get("page", "1") or "1")
        except ValueError:
            page = 1
        page = max(page, 1)
        cursor = (request.form.get("cursor", "") or "").strip() or "*"

        clean_selected = [s.strip() for s in selected_ids if s.strip().isdigit()]
        clean_selected = dedupe_keep_order(clean_selected)
        all_tags = [
            "Build 40",
            "Build 41",
            "Build 42",
            "Animals",
            "Audio",
            "Balance",
            "Building",
            "Clothing/Armor",
            "Farming",
            "Food",
            "Framework",
            "Hardmode",
            "Interface",
            "Items",
            "Language/Translation",
            "Literature",
            "Map",
            "Military",
            "Misc",
            "Models",
            "Multiplayer",
            "Pop Culture",
            "QoL",
            "Realistic",
            "Silly/Fun",
            "Skills",
            "Textures",
            "Traits",
            "Vehicles",
            "Weapons",
            "WIP",
        ]
        selected_tags = [t.strip() for t in tags.split(",") if t.strip()]

        if not clean_selected:
            return (
                render_template_string(
                    WORKSHOP_HTML,
                    q=q,
                    sort=sort,
                    tags=tags,
                    all_tags=all_tags,
                    selected_tags=selected_tags,
                    results=None,
                    searched=True,
                    ini_ids=set(),
                    ini_meta={},
                    workshop_items=workshop_items,
                    mods=mods,
                    updated_ini_text=None,
                    updated_ini_token="",
                    updated_workshop_items_line="",
                    updated_mods_line="",
                    analyze_text="",
                    default_workshop_path=detect_default_workshop_path(),
                    page=page,
                    cursor=cursor,
                    total=0,
                    has_prev=page > 1,
                    has_next=False,
                    error="No Workshop items selected.",
                ),
                400,
            )

        existing_ids: list[str] = []
        for part in workshop_items.replace(",", ";").split(";"):
            p = part.strip()
            if p.isdigit():
                existing_ids.append(p)

        existing_mod_ids: list[str] = []
        for part in mods.replace(",", ";").split(";"):
            p = part.strip()
            if p:
                existing_mod_ids.append(p)

        manual_mod_ids: list[str] = []
        for wid in clean_selected:
            raw = (request.form.get(f"modids_{wid}", "") or "").strip()
            if not raw:
                continue
            # Support "a;b;c", "a, b, c", or whitespace-separated.
            normalized = raw.replace(",", ";").replace("\n", ";").replace("\t", ";")
            for part in normalized.split(";"):
                mod_id = part.strip()
                if mod_id:
                    manual_mod_ids.append(mod_id)

        merged = dedupe_keep_order([*existing_ids, *clean_selected])
        merged_mods = dedupe_keep_order([*existing_mod_ids, *manual_mod_ids])
        updated_workshop_items_line = "WorkshopItems=" + ";".join(merged)
        updated_mods_line = "Mods=" + ";".join(merged_mods)
        # Minimal INI text for download / cross-page handoff.
        updated_ini_text = updated_workshop_items_line + "\n" + updated_mods_line + "\n"
        updated_ini_token = _store_text(updated_ini_text)
        analyze_text = "WorkshopItems=" + ";".join(merged)
        try:
            ini_meta = cached_get_workshop_item_summaries(merged)
        except Exception:
            ini_meta = {}

        return render_template_string(
            WORKSHOP_HTML,
            q=q,
            sort=sort,
            tags=tags,
            all_tags=all_tags,
            selected_tags=selected_tags,
            results=None,
            searched=True,
            ini_ids=set(merged),
            ini_meta=ini_meta,
            workshop_items=";".join(merged),
            mods=";".join(merged_mods),
            updated_ini_text=updated_ini_text,
            updated_ini_token=updated_ini_token,
            updated_workshop_items_line=updated_workshop_items_line,
            updated_mods_line=updated_mods_line,
            analyze_text=analyze_text,
            default_workshop_path=detect_default_workshop_path(),
            page=page,
            cursor=cursor,
            total=0,
            has_prev=page > 1,
            has_next=False,
            error=None,
        )

    @app.post("/workshop/remove")
    def workshop_remove():
        workshop_items = request.form.get("workshop_items", "") or ""
        mods = request.form.get("mods", "") or ""
        q = request.form.get("q", "") or ""
        sort = request.form.get("sort", "relevance") or "relevance"
        tags = request.form.get("tags", "") or ""
        try:
            page = int(request.form.get("page", "1") or "1")
        except ValueError:
            page = 1
        page = max(page, 1)
        cursor = (request.form.get("cursor", "") or "").strip() or "*"

        remove_wids = set(v.strip() for v in request.form.getlist("remove_wid") if v.strip().isdigit())
        current_wids = [p.strip() for p in workshop_items.replace(",", ";").split(";") if p.strip().isdigit()]
        kept_wids = [w for w in current_wids if w not in remove_wids]

        remove_modids_raw = (request.form.get("remove_modids", "") or "").strip()
        remove_modids: set[str] = set()
        if remove_modids_raw:
            normalized = remove_modids_raw.replace(",", ";").replace("\n", ";").replace("\t", ";")
            remove_modids = set(p.strip() for p in normalized.split(";") if p.strip())
        current_mods = [p.strip() for p in mods.replace(",", ";").split(";") if p.strip()]
        kept_mods = [m for m in current_mods if m not in remove_modids]

        ini_ids = set(kept_wids)
        try:
            ini_meta = cached_get_workshop_item_summaries(kept_wids)
        except Exception:
            ini_meta = {}

        return render_template_string(
            WORKSHOP_HTML,
            q=q,
            sort=sort,
            tags=tags,
            all_tags=[
                "Build 40",
                "Build 41",
                "Build 42",
                "Animals",
                "Audio",
                "Balance",
                "Building",
                "Clothing/Armor",
                "Farming",
                "Food",
                "Framework",
                "Hardmode",
                "Interface",
                "Items",
                "Language/Translation",
                "Literature",
                "Map",
                "Military",
                "Misc",
                "Models",
                "Multiplayer",
                "Pop Culture",
                "QoL",
                "Realistic",
                "Silly/Fun",
                "Skills",
                "Textures",
                "Traits",
                "Vehicles",
                "Weapons",
                "WIP",
            ],
            selected_tags=[t.strip() for t in tags.split(",") if t.strip()],
            results=None,
            searched=True,
            ini_ids=ini_ids,
            ini_meta=ini_meta,
            workshop_items=";".join(kept_wids),
            mods=";".join(kept_mods),
            updated_ini_text=None,
            updated_ini_token="",
            updated_workshop_items_line="",
            updated_mods_line="",
            analyze_text="",
            default_workshop_path=detect_default_workshop_path(),
            page=page,
            cursor=cursor,
            total=0,
            has_prev=page > 1,
            has_next=False,
            debug="",
            error=None,
        )

    @app.get("/server")
    def server_get():
        return render_template_string(
            SERVER_HTML,
            settings=None,
            error=None,
            server_ini_text="",
            loaded_defaults={},
        )

    @app.post("/server")
    def server_post():
        try:
            pasted_text = request.form.get("server_ini_text", "") or ""
            uploaded = request.files.get("server_ini_file")
            text = pasted_text
            if uploaded and uploaded.filename:
                text = uploaded.read().decode("utf-8", errors="replace")

            if not text.strip():
                raise ValueError("Upload or paste a pzserver.ini first.")

            settings = parse_pzserver_ini(text)
            if not settings:
                raise ValueError("No settings found (expected KEY=VALUE lines).")

            return render_template_string(
                SERVER_HTML,
                settings=settings,
                error=None,
                server_ini_text=text,
                loaded_defaults={s.key: s.value for s in settings},
            )
        except Exception as exc:
            return (
                render_template_string(
                    SERVER_HTML,
                    settings=None,
                    error=str(exc),
                    server_ini_text=request.form.get("server_ini_text", "") or "",
                    loaded_defaults={},
                ),
                400,
            )

    @app.post("/server/save")
    def server_save():
        text = request.form.get("server_ini_text", "") or ""
        keys = request.form.getlist("key")
        updates: dict[str, str] = {}
        for k in keys:
            updates[k] = request.form.get(f"val_{k}", "")
        updated = apply_pzserver_ini_edits(text, updates)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".ini")
        tmp.write(updated.encode("utf-8", errors="replace"))
        tmp.close()
        return send_file(tmp.name, as_attachment=True, download_name="pzserver.ini")

    @app.get("/server/template")
    def server_template():
        try:
            with importlib_resources.files("pz_modsmith").joinpath("templates/server/pzserver.ini").open(
                "r",
                encoding="utf-8",
                errors="replace",
            ) as f:
                text = f.read()
            settings = parse_pzserver_ini(text)
            return render_template_string(
                SERVER_HTML,
                settings=settings,
                error=None,
                server_ini_text=text,
                loaded_defaults={s.key: s.value for s in settings},
            )
        except Exception as exc:
            return (
                render_template_string(
                    SERVER_HTML,
                    settings=None,
                    error=f"Could not load template: {exc}",
                    server_ini_text="",
                    loaded_defaults={},
                ),
                500,
            )

    @app.get("/sandbox")
    def sandbox_get():
        return render_template_string(
            SANDBOX_HTML,
            settings=None,
            error=None,
            sandbox_text="",
            loaded_defaults={},
        )

    @app.post("/sandbox")
    def sandbox_post():
        try:
            pasted_text = request.form.get("sandbox_text", "") or ""
            uploaded = request.files.get("sandbox_file")
            text = pasted_text
            if uploaded and uploaded.filename:
                text = uploaded.read().decode("utf-8", errors="replace")
            if not text.strip():
                raise ValueError("Upload or paste a pzserver_SandboxVars.lua first.")

            settings = parse_sandbox_vars_lua(text)
            if not settings:
                raise ValueError("No SandboxVars settings found (expected `SandboxVars = { ... }`).")

            return render_template_string(
                SANDBOX_HTML,
                settings=settings,
                error=None,
                sandbox_text=text,
                loaded_defaults={s.key: s.value_raw for s in settings},
            )
        except Exception as exc:
            return (
                render_template_string(
                    SANDBOX_HTML,
                    settings=None,
                    error=str(exc),
                    sandbox_text=request.form.get("sandbox_text", "") or "",
                    loaded_defaults={},
                ),
                400,
            )

    @app.post("/sandbox/save")
    def sandbox_save():
        text = request.form.get("sandbox_text", "") or ""
        keys = request.form.getlist("key")
        updates: dict[str, str] = {}
        for k in keys:
            updates[k] = request.form.get(f"val_{k}", "")
        updated = apply_sandbox_vars_edits(text, updates)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".lua")
        tmp.write(updated.encode("utf-8", errors="replace"))
        tmp.close()
        return send_file(tmp.name, as_attachment=True, download_name="pzserver_SandboxVars.lua")

    @app.get("/sandbox/template")
    def sandbox_template():
        try:
            with importlib_resources.files("pz_modsmith").joinpath("templates/server/pzserver_SandboxVars.lua").open(
                "r",
                encoding="utf-8",
                errors="replace",
            ) as f:
                text = f.read()
            settings = parse_sandbox_vars_lua(text)
            return render_template_string(
                SANDBOX_HTML,
                settings=settings,
                error=None,
                sandbox_text=text,
                loaded_defaults={s.key: s.value_raw for s in settings},
            )
        except Exception as exc:
            return (
                render_template_string(
                    SANDBOX_HTML,
                    settings=None,
                    error=f"Could not load template: {exc}",
                    sandbox_text="",
                    loaded_defaults={},
                ),
                500,
            )

    @app.post("/analyze")
    def analyze_route():
        workshop_path_raw = request.form.get("workshop_path", "").strip()
        pasted_text = request.form.get("pasted_text", "")
        uploaded = request.files.get("console_file")
        server_ini_file = request.files.get("server_ini_file")
        server_ini_text = request.form.get("server_ini_text", "") or ""
        if not server_ini_text.strip():
            server_ini_text = _load_text((request.form.get("server_ini_token", "") or "").strip())

        try:
            workshop_path = expand_path(workshop_path_raw)
            if not workshop_path.exists():
                raise ValueError(f"Workshop path does not exist: {workshop_path}")

            text = pasted_text or ""
            if uploaded and uploaded.filename:
                text += "\n" + uploaded.read().decode("utf-8", errors="replace")

            if server_ini_file and server_ini_file.filename:
                server_ini_text = server_ini_file.read().decode("utf-8", errors="replace")
                # If user didn't paste anything, prefer WorkshopItems= from the INI.
                if not text.strip():
                    ini_ws = get_first_ini_value(server_ini_text, "WorkshopItems")
                    if ini_ws:
                        text = ini_ws
                    else:
                        # Fallback: use INI text (may be noisy), but still lets users proceed
                        # if they pasted Workshop IDs elsewhere in the file.
                        text = server_ini_text

            if not text.strip():
                raise ValueError("Paste a console log / Workshop IDs or upload console.txt.")

            workshop_ids = extract_workshop_ids_from_console_text(text)
            active_mod_ids = extract_active_mod_ids_from_console_text(text)
            if not workshop_ids:
                workshop_ids = extract_workshop_ids_from_free_text(text)
            if not workshop_ids and not active_mod_ids:
                raise ValueError(
                    "No Workshop IDs found (and no active Mod IDs to infer from) in the provided text/file."
                )

            if workshop_ids and request.form.get("fetch_steam_deps"):
                try:
                    steam_api_key = (request.form.get("steam_api_key", "") or "").strip() or (
                        os.environ.get("PZ_MODSMITH_STEAM_API_KEY") or os.environ.get("STEAM_WEB_API_KEY") or ""
                    ).strip()
                    workshop_ids = expand_workshop_ids_with_collections_and_required_items(
                        workshop_ids, api_key=steam_api_key
                    )
                except Exception:
                    # Treat Steam lookup as best-effort; local analysis still works.
                    pass

            prefer_highest_version = bool(request.form.get("prefer_highest_version"))
            result = analyze(
                workshop_ids,
                workshop_path,
                active_mod_ids,
                console_text=text,
                prefer_highest_version=prefer_highest_version,
            )
            try:
                workshop_meta = cached_get_workshop_item_summaries(workshop_ids)
            except Exception:
                workshop_meta = {}
            state_json = json.dumps(result_to_dict(result))
            state_token = _store_text(state_json)
            server_ini_token = _store_text(server_ini_text) if server_ini_text.strip() else ""
            return render_template_string(
                INDEX_HTML,
                workshop_path=str(workshop_path),
                result=result,
                error=None,
                state_json=state_json,
                server_ini_text=server_ini_text,
                workshop_meta=workshop_meta,
                state_token=state_token,
                server_ini_token=server_ini_token,
            )
        except Exception as exc:
            return render_template_string(
                INDEX_HTML,
                workshop_path=workshop_path_raw or detect_default_workshop_path(),
                result=None,
                error=str(exc),
                state_json="",
                server_ini_text=server_ini_text,
                workshop_meta={},
                state_token="",
                server_ini_token=_store_text(server_ini_text) if server_ini_text.strip() else "",
            ), 400

    @app.post("/generate")
    def generate_route():
        state_token = request.form.get("state_token", "") or ""
        state_raw = _load_text(state_token) if state_token else (request.form.get("state", "") or "")
        if not state_raw.strip():
            return ("Missing state.", 400)
        state = json.loads(state_raw)
        result = dict_to_result(state)
        include_workshop_ids = set(v.strip() for v in request.form.getlist("include_workshop_id") if v.strip())
        if include_workshop_ids:
            result.workshop_ids = [wid for wid in result.workshop_ids if wid in include_workshop_ids]
            result.items = [it for it in result.items if it.workshop_id in include_workshop_ids]
        selected: dict[str, list[str]] = {}
        for item in result.items:
            selected[item.workshop_id] = [v for v in request.form.getlist(f"selected_{item.workshop_id}") if v.strip()]
        apply_selection(result, selected)

        # Allow manual Mod IDs for missing items (no mod.info available).
        for item in result.items:
            raw = (request.form.get(f"manual_modids_{item.workshop_id}", "") or "").strip()
            if not raw:
                continue
            normalized = raw.replace(",", ";").replace("\n", ";").replace("\t", ";")
            manual_ids = [p.strip() for p in normalized.split(";") if p.strip()]
            if manual_ids:
                item.selected_mod_ids = dedupe_keep_order([*item.selected_mod_ids, *manual_ids])

        state_json = json.dumps(result_to_dict(result))
        state_token = _store_text(state_json)
        server_ini_text = _load_text((request.form.get("server_ini_token", "") or "").strip()) or (
            request.form.get("server_ini_text", "") or ""
        )
        updated_ini = ""
        updated_ini_token = ""
        if server_ini_text.strip():
            updates = {
                "WorkshopItems": ";".join(result.workshop_ids),
                "Mods": ";".join(result.selected_mod_ids),
            }
            updated_ini = apply_pzserver_ini_edits(server_ini_text, updates)
            updated_ini_token = _store_text(updated_ini)
        return render_template_string(
            RESULT_HTML,
            result=result,
            state_json=state_json,
            state_token=state_token,
            updated_ini=updated_ini,
            updated_ini_token=updated_ini_token,
        )

    @app.post("/download-ini")
    def download_ini_route():
        text = request.form.get("updated_ini", "") or ""
        if not text.strip():
            return ("Missing INI text.", 400)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".ini")
        tmp.write(text.encode("utf-8", errors="replace"))
        tmp.close()
        return send_file(tmp.name, as_attachment=True, download_name="pzserver.ini")

    @app.post("/download-ini-token")
    def download_ini_token_route():
        token = request.form.get("text_token", "") or ""
        text = _load_text(token)
        if not text.strip():
            return ("Missing INI text.", 400)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".ini")
        tmp.write(text.encode("utf-8", errors="replace"))
        tmp.close()
        return send_file(tmp.name, as_attachment=True, download_name="pzserver.ini")

    @app.post("/download-zip")
    def download_zip_route():
        state_token = request.form.get("state_token", "") or ""
        state_raw = _load_text(state_token) if state_token else (request.form.get("state", "") or "")
        if not state_raw.strip():
            return ("Missing state.", 400)
        state = json.loads(state_raw)
        result = dict_to_result(state)
        data = zip_reports(result)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".zip")
        tmp.write(data)
        tmp.close()
        return send_file(tmp.name, as_attachment=True, download_name="pzmodsmith-output.zip")

    print(f"{APP_NAME} running at http://{host}:{port}")
    app.run(host=host, port=port, debug=False)
