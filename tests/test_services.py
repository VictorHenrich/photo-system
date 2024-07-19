from unittest import TestCase
from unittest.mock import Mock, patch
from pathlib import Path
from io import BytesIO
from pydantic import ValidationError

from server.event import AppProducer
from services.file import FileService
from utils.constants import ASSETS_PATH, PICTURE_RESIZING_TOPIC
from utils.entities import ResizingEntity


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

    @patch("services.file.ResizingEntity", spec=ResizingEntity)
    @patch("services.file.AppProducer", spec=AppProducer)
    def test_send_to_resize_picture_with_success(
        self, app_producer_class: Mock, resizing_entity_class: Mock
    ) -> None:
        app_producer_instance: Mock = Mock()

        app_producer_instance.send.return_value = None

        resizing_entity_instance: Mock = Mock(width=100, height=100, filename="")

        resizing_entity_instance.model_dump_json.return_value = ""

        resizing_entity_class.return_value = resizing_entity_instance

        app_producer_class.return_value = app_producer_instance

        file_service: FileService = FileService()

        file_service.send_to_resize_picture(
            content=bytes(),
            filename=resizing_entity_instance.filename,
            width=resizing_entity_instance.width,
            height=resizing_entity_instance.height,
        )

        resizing_entity_class.assert_called()

        app_producer_class.assert_called()

        resizing_entity_instance.model_dump_json.assert_called_once()

        app_producer_instance.send.assert_called_once_with(
            PICTURE_RESIZING_TOPIC, bytes()
        )

    @patch("services.file.AppProducer", spec=AppProducer)
    def test_send_to_resize_picture_with_validation_error(self, _: Mock) -> None:
        wrong_object: Mock = Mock(
            content=bytes(), filename="", width="wrong_width", height="wrong_height"
        )

        file_service: FileService = FileService()

        with self.assertRaises(ValidationError):
            file_service.send_to_resize_picture(
                content=wrong_object.content,
                filename=wrong_object.filename,
                width=wrong_object.width,
                height=wrong_object.height,
            )

    @patch("services.file.AppProducer", spec=AppProducer)
    def test_send_to_resize_picture_with_type_error(self, _: Mock) -> None:
        wrong_object: Mock = Mock(content=object(), filename="")

        file_service: FileService = FileService()

        with self.assertRaises(TypeError):
            file_service.send_to_resize_picture(
                content=wrong_object.content,
                filename=wrong_object.filename,
                width=wrong_object.width,
                height=wrong_object.height,
            )
