from Prompt.base import Prompt
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_message_histories import ChatMessageHistory

class ConversationPrompt(Prompt):
    def create_template(self):
        conversation_message =  ("placeholder", "{messages}")
        prompt = ChatPromptTemplate.from_messages([
            # system_messages,
            conversation_message
            ])
        return prompt

    def add_message_to_history(self,message,history,role="Choi"):
        if role =="David":
            history.add_user_message(message)
        if role =="Choi":
            history.add_ai_message(message)

        return history
            



        