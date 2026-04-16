import requests
import os
from dotenv import load_dotenv


def get_weather(city):
    load_dotenv()
    API_KEY = os.getenv('OPENWEATHER_API_KEY')
    url = (f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial')

    print(url)
    data = requests.get(url).json()

    return {data['main']['temp']}
