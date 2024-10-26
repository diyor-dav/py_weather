from flask import Flask, request, render_template
from weather import get_weather
from waitress import serve

app = Flask(__name__) # create an instance of the Flask class

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/weather')
def get_wether():
    city = request.args.get("city")
    if not bool(city.strip()):
        city = "Tashkent"
        
    weather_data = get_weather(city)
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp= f"{weather_data['main']['temp']:.1f}",
        feels_like= f"{weather_data['main']['feels_like']:.1f}",
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)