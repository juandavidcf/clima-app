from flask import Flask, render_template, request
from Clima import get_weather

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather", methods=["POST"])
def weather():
    city = request.form["city"]
    weather_data = get_weather(city)

    if weather_data:
        return render_template("weather.html", city=city, weather_data=weather_data)
    else:
        return render_template("index.html", error="Ciudad no encontrada")


if __name__ == "__main__":
    app.run(debug=True)