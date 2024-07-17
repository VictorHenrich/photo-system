from fastapi import UploadFile

from server.instances import AppInstances
from utils.constants import INDEX_ENDPOINT_URL, RESIZE_PICTURE_ENDPOINT_URL
from utils.responses import JSONSuccessResponse
from utils.entities import IndexEntity


@AppInstances.api.get(INDEX_ENDPOINT_URL)
async def index() -> JSONSuccessResponse[IndexEntity]:
    body: IndexEntity = IndexEntity()

    return JSONSuccessResponse(content=body)


@AppInstances.api.post(RESIZE_PICTURE_ENDPOINT_URL)
async def resize_image(body: UploadFile) -> JSONSuccessResponse:
    return JSONSuccessResponse(content=None)
