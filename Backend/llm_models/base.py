import google.generativeai as genai
from abc import ABC,abstractmethod
class Base(ABC):
    def __init__(self, model_name: str):
        self.model_name = model_name
        pass
    def generate_answer(self):
        pass