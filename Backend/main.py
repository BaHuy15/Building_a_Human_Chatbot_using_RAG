from Prompt.conversation_prompt import ConversationPrompt
from langchain_community.chat_message_histories import ChatMessageHistory
from llm_models.genai_model import Gemini_model
from llm_models.groq_model import GroqModel

from Prompt.base import system_messages
from Prompt.emotion_prompt import Emotional_extract_prompt
from Prompt.anecdotes_prompt import Anecdotes_extract_prompt
from Prompt.topic_prompt import Topic_extract_prompt  # Assuming you have a module for Topic extraction
from utils import extract_emotion_label
import re



# Initialize prompts
prompt_modules = ConversationPrompt()
emotional_prompt = Emotional_extract_prompt().create_template()
anecdotes_prompt = Anecdotes_extract_prompt().create_template()
topic_prompt = Topic_extract_prompt().create_template()  # Assuming a similar structure for topic
prompt = prompt_modules.create_template()
# Initialize the model and history
model = GroqModel() #Gemini_model()
history = ChatMessageHistory()

    
user_input = ""
while user_input != 'q':
    user_input = input('\n(type exit! to quit) Ask Choi > ')
    if user_input != 'exit!':
        user_messages = system_messages + user_input
        print("this is user messages: ",user_messages)
        prompt_modules.add_message_to_history(user_input, history, role="David")
        
        # Generate answer
        answer = model.generate_answer(user_messages)
        prompt_modules.add_message_to_history(answer, history, role="Choi")
        print('Here is answer',answer)
        
    if user_input == "q":
        # Extract Emotion
        emotional_prompts = emotional_prompt.format(history=str(history))
        emotion_extraction = model.generate_answer(emotional_prompts)

        
        # Extract Anecdote
        anecdotes_prompts = anecdotes_prompt.format(history=str(history))
        anecdotes_extraction = model.generate_answer(anecdotes_prompts)

        # Extract Topic
        topic_prompts = topic_prompt.format(history=str(history))
        topic_extraction = model.generate_answer(topic_prompts)

        # Store results in a DataFrame or use as needed
        extracted_data = {
            "Topic": topic_extraction,
            "Emotion": emotion_extraction,
            "Anecdote": anecdotes_extraction,
            "history":history,
        }
        
        
        # For example, print out or append to a list
        print("\nExtracted data:", extracted_data)
