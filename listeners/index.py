from typing import Any
from base64 import b64decode
from io import BytesIO
from pathlib import Path
import logging
import json

from server.instances import AppInstances
from services.file import FileService
from utils.constants import PICTURE_RESIZING_TOPIC, ASSETS_PATH
from utils.types import DictType
from utils.files import FileUtils


@AppInstances.events.add_listener(PICTURE_RESIZING_TOPIC)
def resize_picture(message: Any) -> None:
    logging.info(f"Data Received in {PICTURE_RESIZING_TOPIC}: {message}")

    file_service: FileService = FileService()

    body: DictType[Any] = json.loads(message.value)

    file_content: BytesIO = BytesIO(b64decode(body["content_base64"]))

    filename: str = body["filename"]

    width: int = body["width"]

    height: int = body["height"]

    format: str = FileUtils.get_extension(filename)

    picture: BytesIO = file_service.resize_picture(
        picture=file_content, format=format, width=width, height=height
    )

    file_path: Path = ASSETS_PATH / filename

    file_service.save_picture(picture, file_path)
