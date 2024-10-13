from llm_models.base import Base
from groq import Groq
import json
from pathlib import Path
class GroqModel(Base):
    def __init__(self,config_file="config/config.json"):
        # Load the API key from the config file
        config_path = Path(config_file)
        if config_path.is_file():
            with open(config_file, 'r') as f:
                config = json.load(f)
                api_key = config.get("groq_api_key")
                self.model_name = config.get("groq_model_name")

        self.client = Groq(api_key=api_key)

    def generate_answer(self,final_prompt):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": final_prompt,
                }
                ],
                model=self.model_name,
            )
        return chat_completion.choices[0].message.content