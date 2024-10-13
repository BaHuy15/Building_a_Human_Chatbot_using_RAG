from llm_models.base import Base
import google.generativeai as genai
from pathlib import Path
import json 
class Gemini_model(Base):
    def __init__(self,config_file="config/config.json"):
        # Load the API key from the config file
        config_path = Path(config_file)
        if config_path.is_file():
            with open(config_file, 'r') as f:
                config = json.load(f)
                api_key = config.get("gemini_api_key")
                model_name = config.get("gemini_model_name")
        else:
            raise FileNotFoundError(f"Config file '{config_file}' not found.")
        self.model = genai.GenerativeModel(model_name)
        # Initialize the API with your API key
        genai.configure(api_key=api_key)
    def generate_answer(self,input_text):
        # Call the model using the GenAI API
        response = self.model.generate_content(input_text).text
        return response

