from __future__ import annotations

import json
import secrets
import socket
import tempfile
import threading
import webbrowser
from importlib import resources as importlib_resources

from .constants import APP_NAME, DEFAULT_PORT
from .utils import expand_path, detect_default_workshop_path
from .models import AnalysisResult
from .log_parser import (
    extract_workshop_ids_from_console_text,
    extract_active_mod_ids_from_console_text,
    extract_workshop_ids_from_free_text,
)
from .analysis import analyze, apply_selection
from .serialization import result_to_dict, dict_to_result
from .reports import zip_reports
from .steam_api import expand_workshop_ids_with_required_items
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
        <input type="checkbox" name="prefer_highest_version" value="1" checked>
        Prefer highest version when the same Mod ID appears multiple times
      </label>
      <p class="muted tiny">Collapses multiple <code>mod.info</code> variants like <code>42.0</code>/<code>42.15</code> to the newest one.</p>

      <button type="submit">Analyze mods</button>
    </form>
  </section>

  {% if result %}
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
      <input type="hidden" name="state" value="{{ state_json }}">
      <input type="hidden" name="server_ini_text" value="{{ server_ini_text | e }}">
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
              <div>
                <strong>Workshop {{ item.workshop_id }}</strong>
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
              <a class="button secondary tiny" target="_blank" href="https://steamcommunity.com/sharedfiles/filedetails/?id={{ item.workshop_id }}">Steam page</a>
            </div>
            <div class="item-body">
              {% if not item.mods %}
                <p class="muted">No downloaded mod.info found for this Workshop item.</p>
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
    <form method="post" action="/download-ini">
      <input type="hidden" name="updated_ini" value="{{ updated_ini }}">
      <button type="submit">Download pzserver.ini</button>
    </form>
    <pre>{{ updated_ini }}</pre>
  </section>
  {% endif %}

  <section class="card">
    <form method="post" action="/download-zip">
      <input type="hidden" name="state" value="{{ state_json }}">
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

    @app.get("/")
    def index():
        return render_template_string(
            INDEX_HTML,
            workshop_path=detect_default_workshop_path(),
            result=None,
            error=None,
            state_json="",
            server_ini_text="",
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
        server_ini_text = ""

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
                    workshop_ids = expand_workshop_ids_with_required_items(workshop_ids)
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
            state_json = json.dumps(result_to_dict(result))
            return render_template_string(
                INDEX_HTML,
                workshop_path=str(workshop_path),
                result=result,
                error=None,
                state_json=state_json,
                server_ini_text=server_ini_text,
            )
        except Exception as exc:
            return render_template_string(
                INDEX_HTML,
                workshop_path=workshop_path_raw or detect_default_workshop_path(),
                result=None,
                error=str(exc),
                state_json="",
                server_ini_text=server_ini_text,
            ), 400

    @app.post("/generate")
    def generate_route():
        state = json.loads(request.form["state"])
        result = dict_to_result(state)
        selected: dict[str, list[str]] = {}
        for item in result.items:
            selected[item.workshop_id] = [v for v in request.form.getlist(f"selected_{item.workshop_id}") if v.strip()]
        apply_selection(result, selected)
        state_json = json.dumps(result_to_dict(result))
        server_ini_text = request.form.get("server_ini_text", "") or ""
        updated_ini = ""
        if server_ini_text.strip():
            updates = {
                "WorkshopItems": ";".join(result.workshop_ids),
                "Mods": ";".join(result.selected_mod_ids),
            }
            updated_ini = apply_pzserver_ini_edits(server_ini_text, updates)
        return render_template_string(
            RESULT_HTML,
            result=result,
            state_json=state_json,
            updated_ini=updated_ini,
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

    @app.post("/download-zip")
    def download_zip_route():
        state = json.loads(request.form["state"])
        result = dict_to_result(state)
        data = zip_reports(result)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".zip")
        tmp.write(data)
        tmp.close()
        return send_file(tmp.name, as_attachment=True, download_name="pzmodsmith-output.zip")

    print(f"{APP_NAME} running at http://{host}:{port}")
    app.run(host=host, port=port, debug=False)
