from Prompt.base import Prompt
# Import necessary modules from LangChain
from langchain.prompts import ChatPromptTemplate
class Emotional_extract_prompt(Prompt):
    def create_template(self):
        system_prompt = """
        You are an expert in identifying emotional phrases in chat conversations. 
        Your task is to analyze the provided chat history and accurately extract emotions such as warmth, concern, frustration, or nostalgia."
        ## Constraint
        - Only response emotion
        - Do not include emoji 
        ## Chat conversation
        {history}
        """
        prompt_template = ChatPromptTemplate.from_template(system_prompt)
        return prompt_template