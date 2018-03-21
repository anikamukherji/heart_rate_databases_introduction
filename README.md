# Heart Rate Databases Introduction Assignment
## Anika Mukherji BME 590

Simple API and database project for storing users, heart rates, and finding averages  using Flask and MongoDB

Requires creating a virtual environment and then running...
```
pip3 install -r requirements.txt
```
Can run db on local environment with docker installed...
```
docker run -v $PWD/db:/data/db -p 27017:27017 mongo
```
Can run server locally with flask...
```
FLASK_APP=server.py flask run
```
For API examples, run `requests_test.py`

Creating new user requires user email, age, and current heart rate

Supports user ages of unit `day`, `week`, `month`, or `year`, but will default to `year`

Determines if an average heart rate is tachycardic based on the most reliable of all sites, Wikipedia: <https://en.wikipedia.org/wiki/Tachycardia>
