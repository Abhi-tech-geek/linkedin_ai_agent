import random

def fetch_trend():
    trends = [
        "AI in Software Testing",
        "Future of QA with AI",
        "How AI helps Testers",
        "Automation Testing with AI"
    ]

    return {"topic": random.choice(trends)}
