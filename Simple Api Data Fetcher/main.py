import requests
import pandas as pd

def fetch_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'City': data['name'],
            'Temperature (°C)': data['main']['temp'],
            'Humidity (%)': data['main']['humidity'],
            'Weather': data['weather'][0]['description']
        }
        return weather_data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def save_to_csv(data):
    df = pd.DataFrame([data])
    df.to_csv('weather_data.csv', index=False)

def main():
    city = input("Enter the city name: ")
    api_key = "/"  # Replace with your actual API key
    weather_data = fetch_weather_data(city, api_key)
    
    if weather_data:
        save_to_csv(weather_data)
        print(f"Weather data for {city} saved to 'weather_data.csv'.")

if __name__ == "__main__":
    main()
