import requests
import string

def get_location():
    location = input("Enter the location: ").lower()
    words = location.split(" ")
    new_words = []
    for word in words:
        word = word.strip(string.punctuation)
        new_words.append(word)
    location = "%20".join(new_words)
    print(f"Your Location: {location}")
    r = requests.get(f"https://www.metaweather.com/api/location/search/?query={location}")
    if r.text == '[]':
        get_location()

    d = r.json()
    id = d[0]['woeid']
    s = requests.get(f"https://www.metaweather.com/api/location/{id}/")
    e = s.json()
    for forecast in e['consolidated_weather']:
        date = forecast['applicable_date']
        state = forecast['weather_state_name']
        min_temp = forecast['min_temp']
        max_temp = forecast['max_temp']
        humidity = forecast['humidity']
        print(f"Date: {date}, Weather: {state}, Min Temp: {min_temp}, "
              f"Max Temp: {max_temp}, Humidity: {humidity}")

if __name__ == "__main__":
    try:
        get_location()
    except requests.exceptions.ConnectionError:
        print("Server not responding, try again later....")
