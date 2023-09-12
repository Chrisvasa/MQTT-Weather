import random
import paho.mqtt.client as mqtt
import time

# Generates fake weather data and publishes it to the broker
def Main():
    client = mqtt.Client("Publisher")
    broker = "test.mosquitto.org"

    client.on_connect=on_connect
    client.on_message=on_message
    client.connect(broker)
    client.loop_start()

    weatherdata = [] # List for weather data
    for i in range(10):
        weatherdata.append(Weather())
        for data in weatherdata:
            client.publish(topic="weathervasa/WeatherForecast/Degrees",payload=f"{data.degrees}C")
            client.publish(topic="weathervasa/WeatherForecast/Humidity",payload=f"{data.humidity}%")
            client.publish(topic="weathervasa/WeatherForecast/Weather",payload=f"{data.weather}")
            client.on_message=on_message
            time.sleep(5)
        weatherdata.pop()
    client.loop_stop()

# Class that randomizes weather data
class Weather():
    def __init__(self):
        self.degrees = random.randint(-20,38)
        self.humidity = random.randint(0,100)
        if random.randint(0,1) == 1:
            self.weather = "Raining"
        else:
            self.weather = "Sunny"

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK Returned code=",rc)
    else:
        print("Bad connection Returned code=",rc)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

Main()