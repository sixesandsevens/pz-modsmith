import json
import os
from glob import glob
import unittest


class TestSteamApiFixtureSchema(unittest.TestCase):
    def test_fixture_shape_get_published_file_details(self) -> None:
        fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures")
        paths = sorted(glob(os.path.join(fixtures_dir, "steam_GetPublishedFileDetails*.json")))
        if not paths:
            self.skipTest("no fixtures found: tests/fixtures/steam_GetPublishedFileDetails*.json")

        for fixture_path in paths:
            with self.subTest(fixture=os.path.basename(fixture_path)):
                with open(fixture_path, "r", encoding="utf-8") as f:
                    payload = json.load(f)

                self.assertIsInstance(payload, dict)
                self.assertIn("response", payload)
                self.assertIsInstance(payload["response"], dict)
                self.assertIn("publishedfiledetails", payload["response"])
                self.assertIsInstance(payload["response"]["publishedfiledetails"], list)

                details = payload["response"]["publishedfiledetails"]
                self.assertTrue(details, "fixture had empty publishedfiledetails")

                first = details[0]
                self.assertIsInstance(first, dict)
                self.assertIn("publishedfileid", first)

    def test_fixture_shape_get_collection_details(self) -> None:
        fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures")
        paths = sorted(glob(os.path.join(fixtures_dir, "steam_GetCollectionDetails*.json")))
        if not paths:
            self.skipTest("no fixtures found: tests/fixtures/steam_GetCollectionDetails*.json")

        for fixture_path in paths:
            with self.subTest(fixture=os.path.basename(fixture_path)):
                with open(fixture_path, "r", encoding="utf-8") as f:
                    payload = json.load(f)

                self.assertIsInstance(payload, dict)
                self.assertIn("response", payload)
                self.assertIsInstance(payload["response"], dict)
                self.assertIn("collectiondetails", payload["response"])
                self.assertIsInstance(payload["response"]["collectiondetails"], list)

                details = payload["response"]["collectiondetails"]
                self.assertTrue(details, "fixture had empty collectiondetails")

                first = details[0]
                self.assertIsInstance(first, dict)
                self.assertIn("publishedfileid", first)
                if int(first.get("result") or 0) == 1:
                    self.assertIn("children", first)
                    self.assertIsInstance(first["children"], list)


if __name__ == "__main__":
    unittest.main()
