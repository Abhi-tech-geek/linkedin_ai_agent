import json

def load_profile():
    with open("memory/profile.json", "r") as f:
        return json.load(f)
