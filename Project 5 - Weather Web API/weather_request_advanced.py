# Features:
# 1. Have display_weather print the weather report.
# 2. Handle network errors by printing a friendly message.
# Also refer weather_request_simple.py for simpler approach


import requests

API_ROOT = 'https://www.metaweather.com'
API_LOCATION = '/api/location/search/?query='
API_WEATHER = '/api/location/'  # + woeid

def fetch_location(query):
    return requests.get(API_ROOT + API_LOCATION + query).json()

def fetch_weather(woeid):
    return requests.get(API_ROOT + API_WEATHER + str(woeid)).json()

def display_weather(weather):
    print(f"Weather for {weather['title']}:")
    for forecast in weather['consolidated_weather']:
        date = forecast['applicable_date']
        state = forecast['weather_state_name']
        min_temp = forecast['min_temp']
        max_temp = forecast['max_temp']
        humidity = forecast['humidity']
        print(f"Date: {date}, Weather: {state}, Min Temp: {min_temp}, "
              f"Max Temp: {max_temp}, Humidity: {humidity}")

def disambiguate_locations(locations):
    print("Ambiguous location! Did you mean:")
    for loc in locations:
        print(f"\t* {loc['title']}")

def weather_dialog():
    try:
        where = ''
        while not where:
            where = input("Where in the world are you? ")
        locations = fetch_location(where)
        if len(locations) == 0:
            print("I don't know where that is.")
        elif len(locations) > 1:
            disambiguate_locations(locations)
        else:
            woeid = locations[0]['woeid']
            display_weather(fetch_weather(woeid))
    except requests.exceptions.ConnectionError:
        print("Server not responding, try again later....")

if __name__ == '__main__':
    while True:
        weather_dialog()
