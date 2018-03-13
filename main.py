from pymodm import connect
import models
import datetime


def add_heart_rate(email, heart_rate, time):
    """
    Takes in email of existing user and appends given
    heart rate and time to respective attributes
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
    """
    user = models.User.objects.raw({"_id": email}).first()
    print(user.email)
    print(user.heart_rate)
    print(user.heart_rate_times)


def get_heart_rates(email):
    if already_user(email):
        user = models.User.objects.raw({"_id": email}).first()
    else:
        return None
    return user.heart_rate


def already_user(email):
    return models.User.objects.raw({"_id": email}).count() > 0


if __name__ == "__main__":
    connect("mongodb://localhost:27017/heart_rate_app")
    if already_user("suyash@suyashkumar.com"):
        add_heart_rate("suyash@suyashkumar.com", 60, datetime.datetime.now())
    else:
        create_user("suyash@suyashkumar.com")
    print_user("suyash@suyashkumar.com")
