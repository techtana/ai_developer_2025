from flask import Blueprint, request, jsonify

update_profile_bp = Blueprint('update_profile', __name__)

@update_profile_bp.route('/update_profile', methods=['POST'])
def update_profile():
    # Dummy implementation
    data = request.get_json()


    
    return jsonify({"status": "profile updated", "received": data}), 200
