"""
flask app (web server)
"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return str(request.remote_addr)
