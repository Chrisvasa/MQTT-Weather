import paho.mqtt.subscribe as subscribe
import pymongo
import time

# Creates a client that connects to the broker
def Main():
    print("Connecting to broker")
    subscribe.callback(callback=on_message, topics="weathervasa/WeatherForecast/#", hostname="test.mosquitto.org")

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK Returned code=",rc)
        client.subscribe("weathervasa/#")
    else:
        print("Bad connection Returned code=",rc)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

Main()