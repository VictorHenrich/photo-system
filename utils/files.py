from typing import Optional, Sequence
import mimetypes

from utils.types import DictType
from utils.exceptions import FileExtensionNotFoundError, FileTypeNotFoundError


image_mimetypes: DictType[str] = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".gif": "image/gif",
    ".bmp": "image/bmp",
    ".tiff": "image/tiff",
    ".tif": "image/tiff",
    ".webp": "image/webp",
    ".ico": "image/vnd.microsoft.icon",
    ".svg": "image/svg+xml",
    ".heif": "image/heif",
    ".heic": "image/heic",
}


for extension, type in image_mimetypes.items():
    mimetypes.add_type(type, extension)


class FileUtils:
    @staticmethod
    def get_extension(content_type: str) -> str:
        extensions: Sequence[str] = mimetypes.guess_all_extensions(content_type)

        try:
            return extensions[0]

        except IndexError:
            raise FileExtensionNotFoundError(content_type)

    @staticmethod
    def get_content_type(url: str):
        types: Sequence[Optional[str]] = mimetypes.guess_type(url)

        try:
            type: Optional[str] = types[0]

        except IndexError:
            FileTypeNotFoundError(url)

        else:
            if type is None:
                FileTypeNotFoundError(url)

            return type
