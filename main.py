from pymodm import connect
import models
import datetime


def add_heart_rate(email, heart_rate, time):
    """
    Takes in email of existing user and appends given
    heart rate and time to respective attributes

    :param email: email of user
    :type email: string
    :param heart_rate: current heart rate of user
    :type heart_rate: int
    :param time: date/time heart rate was taken
    :type time: datetime.date

    :return: dict of user vals
    :rtype: dict
    """
    user = models.User.objects.raw({"_id": email}).first()
    user.heart_rate.append(heart_rate)
    user.heart_rate_times.append(time)
    user.save()
    return user.vals()


def create_user(email, age=None, age_units="year", hr=None):
    """
    Takes in email of new user, creates new user object, and appends given
    heart rate and current time to respective attributes

    :param email: email of user
    :type email: string
    :param age: age of user
    :type age: int
    :param age_units: units of time of given age (should be year, month, week)
    :type age_units: string
    :param hr: current heart rate of user
    :type hr: int

    :return: dict of new user vals
    :rtype: dict
    """
    u = models.User(email, age, age_units, [], [])
    if hr is not None:
        u.heart_rate.append(hr)
        u.heart_rate_times.append(datetime.datetime.now())
    u.adjust_age()
    u.save()
    return u.vals()


def print_user(email):
    """
    Takes in email of new user and prints out all attributes

    :param email: email of user
    :type email: string
    :raises: ValueError if user does not exist
    """
    if not already_user(email):
        print("User does not exist")
        raise ValueError()
    user = models.User.objects.raw({"_id": email}).first()
    print(user.email)
    print(user.heart_rate)
    print(user.heart_rate_times)


def get_heart_rates(email):
    """
    Returns all heart rates for user if user exists

    :param email: email of user
    :type email: string
    :raises: ValueError if user does not exist

    :return: list of heart rates
    :rtype: list
    """
    if already_user(email):
        user = models.User.objects.raw({"_id": email}).first()
    else:
        print("User does not exist")
        raise ValueError()
    return user.heart_rate


def already_user(email):
    """
    Returns whether user has already been created

    :param email: email of user
    :type email: string

    :returns: if user with email already exists
    :rtype: boolean
    """
    return models.User.objects.raw({"_id": email}).count() > 0


def get_av_hr(email, since_time=None):
    """
    Returns average heart rate of user with given email
    since some time if provided

    :param email: email of user
    :type email: string
    :param since_time: start date for calculating average heart rate
    :type since_time: datetime.date
    :raises: ValueError if user does not exist

    :return: average heart rate
    :rtype: float
    """
    if already_user(email):
        user = models.User.objects.raw({"_id": email}).first()
    else:
        print("User does not exist")
        raise ValueError()
    return user.average_hr(since_time=since_time)
