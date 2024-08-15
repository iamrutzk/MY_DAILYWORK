import tkinter as tk
import requests
import json

def get_weather():
    city = city_entry.get()
    api_key = "YOUR_API_KEY_HERE"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?appid={api_key}&q={city}"
    response = requests.get(complete_url)
    data = response.json()
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    weather_label = tk.Label(root, text=f"Weather in {city}:\nTemperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {description}")
    weather_label.pack()

root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter city or zip code:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

root.mainloop()