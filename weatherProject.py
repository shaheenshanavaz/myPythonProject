import os
import requests
from datetime import datetime
user_api = os.environ['current_weather_data']
# user_api = 'feea19ea9b0ad4d05f66673422e8eb5c'
location = input('Enter your city:')
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

complete_api_path = 'https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid='+user_api

api_request = requests.get(complete_api_path)
api_data = api_request.json()
# print(api_data)
if(api_data['cod'] == 404):
    print('Please type a valid city name')
else:
    temperature = ((api_data['main']['temp']) -273.15)
    feels_like = api_data['weather'][0]['description']
    humidity = api_data['main']['humidity']
    now = datetime.now()
    dt_time = now.strftime("%d/%m/%Y %H:%M:%S")

#     >>> f"Hello, {name}. You are {age}."
# 'Hello, Eric. You are 74.'
    print('--------------------------------------------------------------------------------')
    print(f'The Weather Stats of {location.upper()} and its current date and time {dt_time}')
    print('--------------------------------------------------------------------------------')
    print(f'Temperature is: {temperature: .2f}')
    print('Weather feels like: '+feels_like)
    print('Humidity is: {}'.format(humidity))



