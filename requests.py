from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/api/heart_rate", methods=["POST"])
def heart_rate_post():
    pass


@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def heart_rate_get():
    pass


@app.route("/api/heart_rate/average/<user_email>", methods=["GET"])
def heart_rate_average():
    pass


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def heart_rate_interval_average():
    pass
