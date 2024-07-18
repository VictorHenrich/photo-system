from fastapi import UploadFile, File

from server.instances import AppInstances
from utils.constants import INDEX_ENDPOINT_URL, RESIZE_PICTURE_ENDPOINT_URL
from utils.responses import JSONSuccessResponse
from utils.entities import IndexEntity
from services.file import FileService


@AppInstances.api.get(INDEX_ENDPOINT_URL)
async def index() -> JSONSuccessResponse[IndexEntity]:
    body: IndexEntity = IndexEntity()

    return JSONSuccessResponse(content=body)


@AppInstances.api.post(RESIZE_PICTURE_ENDPOINT_URL)
async def resize_image(
    body: UploadFile = File(), width: str = "300", height: str = "300"
) -> JSONSuccessResponse:
    file_service: FileService = FileService()

    content: bytes = await body.read()

    filename: str = body.filename or ""

    file_service.send_to_resize_picture(
        content=content, filename=filename, width=int(width), height=int(height)
    )

    return JSONSuccessResponse(content=None)
