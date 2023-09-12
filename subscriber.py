import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import pymongo
import time

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK Returned code=",rc)
        client.subscribe("weathervasa/#")
    else:
        print("Bad connection Returned code=",rc)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client("Python1")
broker = "test.mosquitto.org"

client.on_connect=on_connect
client.on_message=on_message
client.connect(broker)

print("Connecting to broker")
test = client.subscribe(topic="weathervasa/WeatherForecast/#")
print(test)
time.sleep(5)
client.loop_forever()