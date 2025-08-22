# API-INTEGRATION-AND-DATA-VISUALIZATION

COMPANY: CODTECH IT SOLUTIONS

NAME: JEVIN PAWAN FERNANDES

INTERN ID: CT04DZ1493

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTHOSH

**Project Description

For this project, I wanted to explore how we can connect to real-world data using Python and then make sense of it through graphs. The idea was to fetch live data from a public API and turn it into clear visualizations instead of just plain numbers. After checking a few options, I decided to use the OpenWeatherMap API, because weather data is something we can all relate to and it updates in real-time.

The overall goal was:

Connect to the API and fetch weather forecast data.

Process the data into a structured format.

Visualize it with charts using Python libraries like Matplotlib and Seaborn.

Tools I Used

VS Code: I did all my coding in Visual Studio Code because it’s simple and has a built-in terminal to run Python scripts.

Python 3: The programming language for the project.

Requests: To send a request to the API and collect the response.

Pandas: To structure and clean the raw JSON response.

Matplotlib and Seaborn: To create graphs and visual dashboards.

OpenWeatherMap API: The source of real-time weather forecast data.

How It Works

The way the project works is pretty straightforward:

Fetching Data:
First, I made an HTTP request to the OpenWeatherMap API with my API key and a city name (for example, Mumbai). The API returns a JSON response containing the 5-day weather forecast in 3-hour intervals.

Processing the Data:
The raw API response is just a big JSON file, which is hard to read. So I extracted only the important information:

Date and Time

Temperature

Feels Like temperature

Humidity

Weather condition (like clear, cloudy, or rainy)

I stored this into a pandas DataFrame, which makes it neat and tabular, like an Excel sheet.

Visualizing the Data:
Once the data was ready, I made two main visualizations:

A line chart to show how temperature and “feels like” values change over time. This helps see trends like which times of day are hotter or cooler.

A bar chart to show humidity levels, color-coded by weather condition (rain, clouds, etc.). This makes it easy to connect humidity with the type of weather.

Both charts together act like a small dashboard.

Why This is Useful

This project isn’t just an academic exercise — it can be useful in many situations. For example:

A traveler can quickly see how the weather changes across the week.

Farmers could use the humidity and rainfall predictions.

Businesses like logistics or shipping can use it for planning deliveries.

Instead of just looking at raw weather numbers, the graphs make the information much easier to understand.

My Experience

Honestly, working with an API for the first time felt a little intimidating because of the JSON response. But once I figured out how to pick only the fields I needed, it became fun. Using pandas made the data handling way simpler, and plotting with Seaborn gave professional-looking charts with very little code.

Running everything in VS Code also made it smooth — I could quickly test, debug, and then see my charts pop up in a new window.

Conclusion

In short, my project shows how Python can connect to a live API, process real-world data, and turn it into visual insights. Instead of manually checking the weather forecast, my script automatically fetches the data and creates a mini weather dashboard.

It made me realize how powerful APIs are for bringing in real-time data and how important visualization is for actually understanding that data.

In the future, I would like to make this even more interactive, maybe using Streamlit or Plotly Dash so that users can type any city name and instantly see its forecast dashboard.**

#OUTPUT

<img width="983" height="697" alt="Output task1" src="https://github.com/user-attachments/assets/dc429e09-65b4-4cac-8ff4-8a06b0905b4c" />
