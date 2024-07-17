from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    import controllers

    from server.instances import AppInstances

    AppInstances.api.start()
