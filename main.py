from pymodm import connect
import models
import datetime


def add_heart_rate(email, heart_rate, time):
    user = models.User.objects.raw({"_id": email}).first()
    user.heart_rate.append(heart_rate)
    user.heart_rate_times.append(time)
    user.save()


def create_user(email, age=None, hr=None):
    u = models.User(email, age, [], [])
    if hr is None:
        u.heart_rate.append(hr)
        u.heart_rate_times.append(datetime.datetime.now())
    u.save()


def print_user(email):
    user = models.User.objects.raw({"_id": email}).first()
    print(user.email)
    print(user.heart_rate)
    print(user.heart_rate_times)


def user_dict(email):
    user = models.User.objects.raw({"_id": email}).first()
    vals = {
            "user_email": user.email,
            "user_age": user.age,
            "heart_rates": user.heart_rate,
            "heart_rate_times": user.heart_rate_times
            }
    return vals


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
