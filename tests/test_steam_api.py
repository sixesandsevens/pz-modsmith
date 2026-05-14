import unittest
from unittest.mock import patch

from pz_modsmith.steam_api import expand_workshop_ids_with_required_items


class TestSteamApi(unittest.TestCase):
    def test_expands_required_items(self) -> None:
        fake_payload = {
            "response": {
                "publishedfiledetails": [
                    {"publishedfileid": "111", "children": [{"publishedfileid": "222"}]},
                    {"publishedfileid": "222", "children": [{"publishedfileid": "333"}]},
                    {"publishedfileid": "333", "children": []},
                ]
            }
        }

        def fake_post_form(url: str, data: dict[str, str], timeout_seconds: float = 10.0) -> dict:
            # Return details for whichever ids we asked for.
            requested = []
            for k, v in data.items():
                if k.startswith("publishedfileids["):
                    requested.append(v)
            details = [
                d
                for d in fake_payload["response"]["publishedfiledetails"]
                if d["publishedfileid"] in requested
            ]
            return {"response": {"publishedfiledetails": details}}

        with patch("pz_modsmith.steam_api._post_form", side_effect=fake_post_form):
            out = expand_workshop_ids_with_required_items(["111"], max_depth=3)
        self.assertEqual(out, ["111", "222", "333"])


if __name__ == "__main__":
    unittest.main()

