import io
import json

import numpy as np
from PIL import Image

from neural.workers.base import NeuralWorker
from websocket.base import WebsocketConnect


class ServerConnect(WebsocketConnect):
    def __init__(self, link: str, worker: NeuralWorker):
        super().__init__(link)
        self.__worker = worker

    async def on_message(self, message: str):
        data = json.loads(message)
        image = Image.open(io.BytesIO(data["image"]))
        image_array = np.array(image)
        boxes = self.__worker.detect(image_array)
        array_for_send = []
        for box in boxes:
            array_for_send.append({"id": data["id"], "x1": box.xyxy[0], "y1": box.xyxy[1],
                                   "x2": box.xyxy[2], "y2": box.xyxy[3], "name": box.label_name})
        await self.websocket.send(json.dumps(array_for_send))
