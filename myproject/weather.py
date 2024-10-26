from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

api_key = os.getenv("API_KEY_WEATHER")

def get_weather(city="Tashkent"):
    url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=metric"
    response = requests.get(url).json()
    if response["cod"] != 200:
        print("Error: ", response["message"])
        return "City not founded"
    else: 
        return response


if __name__ == "__main__":
    
    city = input("Enter city name: ")
    if not bool(city.strip()):
        city = "Tashkent"
        
    weather_data = get_weather(city)
    
    
    
