# Weather Data Collector and Publisher

This project consists of two Python scripts that work together to collect weather data and publish it to an MQTT broker. The collected data is then stored in a MongoDB database for further analysis or use.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Script Descriptions](#script-descriptions)
- [License](#license)

## Introduction

In this project, we have two main scripts:

1. **Weather Data Collector (`subscriber.py`):**

   This script subscribes to MQTT topics containing weather data, formats the incoming payloads, and stores the data into a MongoDB database.

2. **Weather Data Publisher (`publisher.py`):**

   This script generates fake weather data, publishes it to MQTT topics, and simulates periodic updates.

## Requirements

Before running the scripts, ensure you have the following dependencies installed:

- Python 3.x
- [Paho MQTT](https://pypi.org/project/paho-mqtt/): MQTT client library for Python
- [PyMongo](https://pypi.org/project/pymongo/): MongoDB driver for Python
- An MQTT broker (e.g., [Mosquitto](https://mosquitto.org/)) if you don't already have one.
- Access to a MongoDB server if you plan to store the data.

## Usage

1. **Clone this repository:**

``` bash 
git clone https://github.com/Chrisvasa/MQTT-Weather.git
cd MQTT-Weather ```


2. **Modify the scripts as needed:**

- Replace the placeholders `{usernamehere}`, `{passwordhere}`, and `{urlhere}` in `subscriber.py` with your MongoDB credentials and connection URI.
- You can customize the MQTT broker settings (e.g., broker URL, topics) in both scripts as per your requirements.

-  **Run the Weather Data Collector:**

``` python subscriber.py ```

- **Run the Weather Data Publisher:**

```python publisher.py```


5. The collector will listen for incoming weather data on the specified MQTT topics and store it in the MongoDB database.

6. The publisher will generate fake weather data and publish it to the MQTT topics, simulating updates.

## Script Descriptions

### Weather Data Collector (`subscriber.py`)

- Subscribes to specified MQTT topics.
- Formats incoming payloads and appends them to a list of dictionaries.
- Combines collected data into one dictionary and inserts it into the MongoDB database.
- The script is designed to collect data from three different weather topics: Degrees, Humidity, and Weather.

### Weather Data Publisher (`publisher.py`)

- Generates fake weather data (temperature, humidity, weather condition) for demonstration purposes.
- Publishes this fake data to the specified MQTT topics.
- Simulates updates every 5 seconds.

## License

This project is licensed under the [MIT License](LICENSE).


