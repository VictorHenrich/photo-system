from server.api import Api

from server.event import AppEvents
from utils.constants import (
    API_HOST,
    API_PORT,
    SWAGGER_API_VERSION,
    SWAGGER_API_TITLE,
    SWAGGER_API_DESCRIPTION,
)


class AppInstances:
    api: Api = Api(
        host=API_HOST,
        port=API_PORT,
        title=SWAGGER_API_TITLE,
        description=SWAGGER_API_DESCRIPTION,
        version=SWAGGER_API_VERSION,
    )

    events: AppEvents = AppEvents()
