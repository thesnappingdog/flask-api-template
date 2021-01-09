from flask import current_app, jsonify
from app.api import bp

@bp.route('/', methods=['GET'])
def index():
    return jsonify({
        "hello?": "world"
    })

