import streamlit as st
import requests

st.title("🌤️ Simple Weather App")

# Function to fetch weather data from OpenWeatherMap
def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"} # units=metric for Celsius
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# User input
city = st.text_input("Enter city name:", "")
api_key = "ea6bbe88da2c0c9b22f8efe52c4cb6ca" # Replace with your actual API key

if st.button("Check Weather") and city:
    with st.spinner("Fetching data..."):
        weather_data = get_weather(city, api_key)
        if weather_data:
            # Extract relevant information
            temp = weather_data["main"]["temp"]
            desc = weather_data["weather"][0]["description"].capitalize()
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]

            # Display the results
            st.subheader(f"Weather in {city}")
            st.metric("Temperature", f"{temp}°C", None)
            st.write(f"**Condition:** {desc}")
            st.write(f"**Humidity:** {humidity}%")
            st.write(f"**Wind Speed:** {wind_speed} m/s")
        else:
            st.error("City not found or error fetching weather data. Please try a more specific name (e.g., 'Paris, Texas').")
elif st.button("Check Weather") and not city:
    st.warning("Please enter a city name.")

