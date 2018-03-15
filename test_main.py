def test_add_heart_rate():
    """
    Tests main.add_heart_rate function
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


def test_get_av_hr():
    """
    Test main.get_av_hr function
    """
    try:
        from pymodm import connect
        from main import create_user, add_heart_rate, get_av_hr
        import pytest
        import datetime
        import time
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    connect("mongodb://localhost:27017/heart_rate_app")
    create_user("test1@test.test", age=0, hr=1)
    assert get_av_hr("test1@test.test") == 1.0
    add_heart_rate("test1@test.test", heart_rate=3,
                   time=datetime.datetime.now())
    assert get_av_hr("test1@test.test") == 2.0
    d = datetime.datetime.today()
    time.sleep(3)
    add_heart_rate("test1@test.test", heart_rate=3,
                   time=datetime.datetime.now())
    assert get_av_hr("test1@test.test", since_time=d) == 3.0
    add_heart_rate("test1@test.test", heart_rate=2,
                   time=datetime.datetime.now())
    assert get_av_hr("test1@test.test", since_time=d) == 2.5
    add_heart_rate("test1@test.test", heart_rate=1,
                   time=datetime.datetime.now())
    assert get_av_hr("test1@test.test", since_time=d) == 2.0
