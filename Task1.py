import requests
import matplotlib.pyplot as plt
import seaborn as sns

# city and API key
city = "Mangalore"
API_KEY = "2ec441e03787ddd96f92d06909906b6b"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

#get data
response = requests.get(url)
data = response.json()

# Information required
temperature = data['main']['temp']
humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind_speed = data['wind']['speed']

weather_data = {
    'Temperature (°C)': temperature,
    'Humidity (%)': humidity,
    'Pressure (hPa)': pressure,
    'Wind Speed (m/s)': wind_speed
}

# visual display
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))

bars = sns.barplot(
    x=list(weather_data.keys()),
    y=list(weather_data.values()),
    palette=["#4db8ff", "#85e085", "#ffcc66", "#ff6666"]
)

# value label on top of each bar
for bar in bars.patches:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height,
             f'{height:.1f}', ha='center', va='bottom')

# chart
plt.title(f"Current weather in {city}")
plt.ylabel("Values")
plt.tight_layout()
plt.show()
