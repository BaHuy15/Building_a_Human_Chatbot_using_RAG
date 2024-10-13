from Prompt.base import Prompt
# Import necessary modules from LangChain
from langchain.prompts import ChatPromptTemplate

class Topic_extract_prompt(Prompt):
    def create_template(self):
        system_prompt = """
        You are an expert in analyzing chat conversations to identify the main topics discussed. 
        Your task is to analyze the provided chat history and accurately extract the central topic or theme.
        
        ## Constraints
        - Only respond with the main topic or theme and a brief supporting explanation or example phrase if relevant.
        - Do not include any additional commentary or emojis.
        
        ## Chat conversation
        {history}
        """
        prompt_template = ChatPromptTemplate.from_template(system_prompt)
        return prompt_template