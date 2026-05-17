import unittest

from pz_modsmith.server_ini import parse_pzserver_ini, apply_pzserver_ini_edits, get_first_ini_value
from pz_modsmith.sandbox_lua import parse_sandbox_vars_lua


class TestServerIni(unittest.TestCase):
    def test_parses_comment_block_and_min_max_default(self) -> None:
        text = "\n".join(
            [
                "# Maximum number of players that can be on the server at one time.",
                "# Min: 1 Max: 100 Default: 32",
                "MaxPlayers=32",
            ]
        )
        settings = parse_pzserver_ini(text)
        self.assertEqual(len(settings), 1)
        s = settings[0]
        self.assertEqual(s.key, "MaxPlayers")
        self.assertEqual(s.value, "32")
        self.assertEqual(s.value_type, "int")
        self.assertEqual(s.min_value, 1)
        self.assertEqual(s.max_value, 100)
        self.assertEqual(s.default, "32")
        self.assertTrue(any("Maximum number of players" in c for c in s.comments))

    def test_sandbox_default_maps_to_option_number(self) -> None:
        text = "\n".join(
            [
                "SandboxVars = {",
                "  -- Default = July",
                "  -- 1 = January",
                "  -- 7 = July",
                "  StartMonth = 7,",
                "}",
            ]
        )
        settings = parse_sandbox_vars_lua(text)
        self.assertEqual(len(settings), 1)
        s = settings[0]
        self.assertEqual(s.default_raw, "July")
        self.assertEqual(s.default_value_raw, "7")

    def test_get_first_ini_value(self) -> None:
        text = "# c\nMods=A;B\nMods=C\n"
        self.assertEqual(get_first_ini_value(text, "Mods"), "A;B")

    def test_apply_appends_missing_keys(self) -> None:
        text = "PVP=true\n"
        out = apply_pzserver_ini_edits(text, {"WorkshopItems": "1;2", "Mods": "A;B"})
        self.assertIn("WorkshopItems=1;2", out)
        self.assertIn("Mods=A;B", out)


if __name__ == "__main__":
    unittest.main()
