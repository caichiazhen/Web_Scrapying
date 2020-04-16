class Location:
    def __init__(self, new_location_name=None,
                 lat=None, lon=None, station_id=None, time=None, weather_element=None):
        self.location_name = new_location_name
        self.lat = lat
        self.lon = lon
        self.station_id = station_id
        self.time = time
        self.weather_element = weather_element

    def from_json(self, json_data):
        self.lat = json_data.get('lat')
        self.lon = json_data.get('lon')
        self.location_name = json_data.get('locationName')
        self.station_id = json_data.get('stationID')
        time1 = json_data.get('time')
        self.time = time1.get('obsTime')


class WeatherElement:
    def __init__(self, wdir=None, wdsd=None, temp=None, humd=None, h24r=None):
        self.wdir= wdir
        self.wdsd = wdsd
        self.temp = temp
        self.humd = humd
        self.h24r = h24r

    def from_json(self, weather_element):

        for element in weather_element:
            elementName = element.get('elementName')
            elementValue = element.get('elementValue')

            if elementName == 'WDIR':
                self.wdir = elementValue

            if elementName == 'WDSD':
                self.wdsd = elementValue

            if elementName == 'TEMP':
                self.temp = elementValue

            if elementName == 'HUMD':
                self.humd = elementValue

            if elementName == '24R':
                self.h24r = elementValue
