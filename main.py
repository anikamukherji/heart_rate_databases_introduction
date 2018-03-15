from pymodm import connect
import models
import datetime


def add_heart_rate(email, heart_rate, time):
    """
    Takes in email of existing user and appends given
    heart rate and time to respective attributes

    :return: dict of user vals
    :rtype: dict
    """
    user = models.User.objects.raw({"_id": email}).first()
    user.heart_rate.append(heart_rate)
    user.heart_rate_times.append(time)
    user.save()
    return user.vals()


def create_user(email, age=None, hr=None):
    """
    Takes in email of new user, creates new user object, and appends given
    heart rate and current time to respective attributes

    :return: dict of new user vals
    :rtype: dict
    """
    u = models.User(email, age, [], [])
    if hr is not None:
        u.heart_rate.append(hr)
        u.heart_rate_times.append(datetime.datetime.now())
    u.save()
    return u.vals()


def print_user(email):
    """
    Takes in email of new user and prints out all attributes
    
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

    :raises: ValueError if user does not exist

    :return: list of heart rates
    :rtype: list
    :return: None if user does not exist
    :rtype: NoneType
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

    :returns: if user with email already exists
    :rtype: boolean
    """
    return models.User.objects.raw({"_id": email}).count() > 0


def get_av_hr(email, since_time=None):
    """
    Returns average heart rate of user with given email
    since some time if provided

    :return: average heart rate
    :rtype: float
    :return: None if user does not exist
    :rtype: NoneType
    """
    if already_user(email):
        user = models.User.objects.raw({"_id": email}).first()
    else:
        return None
    return user.average_hr(since_time=since_time)


if __name__ == "__main__":
    connect("mongodb://localhost:27017/heart_rate_app")
    if already_user("suyash@suyashkumar.com"):
        add_heart_rate("suyash@suyashkumar.com", 60, datetime.datetime.now())
    else:
        create_user("suyash@suyashkumar.com")
    print_user("suyash@suyashkumar.com")
