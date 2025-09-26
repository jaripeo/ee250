import requests

# WeatherAPI key
WEATHER_API_KEY = 'd4ab02f2c8644fb4a2503734251709'  # TODO: Replace with your own WeatherAPI key

def get_weather(city):
    base_url = 'http://api.weatherapi.com/v1/current.json'
    params = {
        'key': WEATHER_API_KEY,
        'q': city,
        'aqi': 'no'
    }
    try:
        response = requests.get(base_url, params=params)
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return

    if response.status_code == 200:
        data = response.json()
        current = data.get('current', {})
        location = data.get('location', {})
        print(f"Status {response.status_code}: Ok")
        print(f"Weather data for {location.get('name', city)}")
        print(f"  Temperature: {current.get('temp_f', 'N/A')}°F")
        print(f"  Feels like: {current.get('feelslike_f', 'N/A')}°F")
        print(f"  Condition: {current.get('condition', {}).get('text', 'N/A')}")
        print(f"  Humidity: {current.get('humidity', 'N/A')}%")
        print(f"  Wind: {current.get('wind_mph', 'N/A')} mph {current.get('wind_dir', 'N/A')}")
        print(f"  Pressure: {current.get('pressure_mb', 'N/A')} mb")
        print(f"  UV Index: {current.get('uv', 'N/A')}")
        print(f"  Cloud cover: {current.get('cloud', 'N/A')}%")
        print(f"  Visibility: {current.get('vis_miles', 'N/A')} miles")
    elif response.status_code == 400:
        print("Error 400: Bad Request. Please check the city name.")
    elif response.status_code == 401:
        print("Error 401: Unauthorized. Check your API key.")
    elif response.status_code == 404:
        print("Error 404: Not Found. The requested resource could not be found.")
    else:
        print(f"Error: {response.status_code}. Something went wrong.")

if __name__ == '__main__':
    city = input("Enter a city name: ").strip()
    if city:
        get_weather(city)
    else:
        print("No city name provided.")
