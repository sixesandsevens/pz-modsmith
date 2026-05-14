import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from pz_modsmith.analysis import analyze


class TestInferWorkshopIds(unittest.TestCase):
    def test_infers_workshop_ids_from_active_mod_ids(self) -> None:
        with TemporaryDirectory() as tmp:
            workshop_path = Path(tmp)

            item_a = workshop_path / "1111111111"
            item_a.mkdir(parents=True)
            (item_a / "mod.info").write_text("id=FooMod\nname=Foo\n", encoding="utf-8")

            item_b = workshop_path / "2222222222"
            item_b.mkdir(parents=True)
            (item_b / "mod.info").write_text("id=BarMod\nname=Bar\n", encoding="utf-8")

            result = analyze([], workshop_path, active_mod_ids=["FooMod"], console_text="LOG : Mod > loading FooMod")
            self.assertEqual(result.workshop_ids, ["1111111111"])
            self.assertEqual(result.missing_ids, [])


if __name__ == '__main__':
    unittest.main()

