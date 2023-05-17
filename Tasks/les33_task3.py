# Task 2
import requests

def get_longitude_longitude(city_name: str) -> tuple:
    url = f"http://api.openweathermap.org/geo/1.0/direct?"
    query = {'q': city_name,
             'appid': '189ea8a89b96b6e9b6c1913534965acc',
             'limit': 1}
    response = requests.get(url, params=query)
    return response.json()[0]['lat'], response.json()[0]['lon']

def exp_weathercode(code):
    with open('weather_code.txt', 'r', encoding='utf-8') as file:
        date = {}
        for i in file.readlines():
            date[int(i.split('-')[0])] = i.split('-')[1].strip()
    return date[code]

def get_current_weather(name: str):
    latitude, longitude = get_longitude_longitude(name)
    url = f"https://api.open-meteo.com/v1/forecast?"
    query = {'latitude': latitude,
             'longitude': longitude,
             'current_weather': True
             }
    response = requests.get(url, params=query)
    for parameters, val in response.json()['current_weather'].items():
        if parameters == 'weathercode':
            print(f"{parameters}: {exp_weathercode(val)}")
        elif parameters == 'is_day':
            if val == 0:
                print(f"{parameters}: Night")
            else:
                print(f"{parameters}: Day")
        else:
            print(f"{parameters}: {val}")


if __name__ == '__main__':
    city = input("Enter name of city: ")
    get_current_weather(city)
