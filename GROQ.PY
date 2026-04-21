import os
import time
from dotenv import load_dotenv
from groq import Groq

load_dotenv()  # checks for the .env file in the folder
client = Groq(api_key=os.getenv("GROQ_API_KEY"))  #initialize the groq cloud serices

print("Ask the assistant to help with your problems...")
user_input = input("You: ")

#defines how the ai behvaes
completion = client.chat.completions.create(    
    model="groq/compound-mini",
    messages=[
      {
        "role": "system",
        "content": "You are an AI assistant."
      },
      {
        "role": "user",
        "content": user_input
      }
    ],
    temperature=1,   #creativity variety
    max_completion_tokens=1050, 
    top_p=1,
    stream=True,   #tells ai to send response piece by piece
    stop=None,
    compound_custom={"tools":{"enabled_tools":["web_search","code_interpreter","visit_website"]}}
)

for chunk in completion:   #grab every response that ai generates
    content = chunk.choices[0].delta.content or ""   # grabs the exact response from all raw data
    for char in content:
        print(char, end="", flush=True)
        time.sleep(0.02)