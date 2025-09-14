from flask import Blueprint, request, jsonify

make_recommendation_bp = Blueprint('make_recommendation', __name__)


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


@make_recommendation_bp.route('/make_recommendation', methods=['POST'])
def make_recommendation():
    # Dummy implementation
    data = request.get_json()


    
    return jsonify({"status": "recommendation made", "received": example_output}), 200
