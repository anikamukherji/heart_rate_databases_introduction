from models import User
from main import *
import datetime
from flask import Flask, jsonify, request
import logging
logging.basicConfig(filename='requests.log', filemode='w',
                    level=logging.DEBUG)
app = Flask(__name__)


@app.route("/api/heart_rate", methods=["POST"])
def heart_rate_post():
    """
    Posts new user with given heart rate
    """
    r = request.get_json()
    try:
        email = r["user_email"]
        age = r["user_age"]
        hr = r["heart_rate"]
    except KeyError as e:
        logging.warning("Incorrect JSON input: {}".format(e))
        d = {"error": "Incorrect JSON input"}
        return jsonify(d), 400
    if already_user(email):
        u_vals = add_heart_rate(email, heart_rate=hr,
                                time=datetime.datetime.now())
    else:
        u_vals = create_user(email, age=age, hr=hr)
    logging.debug("adding hr to user: {}".format(u_vals))
    return jsonify(u_vals), 200


@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def heart_rate_get():
    """
    Gets heart rates for given user email

    :return: all heart rates for user
    :rtype: dict
    """
    heart_rates = get_heart_rates(user_email)
    if heart_rates is None:
        logging.warning("User with email does not exist".format(user_email))
        d = {"error": "User with email does not exist"}
        return jsonify(d), 400
    return jsonify(heart_rates)


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
