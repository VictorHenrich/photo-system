from dotenv import load_dotenv
import logging

if __name__ == "__main__":
    load_dotenv()

    logging.basicConfig(level=logging.INFO)

    import controllers

    from server.instances import AppInstances

    AppInstances.api.start()
