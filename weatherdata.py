class Weather():
    def __init__(self, w, h, r):
        self.weather = w
        self.humidity = h
        self.rain = r

weatherdata = []

weatherdata.append(Weather(30, 90, 3))
weatherdata.append(Weather(15, 20, 2))

for i in weatherdata:
    print(i)


