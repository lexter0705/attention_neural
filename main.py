import asyncio

from config import ConfigReader
from neural import YOLOWorker
from websocket import NeuralConnector

config_reader = ConfigReader()
config = config_reader.read()

worker = YOLOWorker(config["path_to_model"])
connector = NeuralConnector(config["server_url"], worker)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    task = loop.create_task(connector.connect())
    loop.run_until_complete(task)
