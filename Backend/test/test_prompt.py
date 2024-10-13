from Prompt.conversation_prompt import ConversationPrompt
from langchain_community.chat_message_histories import ChatMessageHistory
from llm_models.genai_model import Gemini_model
from Prompt.emotion_prompt import Emotional_extract_prompt
from Prompt.anecdotes_prompt import Anecdotes_extract_prompt
from Prompt.topic_prompt import Topic_extract_prompt  # Assuming you have a module for Topic extraction
import re
system_messages = """
Your name is Choi, and you're from Korea. Your 58-year-old father, David, is being treated for Alzheimer's disease at Seoul Hospital. 
You have extensive experience diagnosing, treating, and researching Alzheimer's, with a deep understanding of its symptoms, progression, and latest treatments. 
Additionally, you're involved in "Digital Cure," a project using AI to create treatment programs for Alzheimer's patients, reducing the need for frequent doctor visits.

Respond to your father's questions in a friendly and cheerful manner, like a family member.

You will also play one of the following roles:

A/Stand-up Comedian: Create humorous routines on topics I provide, like current events. Incorporate personal anecdotes to make the jokes relatable. 
Your first task is to give a funny take on politics.

B/Motivational Speaker: Deliver speeches that inspire action and empower people to achieve their goals. 
Your first task is to create a speech about never giving up
Let's follow my instruction step by step:
1.Detection and Translation 
Detect language of question
## Constrains 
+ If the question is in English, respond in English. 
+ If in Korean, reply in respectful Korean.
+ Do not generate emoji icon
You can switch between languages and translate as needed. 
Keep your responses brief, maintaining a natural conversational tone.
2. Response to user question
Response brief answer
"""

# Initialize prompts
prompt_modules = ConversationPrompt()
emotional_prompt = Emotional_extract_prompt().create_template()
anecdotes_prompt = Anecdotes_extract_prompt().create_template()
topic_prompt = Topic_extract_prompt().create_template()  # Assuming a similar structure for topic

# Initialize the model and history
model = Gemini_model()
history = ChatMessageHistory()
prompt = prompt_modules.create_template()

# Function to extract the emotion label
def extract_emotion_label(emotion_text):
    # Use regular expression to match the emotion label format **Emotion:**
    match = re.search(r'\*\*(\w+):\*\*', emotion_text)
    if match:
        return match.group(1)  # Return the emotion label without asterisks
    else:
        return "No emotion label found"
    
user_input = ""
while user_input != 'q':
    user_input = input('\n(type exit! to quit) Ask Choi > ')
    if user_input != 'exit!':
        user_messages = system_messages + user_input
        prompt_modules.add_message_to_history(user_input, history, role="David")
        
        # Generate answer
        answer = model.generate_answer(user_messages)
        prompt_modules.add_message_to_history(answer, history, role="Choi")
        print('Here is answer',answer)
        
    if user_input == "q":
        # Extract Emotion
        emotional_prompts = emotional_prompt.format(history=str(history))
        emotion_extraction = model.generate_answer(emotional_prompts)
        emotion_extraction=extract_emotion_label(emotion_extraction)
        # print("Extracted Emotion from history:", emotion_extraction)
        
        # Extract Anecdote
        anecdotes_prompts = anecdotes_prompt.format(history=str(history))
        anecdotes_extraction = model.generate_answer(anecdotes_prompts)
        # print("Extracted Anecdotes from history:", anecdotes_extraction)

        # Extract Topic
        topic_prompts = topic_prompt.format(history=str(history))
        topic_extraction = model.generate_answer(topic_prompts)
        # print("Extracted Topic from history:", topic_extraction)

        # Store results in a DataFrame or use as needed
        extracted_data = {
            "Topic": topic_extraction,
            "Emotion": emotion_extraction,
            "Anecdote": anecdotes_extraction
        }
        
        
        
        # For example, print out or append to a list
        print("\nExtracted data:", extracted_data)
