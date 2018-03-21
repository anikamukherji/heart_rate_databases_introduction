from pymodm import connect
import datetime
import requests

if __name__ == "__main__":
    connect("mongodb://localhost:27017/heart_rate_app")
    u_dict = {"user_email": "anika@anika.com", "user_age": 20,
              "age_units":"week", "heart_rate": 65}
    r = requests.post("http://localhost:5000/api/heart_rate", json=u_dict)
    print(r.json())
    r2 = requests.get("http://localhost:5000/api/heart_rate/anika@anika.com")
    print(r2.json())
    e_dict = {"user_email": "anika@anika.com", "heart_rate": 61}
    r3 = requests.post("http://localhost:5000/api/heart_rate", json=e_dict)
    print(r3.json())
    r4 = requests.get("http://localhost:5000/api/heart_rate/anika@anika.com")
    print(r4.json())
    r5 = requests.get("http://localhost:5000/api/heart_rate/average/anika@anika.com")
    print(r5.json())
