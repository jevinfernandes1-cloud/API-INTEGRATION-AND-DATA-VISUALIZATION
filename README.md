# API-INTEGRATION-AND-DATA-VISUALIZATION

COMPANY: CODTECH IT SOLUTIONS

NAME: JEVIN PAWAN FERNANDES

INTERN ID: CT04DZ1493

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTHOSH

**API Integration and Data Visualization

In today’s digital world, data is often generated and shared through Application Programming Interfaces (APIs). APIs enable applications to interact and exchange information seamlessly, allowing developers to build intelligent and data-driven systems. One of the most widely used APIs for real-time information is the OpenWeatherMap API, which provides weather data for different locations across the globe. In this project, we aim to demonstrate how Python can be used to integrate with such a public API, fetch structured data, process it, and finally visualize the results using powerful libraries like Matplotlib and Seaborn. This project combines the principles of data integration, transformation, and visualization into a single workflow.

Objective

The objective of this project is twofold:

To learn how to access and extract meaningful information from a public API.

To represent this data visually in the form of charts and plots, enabling better insights and analysis.

By the end of this implementation, the user will be able to see real-time weather forecasts, represented through line plots, bar charts, and other visualizations that make raw numerical data much easier to interpret.

Tools and Technologies Used

VS Code: As the Integrated Development Environment (IDE) to write, debug, and run the Python script.

Python 3.x: The core programming language used for API requests, data handling, and visualization.

Requests Library: To send HTTP requests and fetch JSON responses from the OpenWeatherMap API.

Pandas: To process and organize raw API data into structured tabular formats.

Matplotlib & Seaborn: To create insightful and aesthetically appealing visualizations.

OpenWeatherMap API: The public API providing weather forecast data in JSON format.

Step 1: API Integration

The first step in this project involves integrating with the OpenWeatherMap API. To access this API, the user is required to generate a free API key by registering on the OpenWeatherMap platform. Once the key is obtained, it is passed as a parameter in the request URL.

For example, the endpoint used in this project is:

http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric


Here, the forecast API provides weather predictions for the next five days, updated in 3-hour intervals. This means that we receive a rich dataset containing not only temperature but also humidity, wind speed, weather conditions, and other attributes. Using the requests library in Python, we fetch the JSON response and extract only the fields that are most relevant to our analysis, such as temperature, feels-like temperature, humidity, date/time, and weather condition.

Step 2: Data Processing

Once the JSON data is obtained, it needs to be cleaned and structured in a usable format. For this purpose, we use the pandas library to create a DataFrame. Each record includes:

Date and Time: Timestamp converted into a human-readable format.

Temperature: The actual measured temperature in Celsius.

Feels Like Temperature: How the temperature feels considering humidity and wind.

Humidity: Percentage of moisture in the air.

Weather Condition: A categorical variable representing whether it is sunny, cloudy, rainy, etc.

This structured DataFrame provides a tabular view of the forecasted weather data, making it easier to filter, analyze, and visualize.

Step 3: Data Visualization

Raw data, while informative, is not always easy to interpret. Visualizations help us identify patterns and trends quickly. Using Matplotlib and Seaborn, we create a simple weather dashboard with the following components:

Line Chart of Temperature Trends
This chart shows the variation of temperature and feels-like temperature across different time intervals. It provides insights into how the temperature fluctuates throughout the day and highlights periods of extreme weather.

Bar Chart of Humidity with Weather Conditions
This chart shows humidity levels across time, with different colors representing weather conditions such as clear, cloudy, or rainy. This helps in correlating humidity with actual weather states.

The combination of these plots creates a simple dashboard-like visualization, where multiple aspects of the weather forecast can be viewed at once.

Applications

The approach demonstrated in this project has practical applications in several domains:

Weather Forecasting Tools: Can be extended into dashboards for agriculture, logistics, or travel planning.

IoT Devices: Can power smart home devices that react to weather conditions (e.g., turning off sprinklers on rainy days).

Data Science Learning: A perfect example for students learning about real-world data extraction and visualization.

Conclusion

This project showcases the complete pipeline of working with public APIs and visualizing the data in Python. By integrating the OpenWeatherMap API, processing the raw JSON data into a structured DataFrame, and finally visualizing it using Matplotlib and Seaborn, we successfully built a weather forecast dashboard. The project emphasizes the importance of APIs in modern computing and demonstrates how visualization can turn raw data into actionable insights.

In the future, this project can be extended to build interactive dashboards using libraries such as Plotly Dash or Streamlit, which would allow users to search for any city and dynamically view its forecast. Thus, the project not only meets the requirements of API integration and visualization but also opens the door to exciting real-world applications.**

#OUTPUT

<img width="983" height="697" alt="Output task1" src="https://github.com/user-attachments/assets/dc429e09-65b4-4cac-8ff4-8a06b0905b4c" />
