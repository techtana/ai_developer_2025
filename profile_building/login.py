from flask import Blueprint, request, jsonify

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    # Dummy implementation
    data = request.get_json()
    return jsonify({"status": "login successful", "received": data}), 200
