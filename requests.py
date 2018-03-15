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
    return jsonify(heart_rates), 200


@app.route("/api/heart_rate/average/<user_email>", methods=["GET"])
def heart_rate_average():
    """
    Gets average heart rate for given user email

    :return: average heart rate
    :rtype: dict
    """
    r = request.get_json()
    try:
        email = r["user_email"]
    except KeyError as e:
        logging.warning("Incorrect JSON input: {}".format(e))
        d = {"error": "Incorrect JSON input"}
        return jsonify(d), 400
    av, is_tachycardic = get_av_hr(email)
    if av is None:
        logging.error("get_av_hr returned None. "
                      "User may not yet exist")
    average_hr = {
                  "heart_rate_average": av,
                  "is_tachycardic": is_tachycardic
                 }
    logging.debug("Returning average heart rate for {}: {}".format(email,
                  av))
    logging.dubug("This heart rate is tachycardic for"
                  "this user:".format(is_tachycardic))
    return jsonify(average_hr), 200


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def heart_rate_interval_average():
    """
    Returns average heart rate since given time

    :return: average heart rate over interval
    :rtype: dict
    """
    r = request.get_json()
    try:
        email = r["user_email"]
        interval_start = r["heart_rate_average_since"]
    except KeyError as e:
        logging.warning("Incorrect JSON input: {}".format(e))
        d = {"error": "Incorrect JSON input"}
        return jsonify(d), 400
    av, is_tachycardic = get_av_hr(email, since_time=interval_start)
    if av is None:
        logging.error("get_av_hr returned None. "
                      "User may not yet exist")
    average_hr = {
                  "heart_rate_average": av,
                  "is_tachycardic": is_tachycardic
                 }
    logging.debug("Returning average heart rate for {} since {}"
                  ": {}".format(email, interval_start, av))
    logging.dubug("This heart rate is tachycardic for"
                  "this user:".format(is_tachycardic))
    return jsonify(average_hr), 200
