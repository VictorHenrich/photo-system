from typing import Type, Any


class ServiceError(Exception):
    def __init__(self, service_class: Type[Any], *messages: str) -> None:
        error_message: str = (
            f"Failed to execute service class: {service_class.__name__}\n"
            + f"For the following errors: ".join(messages)
        )

        super().__init__(error_message)


class FileExtensionNotFoundError(Exception):
    def __init__(self, content_type: str) -> None:
        error_message: str = (
            f"Unable to find file extension by content-type: {content_type}"
        )

        super().__init__(error_message)


class FileTypeNotFoundError(Exception):
    def __init__(self, url: str) -> None:
        error_message: str = f"File type not found by url: {url}"

        super().__init__(error_message)
