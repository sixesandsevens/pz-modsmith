## Steam API fixtures

This folder is for capturing **real** Steam Web API responses (JSON) so we can
lock down the *exact* response shape we see in practice.

### Capture `GetPublishedFileDetails`

Run this on a machine with internet access (outside this sandbox) and save the
output as `tests/fixtures/steam_GetPublishedFileDetails.json`:

```bash
curl -sS -X POST \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "itemcount=1" \
  --data-urlencode "publishedfileids[0]=WORKSHOP_ID" \
  --data-urlencode "return_children=true" \
  "https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/" \
  > tests/fixtures/steam_GetPublishedFileDetails.json
```

Replace `WORKSHOP_ID` with a real Workshop item id (a mod or a collection).

Notes:
- Don’t leave a space after a line-ending `\` (it breaks line continuation).
- If you’re capturing multiple examples, prefer naming by id, e.g.
  `tests/fixtures/steam_GetPublishedFileDetails_3714934241.json`.

### Inspect locally

Once the JSON is saved, you can inspect it with:

```bash
python -m pz_modsmith.inspect_steam_fixture tests/fixtures/steam_GetPublishedFileDetails.json
```
