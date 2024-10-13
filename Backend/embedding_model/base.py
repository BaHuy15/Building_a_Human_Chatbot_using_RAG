from abc import ABC,abstractmethod

class Base(ABC):
    def __init__(self, key, model_name):
        pass

    def encode(self, texts):
        pass

    def encode_queries(self, text: str):
        pass