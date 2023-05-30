import requests
import json

API_KEY = "ee0c0e493ff2ccd205a42dab4250f10d"  


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if status code is not 2xx
        data = response.json()

        # Extract relevant weather information
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        # Print the weather forecast
        print(f"Weather forecast for {city}:")
        print(f"Description: {weather}")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
    except KeyError:
        print(f"Could not retrieve weather data for {city}. Please check the city name.")


def main():
    city = input("Enter a city name: ")
    get_weather(city)


if __name__ == "__main__":
    main()
