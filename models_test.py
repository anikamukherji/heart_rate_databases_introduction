from pymodm import connect
from models import User
from main import *
import datetime


def test_user():
    """
    Tests User object initialization
    """
    try:
        import pytest
        from models import User 
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    connect("mongodb://localhost:27017/heart_rate_app")
    create_user("test@test.test", age=0, hr=1)
    assert already_user("test@test.test") is True
    u = models.User.objects.raw({"_id": "test@test.test"}).first()
    assert u.age == 0
    assert u.heart_rate == [1]


def test_average_hr():
    """
    Tests User object average_hr function
    """
    try:
        import pytest
        from models import User 
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    connect("mongodb://localhost:27017/heart_rate_app")
    create_user("test1@test.test", age=0, hr=1)
    u = models.User.objects.raw({"_id": "test@test.test"}).first()
    assert u.average_hr() == 1
    add_heart_rate("test1@test.test", heart_rate=3,
                    time=datetime.datetime.now())
    assert u.average_hr() == 2.0
