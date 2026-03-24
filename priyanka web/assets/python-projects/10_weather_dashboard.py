"""
🌤️ Weather Dashboard (Simulated)
A simulated weather app that displays weather info for various cities.
Author: Priyanka
"""

import random
from datetime import datetime, timedelta

# Simulated weather data
CITIES = {
    "Mumbai": {"lat": 19.07, "lon": 72.87, "climate": "tropical"},
    "Delhi": {"lat": 28.61, "lon": 77.20, "climate": "semi-arid"},
    "Bangalore": {"lat": 12.97, "lon": 77.59, "climate": "tropical-savanna"},
    "Pune": {"lat": 18.52, "lon": 73.85, "climate": "semi-arid"},
    "Kolkata": {"lat": 22.57, "lon": 88.36, "climate": "tropical-wet"},
    "Chennai": {"lat": 13.08, "lon": 80.27, "climate": "tropical-wet"},
    "Hyderabad": {"lat": 17.38, "lon": 78.48, "climate": "semi-arid"},
    "Jaipur": {"lat": 26.91, "lon": 75.78, "climate": "semi-arid"},
}

CONDITIONS = [
    ("☀️ Sunny", "Clear skies"),
    ("⛅ Partly Cloudy", "Some clouds"),
    ("☁️ Cloudy", "Overcast"),
    ("🌧️ Rainy", "Light showers"),
    ("⛈️ Thunderstorm", "Heavy rain with thunder"),
    ("🌤️ Mostly Sunny", "A few clouds"),
    ("🌫️ Foggy", "Low visibility"),
    ("💨 Windy", "Strong winds"),
]

def generate_weather(city_name, city_info):
    climate = city_info["climate"]
    
    # Base temperature by climate
    base_temps = {
        "tropical": random.uniform(28, 36),
        "semi-arid": random.uniform(25, 40),
        "tropical-savanna": random.uniform(22, 32),
        "tropical-wet": random.uniform(26, 34),
    }
    
    temp = base_temps.get(climate, random.uniform(20, 35))
    humidity = random.randint(30, 90)
    wind_speed = random.uniform(5, 30)
    condition = random.choice(CONDITIONS)
    feels_like = temp + random.uniform(-3, 3)
    uv_index = random.randint(1, 11)
    visibility = random.uniform(5, 15)
    
    return {
        "city": city_name,
        "temp": round(temp, 1),
        "feels_like": round(feels_like, 1),
        "humidity": humidity,
        "wind": round(wind_speed, 1),
        "condition": condition[0],
        "description": condition[1],
        "uv_index": uv_index,
        "visibility": round(visibility, 1),
        "lat": city_info["lat"],
        "lon": city_info["lon"],
    }

def display_weather(data):
    print(f"\n{'═' * 48}")
    print(f"  {data['condition']}  Weather for {data['city']}")
    print(f"{'═' * 48}")
    print(f"  🌡️ Temperature:  {data['temp']}°C")
    print(f"  🤔 Feels Like:   {data['feels_like']}°C")
    print(f"  💧 Humidity:      {data['humidity']}%")
    print(f"  💨 Wind Speed:    {data['wind']} km/h")
    print(f"  ☀️ UV Index:      {data['uv_index']}/11")
    print(f"  👁️ Visibility:    {data['visibility']} km")
    print(f"  📝 Description:   {data['description']}")
    print(f"  📍 Coordinates:   {data['lat']}°N, {data['lon']}°E")
    print(f"  🕐 Updated:       {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'═' * 48}")
    
    # Clothing suggestion
    if data['temp'] > 35:
        print("  👕 Suggestion: Light clothes, stay hydrated! 💧")
    elif data['temp'] > 25:
        print("  👕 Suggestion: Comfortable cotton wear.")
    elif data['temp'] > 15:
        print("  🧥 Suggestion: Carry a light jacket.")
    else:
        print("  🧣 Suggestion: Wear warm clothes!")

def show_forecast(city_name, city_info):
    print(f"\n📅 5-Day Forecast for {city_name}:")
    print(f"{'─' * 48}")
    
    for i in range(5):
        day = datetime.now() + timedelta(days=i + 1)
        data = generate_weather(city_name, city_info)
        day_name = day.strftime("%a %d %b")
        print(f"  {day_name:<12}  {data['condition']:<20}  {data['temp']}°C  💧{data['humidity']}%")
    
    print(f"{'─' * 48}")

def compare_cities():
    print(f"\n{'═' * 55}")
    print(f"  📊 City Comparison")
    print(f"{'═' * 55}")
    print(f"  {'City':<12} {'Temp':>6} {'Humidity':>10} {'Wind':>8} {'Condition'}")
    print(f"  {'─'*12} {'─'*6} {'─'*10} {'─'*8} {'─'*15}")
    
    for city_name, city_info in CITIES.items():
        data = generate_weather(city_name, city_info)
        print(f"  {city_name:<12} {data['temp']:>5.1f}° {data['humidity']:>8}% {data['wind']:>6.1f} {data['condition']}")
    
    print(f"{'═' * 55}")

def weather_dashboard():
    print("=" * 40)
    print("   🌤️ WEATHER DASHBOARD")
    print("=" * 40)
    print("   (Simulated — no API needed!)")
    
    while True:
        print("\n📂 Menu:")
        print("1. Check city weather")
        print("2. 5-day forecast")
        print("3. Compare all cities")
        print("4. Exit")
        
        choice = input("\n👉 Choose (1-4): ").strip()
        
        if choice == '1' or choice == '2':
            print("\n🏙️ Available cities:")
            cities = list(CITIES.keys())
            for i, city in enumerate(cities, 1):
                print(f"   {i}. {city}")
            
            try:
                idx = int(input("\n👉 Pick a city (1-8): ")) - 1
                city_name = cities[idx]
                city_info = CITIES[city_name]
            except (ValueError, IndexError):
                print("❌ Invalid choice!")
                continue
            
            if choice == '1':
                data = generate_weather(city_name, city_info)
                display_weather(data)
            else:
                show_forecast(city_name, city_info)
        
        elif choice == '3':
            compare_cities()
        
        elif choice == '4':
            print("\n👋 Stay weather-aware! ☀️")
            break
        
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    weather_dashboard()
