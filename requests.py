from models import User
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/api/heart_rate", methods=["POST"])
def heart_rate_post():
    """
    Posts new user with given heart rate
    """
    r = request.get_json()
    email = r["user_email"]
    age = r["user_age"]
    hr = r["heart_rate"]
    pass


@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def heart_rate_get():
    """
    Gets heart rates for given user email

    :return: all heart rates for user
    :rtype: dict 
    """
    # return jsonify(heart_rates)
    pass


@app.route("/api/heart_rate/average/<user_email>", methods=["GET"])
def heart_rate_average():
    """
    Gets average heart rate for given user email

    :return: average heart rate
    :rtype: dict 
    """
    # return jsonify(average_hr)
    pass


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def heart_rate_interval_average():
    """
    Returns average heart rate since given time

    :return: average heart rate over interval
    :rtype: dict
    """
    # return jsonify(average_hr)
    pass
