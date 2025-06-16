import asyncio
import io
import json
import base64

import numpy as np
from PIL import Image

from neural.workers.base import NeuralWorker
from websocket.base import WebsocketConnector


class NeuralConnector(WebsocketConnector):
    def __init__(self, link: str, worker: NeuralWorker, reconnect_time: int = 1000):
        super().__init__(link)
        self.__worker = worker
        self.__reconnect_time = reconnect_time

    async def on_message(self, message: str):
        if message == "is_connected":
            return
        data = json.loads(message)
        image_data = base64.b64decode(data["image"])
        image = Image.open(io.BytesIO(image_data))
        image_array = np.array(image)
        boxes = self.__worker.detect(image_array)
        array_for_send = []
        for box in boxes:
            array_for_send.append({"x1": round(box.xyxy[0]), "y1": round(box.xyxy[1]),
                                   "x2": round(box.xyxy[2]), "y2": round(box.xyxy[3]), "name": box.label_name})
        await self.websocket.send(json.dumps({"id": data["id"], "boxes": array_for_send}))