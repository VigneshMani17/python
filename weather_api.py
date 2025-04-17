import requests
import datetime

base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "79af113b037e661cce34602e28084ad6"

def whether_info(city_name):
    url = f"{base_url}appid={api_key}&q={city_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error retrieving data: {response.status_code}")

def kelvin_to_celsius_fahrenheit(kelvin,min_temp, max_temp):
    celsius = kelvin - 273.15
    celsius_min = min_temp - 273.15
    celsius_max = max_temp - 273.15
    return celsius, celsius_min, celsius_max    


city_name = input("Enter the name of the city: ")
whether_data = whether_info(city_name)
kelvin = whether_data['main']['temp']
min_temp = whether_data['main']['temp_min']
max_temp = whether_data['main']['temp_max']
celsius, min_temp,max_temp = kelvin_to_celsius_fahrenheit(kelvin,min_temp,max_temp)
humidity = whether_data['main']['humidity']
wind_speed = whether_data['wind']['speed']
description = whether_data['weather'][0]['description']
cloudiness = whether_data['clouds']['all']
country = whether_data['sys']['country']
sun_rise = whether_data['sys']['sunrise']
sun_set = whether_data['sys']['sunset']

print(f"City: {city_name.capitalize()}")
print(f"Country: {country}")    
print(f"Temperature: {celsius:.2f} °C")
print(f"Minimum Temperature: {min_temp} K")
print(f"Maximum Temperature: {max_temp} K")
print(f"Humidity: {humidity}%")
print(f"Wind Speed: {wind_speed} m/s")
print(f"Description: {description.capitalize()}")
print(f"Cloudiness: {cloudiness}%")
print(f"Sunrise: {datetime.datetime.fromtimestamp(sun_rise).strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Sunset: {datetime.datetime.fromtimestamp(sun_set).strftime('%Y-%m-%d %H:%M:%S')}")