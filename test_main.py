def test_add_heart_rate():
    """
    Tests main.add_heart_rate function
    """
    try:
        from pymodm import connect
        from main import add_heart_rate
        import pytest
        import models
        import datetime
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    d = datetime.datetime.now()
    connect("mongodb://localhost:27017/heart_rate_app")
    u = models.User("test@test.test", age=0, heart_rate=[1],
                    heart_rate_times=[d])
    u.save()
    u = models.User.objects.raw({"_id": "test@test.test"}).first()
    ret = add_heart_rate("test@test.test", heart_rate=4, time=d)
    assert ret["user_email"] == "test@test.test"
    assert ret["user_age"] == 0
    assert ret["heart_rates"] == [1, 4]
    assert len(ret["heart_rate_times"]) == 2


def test_create_user():
    try:
        from pymodm import connect
        from main import create_user
        import pytest
        import models
        import datetime
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    connect("mongodb://localhost:27017/heart_rate_app")
    vals = create_user("test@test.test", age=0, hr=1)
    u = models.User.objects.raw({"_id": "test@test.test"}).first()
    assert u.email == "test@test.test"
    assert u.age == 0
    assert u.heart_rate == [1]
    assert len(u.heart_rate_times) == 1
    assert u.email == vals["user_email"]
    assert u.age == vals["user_age"]
    assert u.heart_rate == vals["heart_rates"]


def test_print_user():
    """
    Test main.print_user function
    """
    try:
        from main import print_user
        import models
        import pytest
        import datetime
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    with pytest.raises(ValueError):
        print_user("doesnotexist@test.test")
    u = models.User("doesexist@test.test", age=0, heart_rate=[1],
                    heart_rate_times=[datetime.datetime.now()])
    u.save()
    assert print_user("doesexist@test.test") is None


def test_get_heart_rates():
    """
    Tests main.get_heart_rates function
    """
    try:
        from main import get_heart_rates
        import models
        import pytest
        import datetime
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    with pytest.raises(ValueError):
        get_heart_rates("doesnotexist@test.test")
    u = models.User("doesexist@test.test", age=0, heart_rate=[1, 2, 3],
                    heart_rate_times=[datetime.datetime.now()])
    u.save()
    assert get_heart_rates("doesexist@test.test") == [1, 2, 3]


def test_already_user():
    """
    Tests main.already_user function
    """
    try:
        from main import already_user
        import models
        import pytest
        import datetime
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    assert already_user("doesnotexist@test.test") is False
    u = models.User("doesexist@test.test", age=0, heart_rate=[1, 2, 3],
                    heart_rate_times=[datetime.datetime.now()])
    u.save()
    assert already_user("doesexist@test.test") is True



def test_get_av_hr():
    """
    Test main.get_av_hr function
    """
    try:
        from pymodm import connect
        from main import add_heart_rate, get_av_hr
        import models
        import pytest
        import datetime
        import time
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    connect("mongodb://localhost:27017/heart_rate_app")
    u = models.User("test1@test.test", age=0, heart_rate=[1],
                    heart_rate_times=[datetime.datetime.now()])
    u.save()
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
