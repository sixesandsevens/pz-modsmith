import unittest
from unittest.mock import patch

from pz_modsmith.steam_api import (
    expand_collection_ids,
    expand_workshop_ids_with_collections_and_required_items,
    expand_workshop_ids_with_required_items,
)


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

    def test_expands_collections(self) -> None:
        def fake_post_form(url: str, data: dict[str, str], timeout_seconds: float = 10.0) -> dict:
            if "GetCollectionDetails" not in url:
                raise AssertionError(f"unexpected endpoint: {url}")

            requested = []
            for k, v in data.items():
                if k.startswith("publishedfileids["):
                    requested.append(v)

            collectiondetails = []
            for cid in requested:
                if cid == "999":  # treat 999 as a collection with two members
                    collectiondetails.append(
                        {
                            "publishedfileid": "999",
                            "result": 1,
                            "children": [{"publishedfileid": "111"}, {"publishedfileid": "222"}],
                        }
                    )
                else:
                    collectiondetails.append({"publishedfileid": cid, "result": 9, "children": []})

            return {"response": {"collectiondetails": collectiondetails}}

        with patch("pz_modsmith.steam_api._post_form", side_effect=fake_post_form):
            out = expand_collection_ids(["999", "123"])
        self.assertEqual(out, ["111", "222", "123"])

    def test_expands_collections_then_required_items(self) -> None:
        def fake_post_form(url: str, data: dict[str, str], timeout_seconds: float = 10.0) -> dict:
            if "GetCollectionDetails" in url:
                requested = [v for k, v in data.items() if k.startswith("publishedfileids[")]
                return {
                    "response": {
                        "collectiondetails": [
                            {
                                "publishedfileid": requested[0],
                                "result": 1,
                                "children": [{"publishedfileid": "111"}],
                            }
                        ]
                    }
                }

            if "GetPublishedFileDetails" in url:
                requested = [v for k, v in data.items() if k.startswith("publishedfileids[")]
                # 111 requires 222
                details = []
                for wid in requested:
                    if wid == "111":
                        details.append({"publishedfileid": "111", "children": [{"publishedfileid": "222"}]})
                    elif wid == "222":
                        details.append({"publishedfileid": "222", "children": []})
                return {"response": {"publishedfiledetails": details}}

            raise AssertionError(f"unexpected endpoint: {url}")

        with patch("pz_modsmith.steam_api._post_form", side_effect=fake_post_form):
            out = expand_workshop_ids_with_collections_and_required_items(["999"], max_depth=2)
        self.assertEqual(out, ["111", "222"])

    def test_required_items_uses_published_file_service_when_api_key_provided(self) -> None:
        calls: list[str] = []

        def fake_get_details(ids: list[str], *, api_key: str, include_children: bool, timeout_seconds: float = 10.0) -> list[dict]:
            calls.append(api_key)
            # 111 requires 222; 222 requires none
            out = []
            for wid in ids:
                if wid == "111":
                    out.append({"publishedfileid": "111", "children": [{"publishedfileid": "222"}]})
                elif wid == "222":
                    out.append({"publishedfileid": "222", "children": []})
            return out

        with patch("pz_modsmith.steam_api.get_published_file_service_details", side_effect=fake_get_details):
            out = expand_workshop_ids_with_required_items(["111"], max_depth=2, api_key="KEY123")

        self.assertEqual(out, ["111", "222"])
        self.assertTrue(calls)
        self.assertTrue(all(c == "KEY123" for c in calls))


if __name__ == "__main__":
    unittest.main()
