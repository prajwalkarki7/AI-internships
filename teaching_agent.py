import os
from dotenv import load_dotenv
from groq import Groq
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import create_engine, Column, Integer, String

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 1. Updated Table Schema to hold both sides
class Base(DeclarativeBase):
    pass

class UserQuery(Base):
    __tablename__ = 'user_queries'
    id = Column(Integer, primary_key=True)
    user_question = Column(String)  # Your input
    ai_answer = Column(String)      # The full AI response

engine = create_engine("sqlite:///teaching.db")
Base.metadata.create_all(engine)
session = Session(engine)

while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the teaching assistant. Goodbye!")
        break

    completion = client.chat.completions.create(
        model="groq/compound",
        messages=[
            {"role": "system", "content": "You are a Nepali Teaching Assistant..."},
            {"role": "user", "content": user_input},
        ],
        stream=True,
    )

    full_response = ""
    
    # 2. Accumulate the response in 'full_response'
    for chunk in completion:
        content = chunk.choices[0].delta.content or ""
        print(content, end="", flush=True)
        full_response += content

    # 3. SAVE THE WHOLE CONVERSATION TURN (Outside the chunk loop)
    if full_response:
        new_entry = UserQuery(
            user_question=user_input, 
            ai_answer=full_response
        )
        session.add(new_entry)
        session.commit() # This saves one single row with both texts