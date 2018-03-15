def test_user():
    """
    Tests User object initialization
    """
    try:
        from pymodm import connect
        import pytest
        import datetime
        from models import User
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    d = datetime.datetime.now()
    u = User("test@test.test", age=0, heart_rate=[1], heart_rate_times=[d])
    assert u.email == "test@test.test"
    assert u.age == 0
    assert u.heart_rate == [1]
    assert u.heart_rate_times == [d]


def test_average_hr():
    """
    Tests User object average_hr function
    """
    try:
        import pytest
        import datetime
        from models import User
        import time
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    d = datetime.datetime.now()
    u = User("test@test.test", age=0, heart_rate=[1], heart_rate_times=[d])
    assert u.average_hr() == 1.0
    u.heart_rate += [3]
    u.heart_rate_times += [d]
    assert u.average_hr() == 2.0
    d2 = datetime.datetime.now()
    time.sleep(3)
    u.heart_rate += [3]
    u.heart_rate_times += [datetime.datetime.now()]
    assert u.average_hr(since_time=d2) == 3.0
    u.heart_rate += [2]
    u.heart_rate_times += [datetime.datetime.now()]
    assert u.average_hr(since_time=d2) == 2.5
    u.heart_rate += [1]
    u.heart_rate_times += [datetime.datetime.now()]
    assert u.average_hr(since_time=d2) == 2.0


def test_adjust_age():
    """
    Tests User object average_hr function
    """
    try:
        import pytest
        import datetime
        from models import User
        import time
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    d = datetime.datetime.now()
    u = User("test@test.test", age=8, age_units="day",
             heart_rate=[1], heart_rate_times=[d])
    u.adjust_age()
    assert u.age == 1
    assert u.age_units == "week"
    u.age = 13
    u.adjust_age()
    assert u.age == 3
    assert u.age_units == "month"
    u.age = 25
    u.adjust_age()
    assert u.age == 2
    assert u.age_units == "year"
    u.age = 15
    u.adjust_age()
    assert u.age == 15
    assert u.age_units == "year"
    invalid_units = ["second", 10, "invalid"]
    for i in invalid_units:
        with pytest.raises(ValueError):
            u.age_units = i
            u.adjust_age()
