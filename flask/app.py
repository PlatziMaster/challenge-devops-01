from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    ip_address = request.remote_addr
    return "Flask, Requester IP: " + ip_address