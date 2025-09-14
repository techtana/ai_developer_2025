from flask import Blueprint, request, jsonify

create_questionaire_bp = Blueprint('create_questionaire', __name__)

example_data = {
    "prev_recommendations": {
        "_id": '64f8c3e2e4b0c9b1a1d2f3g4',
        "item": "Go running for 30 minutes",
        "reason": "To better health"
    }
}

@create_questionaire_bp.route('/create_questionaire', methods=['POST'])
def update_profile():
    # Dummy implementation
    data = request.get_json()
    
    return jsonify({"status": "success", "response": example_data}), 200
