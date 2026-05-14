import unittest

from pz_modsmith.server_ini import apply_pzserver_ini_edits
from pz_modsmith.sandbox_lua import apply_sandbox_vars_edits


class TestEditRoundtrip(unittest.TestCase):
    def test_ini_edit_preserves_comments(self) -> None:
        text = "# hi\nPVP=true\n\nMaxPlayers=32\n"
        out = apply_pzserver_ini_edits(text, {"PVP": "false", "MaxPlayers": "12"})
        self.assertIn("# hi", out)
        self.assertIn("PVP=false", out)
        self.assertIn("MaxPlayers=12", out)

    def test_sandbox_edit_updates_assignment(self) -> None:
        text = "SandboxVars = {\n  Zombies = 4,\n  ZombieMigrate = true,\n}\n"
        out = apply_sandbox_vars_edits(text, {"Zombies": "6", "ZombieMigrate": "false"})
        self.assertIn("Zombies = 6", out)
        self.assertIn("ZombieMigrate = false", out)


if __name__ == "__main__":
    unittest.main()

