import asyncio
import time

from config import ConfigReader
from neural import YOLOWorker
from websocket import NeuralConnector

config_reader = ConfigReader()
config = config_reader.read()

worker = YOLOWorker(config["path_to_model"])
connector = NeuralConnector(config["server_url"], worker)

def connect():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        task = loop.create_task(connector.connect())
        loop.run_until_complete(task)
    except Exception as e:
        print(e)
        time.sleep(100)
        connect()

if __name__ == "__main__":
    connect()
