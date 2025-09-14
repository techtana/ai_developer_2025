from openai_client import OpenAIClient
from datetime import datetime, timedelta

today = datetime.now()

def get_user_inputs(uid: str):
    return [
        {
            "date": today - timedelta(days=1),
            "current_feeling": 2,
            "activity_done": ["run", "dance", "meditate"],
            "sleep": 8,
            "major_events" : ["looking for a job"],
            "additional_info": "I didn't have coffee this morning, so i am feeling tired"
        }
    ]

system_prompt = """
You are an analayser of user emotions an
"""