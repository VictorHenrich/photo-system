from server.api import Api

from server.event import AppEvents
from utils.constants import API_HOST, API_PORT


class AppInstances:
    api: Api = Api(host=API_HOST, port=API_PORT)

    events: AppEvents = AppEvents()
