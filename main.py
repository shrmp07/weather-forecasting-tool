import requests

API_KEY = "cdc0c9ab896d69207da94caa76c432da"  #OpenWeatherMap API key

def get_weather(city):
    try:
        # Making a request to the OpenWeatherMap API
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        )
        response.raise_for_status()  # Raise an exception if the request was unsuccessful

        # Parsing the weather data
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        # Displaying the weather forecast
        print(f"Weather forecast for {city}:")
        print(f"Description: {weather}")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching the weather data.")
        print(e)

if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)
