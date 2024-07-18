from PIL import Image, ImageFile
from io import BytesIO


class FileService:
    def resize_picture(self, picture: BytesIO, width: int, height: int) -> BytesIO:
        picture_data: ImageFile.ImageFile = Image.open(picture)

        resized_picture: Image.Image = picture_data.resize((width, height))

        picture_io: BytesIO = BytesIO()

        resized_picture.save(picture_io)

        return picture_io

    def send_to_resize_picture(
        self, filecontent: bytes, filename: str, width: int, height: int
    ) -> None:
        pass
