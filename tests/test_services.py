from unittest import TestCase
from unittest.mock import Mock
from pathlib import Path
from io import BytesIO

from services.file import FileService


class ServicesTestCase(TestCase):
    def test_rezise_picture_with_success(self) -> None:
        file_service: FileService = FileService()

        file_path: Path = Path.cwd() / "tests" / "assets" / "test.jpg"

        width: int = 1000

        height: int = 1000

        format: str = "jpeg"

        with open(file_path, mode="rb+") as file:
            picture: BytesIO = BytesIO(file.read())

            file.seek(0)

            resized_picture: BytesIO = file_service.resize_picture(
                picture=picture, height=height, width=width, format=format
            )

            file.writelines(resized_picture.readlines())

    def test_send_to_resize_picture_with_success(self) -> None:
        file_service: FileService = FileService()

        file_path: Path = Path.cwd() / "assets" / "test.jpg"

        width: int = 1000

        height: int = 1000

        with open(file_path, mode="rb+") as file:
            file_service.send_to_resize_picture(
                content=file.read(), filename=file.name, width=width, height=height
            )
