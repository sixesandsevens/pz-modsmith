import unittest

from pz_modsmith.models import ModInfo
from pz_modsmith.scanner import collapse_to_highest_version


class TestCollapseVersions(unittest.TestCase):
    def test_keeps_highest_version_per_mod_id(self) -> None:
        mods = [
            ModInfo(
                workshop_id="1",
                mod_id="TombGothHair",
                name="Hair",
                path="/ws/1/mods/Tomb's Goth Hair/42.0/mod.info",
                score=0,
                notes=[],
            ),
            ModInfo(
                workshop_id="1",
                mod_id="TombGothHair",
                name="Hair",
                path="/ws/1/mods/Tomb's Goth Hair/42.15/mod.info",
                score=0,
                notes=[],
            ),
        ]
        out = collapse_to_highest_version(mods)
        self.assertEqual(len(out), 1)
        self.assertIn("42.15", out[0].path)


if __name__ == "__main__":
    unittest.main()

