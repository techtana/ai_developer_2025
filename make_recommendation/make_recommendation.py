from flask import Blueprint, request, jsonify

make_recommendation_bp = Blueprint('make_recommendation', __name__)

@make_recommendation_bp.route('/make_recommendation', methods=['POST'])
def make_recommendation():
    # Dummy implementation
    data = request.get_json()


    
    return jsonify({"status": "recommendation made", "received": data}), 200
