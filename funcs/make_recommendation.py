example_input = {
    "user_id": '1241323',
    "prev_recommendations": {
        "_id": '64f8c3e2e4b0c9b1a1d2f3g4',
        "rating": 4
    },
    "responses": {
        "mood": 3,
        "sleep": 3,
        "activities": [],
        "other": "I enjoy documentaries."
    }
}

example_output = {
    "recommendations": {
        "item": "Go running for 30 minutes",
        "reason": "To better health"
    }
}

def make_recommendation(uid, feedback, prompt):
    recommendation = None
    return recommendation

