import os
import time
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("Ask the assistant to help with your problems...")
user_input = input("You: ")

completion = client.chat.completions.create(
    model="groq/compound-mini",
    messages=[
      {
        "role": "system",
        "content": "You are a concise consultant. Provide direct, brief answers. Avoid introductions, conclusions, or filler text. Give only the most necessary details."
      },
      {
        "role": "user",
        "content": user_input
      }
    ],
    temperature=1,
    max_completion_tokens=800,
    top_p=1,
    stream=True,
    stop=None,
    compound_custom={"tools":{"enabled_tools":["web_search","code_interpreter","visit_website"]}}
)

for chunk in completion:
    content = chunk.choices[0].delta.content or ""
    for char in content:
        print(char, end="", flush=True)
        time.sleep(0.02)