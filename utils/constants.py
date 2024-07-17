import os


BROKER_KAFKA_URL: str = os.environ.get("BROKER_KAFKA_URL", "localhost:9092")

API_HOST: str = os.environ.get("API_HOST", "localhost")

API_PORT: int = int(os.environ.get("API_PORT", "5000"))

INDEX_ENDPOINT_URL: str = os.environ.get("INDEX_URL", "/")

RESIZE_PICTURE_ENDPOINT_URL: str = os.environ.get("RESIZE_URL", "")

PICTURE_RESIZING_TOPIC: str = os.environ.get("PICTURE_RESIZING_TOPIC", "")

SWAGGER_API_VERSION: str = os.environ.get("SWAGGER_API_VERSION", "1.0.0")
