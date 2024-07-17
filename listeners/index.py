from typing import Any

from server.instances import AppInstances
from utils.constants import PICTURE_RESIZING_TOPIC


@AppInstances.events.add_listener(PICTURE_RESIZING_TOPIC)
def resize_picture(message: Any) -> None:
    pass
