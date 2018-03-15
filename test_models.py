def test_user():
    """
    Tests User object initialization
    """
    try:
        from pymodm import connect
        from main import create_user, already_user
        import pytest
        import models
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
        from pymodm import connect
        from main import create_user, add_heart_rate
        import pytest
        import datetime
        import models
        import time
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    connect("mongodb://localhost:27017/heart_rate_app")
    create_user("test1@test.test", age=0, hr=1)
    u = models.User.objects.raw({"_id": "test1@test.test"}).first()
    assert u.average_hr() == 1.0
    add_heart_rate("test1@test.test", heart_rate=3,
                   time=datetime.datetime.now())
    u = models.User.objects.raw({"_id": "test1@test.test"}).first()
    assert u.average_hr() == 2.0
    d = datetime.datetime.today()
    time.sleep(3)
    add_heart_rate("test1@test.test", heart_rate=3,
                   time=datetime.datetime.now())
    u = models.User.objects.raw({"_id": "test1@test.test"}).first()
    assert u.average_hr(since_time=d) == 3.0
    add_heart_rate("test1@test.test", heart_rate=2,
                   time=datetime.datetime.now())
    u = models.User.objects.raw({"_id": "test1@test.test"}).first()
    assert u.average_hr(since_time=d) == 2.5
    add_heart_rate("test1@test.test", heart_rate=1,
                   time=datetime.datetime.now())
    u = models.User.objects.raw({"_id": "test1@test.test"}).first()
    assert u.average_hr(since_time=d) == 2.0
