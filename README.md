# 🤖 LinkedIn AI Agent (Human‑in‑the‑Loop)

An AI-powered LinkedIn content agent that generates **long, high‑quality, personalized LinkedIn posts** based on user profile and trending topics — with **manual approval** for safety and control.

---

## 🚀 Project Overview

This project demonstrates how an **AI Agent** can assist professionals by generating meaningful LinkedIn posts automatically, while still keeping a **human in control** before publishing.

The system:

* Reads user profile data (role, skills, experience)
* Selects a relevant tech topic
* Uses a Large Language Model (LLM) to generate a long LinkedIn post
* Asks for **manual approval** before finalizing the content

This mirrors **real-world AI usage in companies**, where AI assists but humans make the final decision.

---

## 🧠 Key Concepts Used

* AI Agents
* Large Language Models (LLMs)
* Prompt Engineering
* Human‑in‑the‑Loop Design
* API Integration
* Clean Architecture
* Environment Variable Security

---

## 🏗️ System Architecture

```
profile.json  →  profile_agent
                    ↓
            trend_agent
                    ↓
          post_writer_agent (AI)
                    ↓
           approval_agent
                    ↓
           approved_post.txt
```

---

## 📂 Project Structure

```
linkedin_ai_agent/
│
├── agents/
│   ├── profile_agent.py
│   ├── trend_agent.py
│   ├── post_writer_agent.py
│   └── approval_agent.py
│
├── memory/
│   └── profile.json
│
├── .env
├── main.py
└── approved_post.txt
```

---

## 📄 File‑by‑File Explanation

### 1️⃣ `memory/profile.json`

Stores user‑specific data used to personalize AI output.

Example:

```json
{
  "name": "Abhinav",
  "role": "Software Tester",
  "skills": ["Automation Testing", "API Testing", "AI Tools"],
  "experience": "1+ years",
  "tone": "professional + friendly"
}
```

---

### 2️⃣ `agents/profile_agent.py`

Loads profile data from JSON.

Purpose:

* Keeps data handling separate from AI logic
* Improves maintainability

---

### 3️⃣ `agents/trend_agent.py`

Selects a trending tech topic.

Currently:

* Uses mocked topics for demo

Future enhancement:

* Can be replaced with live APIs (blogs, news, GitHub trends)

---

### 4️⃣ `agents/post_writer_agent.py` (Core AI Agent)

Responsibilities:

* Builds a structured prompt
* Calls the Groq LLM API
* Generates long‑form LinkedIn posts
* Ensures dynamic, non‑repetitive output

Key features:

* Prompt engineering for length & tone
* Controlled generation parameters
* Reliable and fast inference using Groq

---

### 5️⃣ `agents/approval_agent.py`

Implements **human approval**.

Flow:

* Displays generated post
* Asks user to approve or reject
* Saves approved content to `approved_post.txt`

This ensures ethical and safe AI usage.

---

### 6️⃣ `main.py`

Acts as the **orchestrator**.

Controls execution flow:

1. Load profile
2. Fetch topic
3. Generate post
4. Ask for approval

---

### 7️⃣ `.env`

Stores sensitive credentials securely.

Example:

```env
GROQ_API_KEY=your_api_key_here
```

Secrets are never hardcoded in source files.

---

## ⚙️ Tech Stack

* Python 3
* Groq LLM API (LLaMA 3.1)
* python‑dotenv
* Clean modular architecture

---

## ▶️ How to Run

1. Clone the repository
2. Create a `.env` file with your Groq API key
3. Install dependencies

   ```bash
   python -m pip install groq python-dotenv
   ```
4. Run the agent

   ```bash
   python main.py
   ```
5. Approve the generated LinkedIn post

---

## 🔐 Why Manual Approval?

* Prevents spam or unsafe content
* Avoids LinkedIn policy violations
* Reflects real corporate AI workflows

This design choice follows **responsible AI principles**.

---

## 🧪 Sample Output

* Long, well‑structured LinkedIn post
* Real‑world testing examples
* Clear learning points
* Call‑to‑action question

---

## 🎯 Resume / Interview Description

> Built an AI-powered LinkedIn content agent using Python and Groq LLMs with human‑in‑the‑loop approval, profile‑based personalization, and structured prompt engineering.

---

## 🔮 Future Enhancements

* UI with preview & approve button
* Scheduler for daily post reminders
* Multi‑LLM support (Groq, Gemini, Local AI)
* Live trend fetching
* Hinglish content mode

---

## ✅ Conclusion

This project demonstrates **real‑world AI engineering**, not just API usage. It focuses on reliability, safety, personalization, and clean design — exactly how AI systems are built in production environments.

---

💡 *AI should assist humans, not replace them — this project is built on that principle.*
