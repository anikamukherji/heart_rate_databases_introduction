from pymodm import connect
import datetime
import requests
import time

if __name__ == "__main__":
    connect("mongodb://localhost:27017/heart_rate_app")
    dict1 = {"user_email": "anika@anika.com", "user_age": 20,
             "age_units": "week", "heart_rate": 65}
    r = requests.post("http://localhost:5000/api/heart_rate", json=dict1)
    print(r.json())
    r2 = requests.get("http://localhost:5000/api/heart_rate/anika@anika.com")
    print(r2.json())
    d = datetime.datetime.now()
    time.sleep(2)
    dict2 = {"user_email": "anika@anika.com", "heart_rate": 61}
    r3 = requests.post("http://localhost:5000/api/heart_rate", json=dict2)
    print(r3.json())
    r4 = requests.get("http://localhost:5000/api/heart_rate/anika@anika.com")
    print(r4.json())
    r5 = requests.get("http://localhost:5000/api/heart_rate"
                      "/average/anika@anika.com")
    print(r5.json())
    dict3 = {"user_email": "anika@anika.com",
             "heart_rate_average_since": d.isoformat()}
    r6 = requests.post("http://localhost:5000/api/heart_rate/interval_average",
                       json=dict3)
    print(r6.json())
