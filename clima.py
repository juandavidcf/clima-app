import requests

def get_weather(city):
    api_key = "TU_API_KEY"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric&lang=es"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()

        main = data["main"]
        wind = data["wind"]
        weather = data["weather"][0]["description"]

        return {
            "temperature": main["temp"],
            "humidity": main["humidity"],
            "pressure": main["pressure"],
            "wind_speed": wind["speed"],
            "description": weather
        }
    else:
        return None
