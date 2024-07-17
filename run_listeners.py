from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    import listeners

    from server.instances import AppInstances

    AppInstances.events.run_consumers()
