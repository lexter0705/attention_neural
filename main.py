import asyncio

from config import ConfigReader
from neural import YOLOWorker
from websocket import ServerConnect

config_reader = ConfigReader()
config = config_reader.read()

worker = YOLOWorker(config["path_to_model"], config["classes"])
connector = ServerConnect(config["server_url"], worker)

if __name__ == "__main__":
    event_loop = asyncio.new_event_loop()
    task = asyncio.create_task(connector.connect())