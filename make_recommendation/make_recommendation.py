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


@make_recommendation_bp.route('/make_recommendation', methods=['POST', 'GET'])
def make_recommendation():
    if request.method == 'GET':
        return (jsonify({"status": "success", 
                            "data": {
                                "example_input": example_input,
                                "example_output": example_output,
                            }}), 200)
    elif request.method == 'POST':
        data = request.get_json()
        # Here you would process the input and generate recommendations
        return jsonify({"status": "success", "data": data}), 200
