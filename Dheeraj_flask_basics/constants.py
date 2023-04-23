from main import app
from flask import jsonify


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'code': 400, 'message': 'Not Found'}), 404


@app.errorhandler(405)
def method_not_allowed_error(error):
    return jsonify({'code': 405, 'message': 'Method Not Allowed'}), 405


@app.errorhandler(200)
def success_request(error):
    return jsonify({'code': 200, 'message': 'Successful request'}), 200

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'code': 401, 'message': 'Unauthorized request'}), 401

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'code': 500, 'message': 'Internal Server Error'}), 500

