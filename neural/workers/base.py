import abc

import numpy as np

from neural.label import Label


class NeuralWorker:
    @abc.abstractmethod
    def detect(self, image: np.ndarray) -> list[Label]:
        pass