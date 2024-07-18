from unittest import TestCase
import logging

from utils.files import FileUtils


class UtilsTestCase(TestCase):
    def test_get_content_type(self) -> None:
        content_type = FileUtils.get_content_type(
            "C:\\\\projetos\\\\photo-system\\\\assets\\\\test.jpg"
        )

        logging.info(f"Content Type: {content_type}")

        self.assertEqual(content_type, "image/jpeg")

    def test_get_extension(self) -> None:
        content_type: str = "image/jpeg"

        extension: str = FileUtils.get_extension(content_type)

        logging.info(f"Extension: {extension}")

        self.assertEqual(extension, "jpg")
