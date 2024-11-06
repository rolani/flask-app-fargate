"""Module providing random choices."""
from random import choices
from flask import render_template
from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

def random_fruit():
    """Returns random fruit"""

    fruits = [
    "apple", "cherry", "orange", "banana", "pawpaw", "grapes", 
    "mango", "pineapple", "strawberry", "blueberry", "blackberry", 
    "watermelon", "kiwi", "peach", "plum", "apricot", 
    "pomegranate", "guava", "fig", "dragon fruit", 
    "lychee", "raspberry", "coconut", "lime", "lemon", 
    "grapefruit", "nectarine", "pear", "passion fruit", "jackfruit"
    ]
    return choices(fruits)


@app.route("/random")
def fruit():
    """Return random fruit"""

    my_fruit = random_fruit()
    return render_template("index.html", title="Random Fruit", fruit=my_fruit)

# Define a mapping of cities to timezones
city_timezones = {
    "New York": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney",
    "Toronto": "America/Toronto",
    "Paris": "Europe/Paris",
    "Mumbai": "Asia/Kolkata",
    "Los Angeles": "America/Los_Angeles",
    "Chicago": "America/Chicago",
    "Mexico City": "America/Mexico_City",
    "Berlin": "Europe/Berlin",
    "Moscow": "Europe/Moscow",
    "Beijing": "Asia/Shanghai",
    "Hong Kong": "Asia/Hong_Kong",
    "Johannesburg": "Africa/Johannesburg",
    "Buenos Aires": "America/Argentina/Buenos_Aires",
    "Cairo": "Africa/Cairo",
    "Rome": "Europe/Rome",
    "Singapore": "Asia/Singapore",
    "Seoul": "Asia/Seoul",
    "Bangkok": "Asia/Bangkok",
    "Vienna": "Europe/Vienna",
    "Istanbul": "Europe/Istanbul",
    "Zurich": "Europe/Zurich",
    "Stockholm": "Europe/Stockholm",
    "Sao Paulo": "America/Sao_Paulo",
    "Jakarta": "Asia/Jakarta",
    "Helsinki": "Europe/Helsinki",
    "Dubai": "Asia/Dubai"
}

@app.route('/current-time', methods=['GET'])
def get_current_time():
    city = request.args.get('city')
    
    if not city:
        return jsonify({"error": "Please provide a city name."}), 400
    
    timezone = city_timezones.get(city.title())
    
    if not timezone:
        return jsonify({"error": f"Timezone for {city} not found."}), 404
    
    city_time = datetime.now(pytz.timezone(timezone))
    formatted_time = city_time.strftime("%Y-%m-%d %H:%M:%S")
    
    return jsonify({
        "city": city,
        "current_time": formatted_time
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)