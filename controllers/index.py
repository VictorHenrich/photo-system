from typing import Union
from fastapi import UploadFile

from server.instances import AppInstances
from utils.constants import (
    INDEX_ENDPOINT_URL,
    RESIZE_PICTURE_ENDPOINT_URL,
    DEFAULT_PICTURE_HEIGHT_SIZE,
    DEFAULT_PICTURE_WIDTH_SIZE,
)
from utils.responses import JSONSuccessResponse, JSONErrorResponse
from utils.entities import IndexEntity
from utils.exceptions import ServiceError
from services.file import FileService


@AppInstances.api.get(INDEX_ENDPOINT_URL)
async def index() -> JSONSuccessResponse[IndexEntity]:
    body: IndexEntity = IndexEntity()

    return JSONSuccessResponse(content=body)


@AppInstances.api.post(RESIZE_PICTURE_ENDPOINT_URL)
async def resize_image(
    body: UploadFile,
    width: str = DEFAULT_PICTURE_WIDTH_SIZE,
    height: str = DEFAULT_PICTURE_HEIGHT_SIZE,
) -> Union[JSONSuccessResponse, JSONErrorResponse]:
    file_service: FileService = FileService()

    content: bytes = await body.read()

    filename: str = body.filename or ""

    try:
        file_service.send_to_resize_picture(
            content=content, filename=filename, width=int(width), height=int(height)
        )

    except ServiceError as error:
        return JSONErrorResponse(detail=str(error))

    return JSONSuccessResponse(content=None)
