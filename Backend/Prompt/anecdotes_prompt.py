from Prompt.base import Prompt
# Import necessary modules from LangChain
from langchain.prompts import ChatPromptTemplate
# class Anecdotes_extract_prompt(Prompt):
#     def create_template(self):
#         system_prompt = """
#         "You are an expert in identifying personal stories and anecdotes in conversations. 
#         Your task is to analyze the following chat history and extract any anecdotes, 
#         which are personal stories or specific experiences shared by the participants. Please identify the anecdotes clearly and 
#         explain briefly why they qualify as anecdotes."
#         ## Chat conversation
#         {history}
#         """
#         prompt_template = ChatPromptTemplate.from_template(system_prompt)
#         return prompt_template
class Anecdotes_extract_prompt(Prompt):
    def create_template(self):
        system_prompt = """
        "You are an expert in identifying personal stories and anecdotes in conversations. 
        Your task is to analyze the chat history below and extract any anecdotes—personal stories or specific experiences shared by the participants. 
        For each anecdote, provide a clear identification and a brief explanation of why it qualifies as an anecdote."
        ## Chat conversation
        {history}
        """
        prompt_template = ChatPromptTemplate.from_template(system_prompt)
        return prompt_template
