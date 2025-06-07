import numpy as np

from ultralytics import YOLO
import torch

from neural.label import Label
from neural.workers.base import NeuralWorker


class YOLOWorker(NeuralWorker):
    def __init__(self, model_path: str):
        self.__model = YOLO(model_path)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.__model.to(device)

    def detect(self, image: np.ndarray) -> list[Label]:
        predict = self.__model.predict(source=image)
        labels = [Label(self.__model.names[box.cls.tolist()[0]], box.xyxy.tolist()[0], box.conf.tolist()[0]) for box in predict[0].boxes]
        return labels