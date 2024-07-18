from unittest import TestCase
from unittest.mock import Mock
from pathlib import Path
from io import BytesIO

from services.file import FileService


class ServicesTestCase(TestCase):
    def test_rezise_picture_with_success(self) -> None:
        file_service: FileService = FileService()

        file_path: Path = Path.cwd() / "tests" / "assets" / "test.png"

        width: int = 500

        height: int = 500

        with open(file_path, mode="rb+") as file:
            picture: BytesIO = BytesIO(file.read())

            resized_picture: BytesIO = file_service.resize_picture(
                picture=picture, height=height, width=width
            )

            file.write(resized_picture.read())
