import json


class ConfigReader:
    def __init__(self, path_to_file: str = "config/config.json"):
        self.__path_to_file = path_to_file

    def read(self) -> dict:
        with open(self.__path_to_file, "r") as f:
            return json.loads(f.read())