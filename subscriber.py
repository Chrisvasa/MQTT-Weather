import paho.mqtt.subscribe as subscribe
from pymongo import MongoClient

user = "{usernamehere}" # Replace with your username
password = "{passwordhere}" # Replace with your password
uri = f"{urlhere}"
client = MongoClient(uri)
db = client["weather_data"]
coll = db["weather"]

weatherdata = []
# Subscribes to the broker and listens for the different weather topics
def Main():
    print("Connecting to broker")
    subscribe.callback(callback=on_message, topics="weathervasa/WeatherForecast/#", hostname="test.mosquitto.org")

# When a weather topic gets updated, this gets called
# Formats the incoming payload, and appends it to a list of dicts
# Then combines the three different items into one dict and adds it to the DB
def on_message(client, userdata, msg):
    if(len(weatherdata) >= 3):
        result = {}
        for d in weatherdata:
            result.update(d)
        x = coll.insert_one(result)
        print("Post success:",x.acknowledged)
        weatherdata.clear()
    topic = msg.topic.split("/")
    data = msg.payload.decode("utf-8")
    weatherdata.append({f"{topic[2]}": f'{data}'})

Main()