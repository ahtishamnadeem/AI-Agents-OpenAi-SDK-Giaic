import os
import chainlit as cl
from dotenv import load_dotenv
import google.generativeai as genai
from agents import Agent, Runner, function_tool

# -------------------- Load ENV --------------------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# -------------------- Gemini Model --------------------
model = genai.GenerativeModel("gemini-1.5-flash")

# -------------------- Tools --------------------
@function_tool
def answer_question(query: str) -> str:
    """Answer academic questions as a helpful tutor."""
    response = model.generate_content(query)
    return response.text

@function_tool
def study_tips(topic: str) -> str:
    """Provide effective study tips for a given topic."""
    response = model.generate_content(f"Give 5 effective study tips for {topic}.")
    return response.text

@function_tool
def summarize_text(passage: str) -> str:
    """Summarize a given text in 3-4 lines."""
    response = model.generate_content(f"Summarize the following text in 3-4 lines:\n\n{passage}")
    return response.text

# -------------------- Agent --------------------
student_agent = Agent(
    name="Smart Student Assistant",
    instructions="Helps students with academic questions, study tips, and summaries.",
    tools=[answer_question, study_tips, summarize_text],
)

# -------------------- Chainlit Handlers --------------------
@cl.on_chat_start
async def start_chat():
    await cl.Message(
        content=(
            "# 🎓 Smart Student Assistant\n\n"
            "Welcome! I can:\n"
            "- 📘 Answer academic questions\n"
            "- 📝 Provide study tips\n"
            "- ✨ Summarize text\n\n"
            "Type your query below 👇"
        )
    ).send()

@cl.on_message
async def handle_message(message: cl.Message):
    query = message.content
    result = Runner.run_sync(student_agent, query)
    await cl.Message(content=result.final_output).send()
