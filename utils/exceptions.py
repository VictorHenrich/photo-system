from typing import Type, Any


class ServiceError(Exception):
    def __init__(self, service_class: Type[Any], *messages: str) -> None:
        error_message: str = (
            f"Failed to execute service class: {service_class.__name__}\n"
            + f"For the following errors: ".join(messages)
        )

        super().__init__(error_message)
