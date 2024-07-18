from unittest import TestCase
from pathlib import Path
from io import BytesIO

from services.file import FileService
from utils.constants import ASSETS_PATH


class ServicesTestCase(TestCase):
    def test_rezise_picture(self) -> None:
        file_service: FileService = FileService()

        file_path: Path = ASSETS_PATH / "test.jpg"

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

    def test_rezise_picture_with_invalid_file_type(self) -> None:
        file_service: FileService = FileService()

        width: int = 1000

        height: int = 1000

        format: str = "pdf"

        with self.assertRaises(KeyError):
            file_service.resize_picture(
                picture=BytesIO(), height=height, width=width, format=format
            )

    def test_rezise_picture_with_size_value_error(self) -> None:
        file_service: FileService = FileService()

        file_path: Path = ASSETS_PATH / "test.jpg"

        width: int = 0

        height: int = 0

        format: str = "jpeg"

        with open(file_path, mode="rb+") as file:
            picture: BytesIO = BytesIO(file.read())

            file.seek(0)

            with self.assertRaises(ValueError):
                file_service.resize_picture(
                    picture=picture, height=height, width=width, format=format
                )

    def test_send_to_resize_picture_with_success(self) -> None:
        file_service: FileService = FileService()

        file_path: Path = ASSETS_PATH / "test.jpg"

        width: int = 100

        height: int = 100

        with open(file_path, mode="rb+") as file:
            file_service.send_to_resize_picture(
                content=file.read(), filename=file.name, width=width, height=height
            )
