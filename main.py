from pymodm import connect
import models
import datetime


def add_heart_rate(email, heart_rate, time):
    user = models.User.objects.raw({"_id": "suyash@suyashkumar.com"}).first()
    user.heart_rate.append(heart_rate)
    user.heart_rate_times.append(time)
    user.save()


def create_user():
    u = models.User("suyash@suyashkumar.com", 24, [], [])
    u.heart_rate.append(60)
    u.heart_rate_times.append(datetime.datetime.now())
    u.save()


def print_user(email):
    user = models.User.objects.raw({"_id": "suyash@suyashkumar.com"}).first()
    print(user.email)
    print(user.heart_rate)
    print(user.heart_rate_times)


if __name__ == "__main__":
    connect("mongodb://localhost:27017/heart_rate_app")
    # create_user()
    add_heart_rate("suyash@suyashkumar.com", 60, datetime.datetime.now())
    print_user("suyash@suyashkumar.com")
