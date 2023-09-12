from requests import post
import paho.mqtt.client as mqtt
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

# client.loop_start()
print("Connecting to broker")
client.publish(topic="weathervasa/test",payload="Robert är en riktig noob")
time.sleep(4)

# client.loop_stop()