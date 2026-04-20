from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

def get_advice(name, goal):
    prompt = f"""
    You are a career advisor.

    User Name: {name}
    Goal: {goal}

    Give short and clear career advice.
    """

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text


def save_history(user_input, response):
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f"INPUT: {user_input}\n")
        f.write(f"OUTPUT: {response}\n")
        f.write("-" * 40 + "\n")


def get_skills(goal):
    prompt = f"""
    List the key skills required to become a {goal}.
    Give main bullet points.
    """

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text