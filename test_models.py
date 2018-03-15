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


def test_is_tachycardic():
    try:
        import pytest
        import datetime
        from models import User
        import time
    except ImportError as e:
        print("Necessary import failed: {}".format(e))
        return
    d = datetime.datetime.now()
    u = User("test@test.test", age=1, age_units="day")
    assert u.is_tachycardic(160) is True
    assert u.is_tachycardic(150) is False
    u.age = 5
    assert u.is_tachycardic(170) is True
    assert u.is_tachycardic(150) is False
    u.age = 1
    u.age_units = "week"
    assert u.is_tachycardic(185) is True
    assert u.is_tachycardic(180) is False
    u.age_units = "month"
    assert u.is_tachycardic(180) is True
    assert u.is_tachycardic(178) is False
    u.age = 5
    assert u.is_tachycardic(188) is True
    assert u.is_tachycardic(178) is False
    u.age = 10
    assert u.is_tachycardic(170) is True
    assert u.is_tachycardic(168) is False
    u.age = 1
    u.age_units = "year"
    assert u.is_tachycardic(160) is True
    assert u.is_tachycardic(150) is False
    u.age = 3
    assert u.is_tachycardic(140) is True
    assert u.is_tachycardic(130) is False
    u.age = 7
    assert u.is_tachycardic(135) is True
    assert u.is_tachycardic(125) is False
    u.age = 10
    assert u.is_tachycardic(132) is True
    assert u.is_tachycardic(128) is False
    u.age = 12
    assert u.is_tachycardic(120) is True
    assert u.is_tachycardic(115) is False
    u.age = 16
    assert u.is_tachycardic(101) is True
    assert u.is_tachycardic(99) is False
    u.age = 55
    assert u.is_tachycardic(101) is True
    assert u.is_tachycardic(99) is False
