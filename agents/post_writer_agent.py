# import os
# import time
# import random
# import requests
# from dotenv import load_dotenv
#
# load_dotenv()
#
# HF_API_KEY = os.getenv("HF_API_KEY")
#
# API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
#
# headers = {
#     "Authorization": f"Bearer {HF_API_KEY}"
# }
#
#
# def generate_post(profile, trend):
#     """
#     Generates a long LinkedIn post.
#     1. Tries Hugging Face model (with retry)
#     2. If HF fails, returns a dynamic long fallback post
#     """
#
#     prompt = f"""
# Write a detailed LinkedIn post (medium to long length).
#
# Guidelines:
# - 4–5 paragraphs
# - Explain the topic with examples
# - Relate it to Software Testing
# - Add learning points
# - Professional + friendly tone
# - Use emojis lightly
# - End with a question
# - Add 5–7 hashtags
#
# Context:
# Role: {profile['role']}
# Skills: {', '.join(profile['skills'])}
# Topic: {trend['topic']}
# """
#
#     # =========================
#     # 1️⃣ TRY HUGGING FACE (3 times)
#     # =========================
#     for attempt in range(3):
#         try:
#             response = requests.post(
#                 API_URL,
#                 headers=headers,
#                 json={
#                     "inputs": prompt,
#                     "parameters": {
#                         "max_new_tokens": 350,
#                         "temperature": 0.8,
#                         "top_p": 0.95,
#                         "do_sample": True
#                     }
#                 },
#                 timeout=90
#             )
#
#             result = response.json()
#
#             # ✅ Success case
#             if isinstance(result, list) and "generated_text" in result[0]:
#                 return result[0]["generated_text"]
#
#             # ⏳ Model loading / HF issue
#             if isinstance(result, dict) and "error" in result:
#                 print("⏳ Model loading, retrying in 10 seconds...")
#                 time.sleep(10)
#
#         except Exception as e:
#             print(f"⚠️ HF error: {e}")
#             time.sleep(5)
#
#     # =========================
#     # 2️⃣ FINAL FALLBACK (DYNAMIC + LONG)
#     # =========================
#     openings = [
#         "Over the past few months, I’ve been reflecting on how quickly technology is evolving.",
#         "Lately, I’ve been thinking about how the role of software testers is changing in modern teams.",
#         "In today’s fast-paced tech world, quality engineering is becoming more important than ever.",
#         "The expectations from software testers today are very different compared to a few years ago."
#     ]
#
#     middles = [
#         "Earlier, testing was mostly about executing test cases and reporting bugs. Today, testers are expected to think about quality, risk, and user experience.",
#         "Testing is no longer limited to finding defects. It now involves understanding systems deeply and ensuring reliability across environments.",
#         "With increasing system complexity, testers play a crucial role in improving stability and confidence in every release."
#     ]
#
#     skill_focus = [
#         "Automation Testing to reduce repetitive manual effort and speed up regression cycles",
#         "API Testing to ensure backend reliability and smooth integrations",
#         "AI-powered tools to improve test coverage and testing efficiency"
#     ]
#
#     endings = [
#         "Learning continuously and adapting to new tools has become essential for long-term growth in tech.",
#         "Staying curious and open to learning is the only way to remain relevant in this industry.",
#         "Upskilling regularly is no longer optional — it’s a necessity in today’s tech landscape."
#     ]
#
#     return f"""
# 🚀 {trend['topic']}
#
# {random.choice(openings)}
#
# As a {profile['role']}, I’m exploring how modern tools, automation, and AI-driven
# approaches are helping testers work smarter instead of harder. These tools reduce
# repetitive tasks and allow teams to focus more on quality, analysis, and overall
# product reliability.
#
# {random.choice(middles)}
#
# Currently, I’m focusing on:
# 🔹 {skill_focus[0]}
# 🔹 {skill_focus[1]}
# 🔹 {skill_focus[2]}
#
# {random.choice(endings)}
#
# How are you preparing yourself for the future of testing and technology?
#
# #SoftwareTesting #QA #Automation #AI #Learning #TechCareers
# """

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
