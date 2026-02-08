import os
import random
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_post(profile, trend):
    """
    Generates a long LinkedIn post using Groq LLM.
    Always dynamic, fast, and reliable.
    """

    system_prompt = (
        "You are a professional LinkedIn content writer for tech professionals."
    )

    user_prompt = f"""
Write a detailed LinkedIn post (medium to long length).

Guidelines:
- 4–5 paragraphs
- Explain the topic clearly
- Relate it to real-world Software Testing
- Add learning points
- Professional + friendly tone
- Use emojis lightly
- End with a question
- Add 5–7 relevant hashtags

Context:
Role: {profile['role']}
Skills: {', '.join(profile['skills'])}
Topic: {trend['topic']}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.8,
        max_tokens=500,
        top_p=0.9,
    )

    return response.choices[0].message.content
