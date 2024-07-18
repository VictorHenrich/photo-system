from pydantic import BaseModel

from utils.constants import SWAGGER_API_VERSION


class IndexEntity(BaseModel):
    version: str = SWAGGER_API_VERSION
    name: str = "APPLICATION"
    description: str = "APLICATION RUNNING"


class ResizingEntity(BaseModel):
    filename: str

    content_base64: str

    width: int

    height: int
