"""
flask app (web server)
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    """ simply returns the IP of the caller """
    return jsonify({"ip": request.environ.get('HTTP_X_REAL_IP',
                                              request.remote_addr)}), 200
