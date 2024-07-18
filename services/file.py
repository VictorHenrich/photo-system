from PIL import Image, ImageFile
from io import BytesIO
from base64 import b64encode
from pathlib import Path

from server.event import AppProducer
from utils.constants import PICTURE_RESIZING_TOPIC, ASSETS_PATH
from utils.entities import ResizingEntity


class FileService:
    def resize_picture(
        self, picture: BytesIO, format: str, width: int, height: int
    ) -> BytesIO:
        picture_data: ImageFile.ImageFile = Image.open(picture, formats=[format])

        resized_picture: Image.Image = picture_data.resize((width, height))

        picture_io: BytesIO = BytesIO()

        resized_picture.save(picture_io, format=format)

        picture_io.seek(0)

        return picture_io

    def save_picture(self, picture: BytesIO, path: Path) -> None:
        with open(path, mode="wb") as file:
            file.writelines(picture.readlines())

    def send_to_resize_picture(
        self, content: bytes, filename: str, width: int, height: int
    ) -> None:
        producer: AppProducer = AppProducer()

        content_b64: str = b64encode(content).decode("utf-8")

        data: ResizingEntity = ResizingEntity(
            filename=filename, content_base64=content_b64, width=width, height=height
        )

        producer.send(PICTURE_RESIZING_TOPIC, data.model_dump_json().encode("utf-8"))
