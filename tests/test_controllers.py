from typing import Any
from unittest import TestCase
from fastapi.testclient import TestClient
from httpx import Response
import logging

from server.instances import AppInstances
from utils.constants import RESIZE_PICTURE_ENDPOINT_URL, ASSETS_PATH
from utils.types import DictType
from utils.files import FileUtils


class ControllersTestCase(TestCase):
    def setUp(self) -> None:
        self.__client: TestClient = TestClient(app=AppInstances.api)

    def test_resize_image(self) -> None:
        file_url: str = str(ASSETS_PATH / "test.jpg")

        width: str = "200"

        height: str = "200"

        with open(file_url, mode="rb") as file:
            params: DictType[str] = {"width": width, "height": height}

            files: DictType = {
                "body": (file.name, file, FileUtils.get_content_type(file_url))
            }

            response: Response = self.__client.post(
                RESIZE_PICTURE_ENDPOINT_URL, files=files, params=params
            )

            json_response: DictType[Any] = response.json()

            logging.info(f"Response Data: {json_response}")

            self.assertTrue(response.status_code, 200)

            self.assertDictEqual(json_response, {"content": None})

    def test_resize_image_with_error(self) -> None:

        response: Response = self.__client.post(RESIZE_PICTURE_ENDPOINT_URL, files={})

        json_response: DictType[Any] = response.json()

        logging.info(f"Response Data: {json_response}")

        self.assertTrue(response.status_code, 422)
