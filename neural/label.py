class Label:
    def __init__(self, class_name: str, xyxy: list[int], confidence: float):
        self.__label_name = class_name
        self.__xyxy = xyxy
        self.__confidence = confidence

    @property
    def confidence(self):
        return self.__confidence

    @property
    def label_name(self):
        return self.__label_name

    @property
    def xyxy(self):
        return self.__xyxy.copy()