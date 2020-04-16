import requests
from data import Location, WeatherElement

url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=rdec-key-123-45678-011121314'
html_content = requests.get(url) #向html提出get請求

json_content = html_content.json() #將內容轉為json
#print(json_content)

records = json_content.get('records')
location = records.get('location')

 #   print(location)
allLocations = []

for item in location:
    l = Location()
    l.from_json(item)

    weather_element_json = item.get('weatherElement')
    element = WeatherElement()
    element.from_json(weather_element_json)
    l.weather_element = element

    allLocations.append(l)



