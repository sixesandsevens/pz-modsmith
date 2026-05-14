import unittest

from pz_modsmith.log_parser import extract_workshop_ids_from_free_text


class TestLogParser(unittest.TestCase):
    def test_free_text_id_list(self) -> None:
        text = "1234567890; 2345678901\n"
        self.assertEqual(extract_workshop_ids_from_free_text(text), ["1234567890", "2345678901"])

    def test_free_text_workshopitems_line(self) -> None:
        text = "WorkshopItems=1234567890;2345678901\n"
        self.assertEqual(extract_workshop_ids_from_free_text(text), ["1234567890", "2345678901"])

    def test_console_log_does_not_grab_random_numbers(self) -> None:
        text = "\n".join(
            [
                "LOG  : General     , 1234567890, some message",
                "LOG  : General     , workshop path /home/me/.local/share/Steam/steamapps/workshop/content/108600",
                "LOG  : General     , port 16261",
            ]
        )
        self.assertEqual(extract_workshop_ids_from_free_text(text), [])


if __name__ == '__main__':
    unittest.main()

