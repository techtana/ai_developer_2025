from flask import Blueprint, request, jsonify

update_model_bp = Blueprint('update_model', __name__)


@update_model_bp.route('/update_model', methods=['POST', 'GET'])
def update_model():
    if request.method == 'GET':
        return jsonify({"status": "success", "response": None}), 200
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify({"status": "success", "response": data}), 200
