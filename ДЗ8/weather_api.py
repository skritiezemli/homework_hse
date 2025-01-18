import requests
import json

api_key = "c8b20a16a5b0679b27e511f47ab26c19"


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    data = response.json()
    return data


city = input("Введите название города: ")
try:
    weather_data = get_weather(city)
    print(f"Температура в {city}: {weather_data['main']['temp']}°C")
    print(f"Описание: {weather_data['weather'][0]['description']}")
except KeyError as e:
    print(f"Произошла ошибка при выполнении запроса")
    exit()
