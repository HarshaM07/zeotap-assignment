import requests
import time
from datetime import datetime
from collections import defaultdict
import smtplib
from email.mime.text import MIMEText
import matplotlib.pyplot as plt
import pandas as pd

# Configuration
API_KEY = "803afe71bf9c746fbad115acc5b7f36e"  # Replace with your OpenWeatherMap API key
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
INTERVAL = 300  # Fetch data every 5 minutes
temperature_threshold = 31  # Celsius
alert_count = 0

# In-memory storage for daily weather data
daily_data = defaultdict(list)


def fetch_weather(city):
    """Fetch weather data from OpenWeatherMap API using city name."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()


def kelvin_to_celsius(temp_kelvin):
    """Convert temperature from Kelvin to Celsius."""
    return temp_kelvin - 273.15


def process_weather_data(data):
    """Process the received weather data."""
    dt = datetime.utcfromtimestamp(data["dt"]).date()
    temp_celsius = kelvin_to_celsius(data["main"]["temp"])
    weather_condition = data["weather"][0]["main"]

    daily_data[dt].append(
        {
            "temp": temp_celsius,
            "weather": weather_condition,
        }
    )


def summarize_daily_weather():
    """Summarize daily weather data."""
    summaries = {}
    for date, entries in daily_data.items():
        avg_temp = sum(entry["temp"] for entry in entries) / len(entries)
        max_temp = max(entry["temp"] for entry in entries)
        min_temp = min(entry["temp"] for entry in entries)
        dominant_weather = max(
            set(entry["weather"] for entry in entries), key=lambda x: entries.count(x)
        )

        summaries[date] = {
            "avg_temp": avg_temp,
            "max_temp": max_temp,
            "min_temp": min_temp,
            "dominant_weather": dominant_weather,
        }
    return summaries


def check_alerts(current_temp):
    """Check if current temperature exceeds the defined threshold."""
    global alert_count
    if current_temp > temperature_threshold:
        alert_count += 1
        if alert_count >= 2:  # Trigger alert for two consecutive updates
            trigger_alert()
    else:
        alert_count = 0  # Reset count if below threshold


def trigger_alert():
    """Trigger an alert when threshold is breached."""
    print("Alert! Temperature exceeds the threshold!")
    send_email_alert()


def send_email_alert():
    """Send an email notification."""
    sender_email = "harshamvviet@gmail.com"
    receiver_email = "harsham617@gmail.com"
    password = "qrzt ftzq ucbm noqq"  # Use app password if using Gmail

    msg = MIMEText("Alert: Temperature exceeds the configured threshold!")
    msg["Subject"] = "Weather Alert"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Start TLS for security
            server.login(sender_email, password)  # Log in to your email account
            server.send_message(msg)  # Send the email
            print("Email alert sent.")
    except smtplib.SMTPAuthenticationError:
        print("Failed to authenticate. Check your email and password.")
    except smtplib.SMTPException as e:
        print(f"Failed to send email alert: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def visualize_weather_data():
    """Visualize the daily weather summaries."""
    if not daily_data:
        print("No data to visualize.")
        return

    # Prepare data for visualization
    dates = list(daily_data.keys())
    avg_temps = [
        sum(entry["temp"] for entry in daily_data[date]) / len(daily_data[date])
        for date in dates
    ]

    # Create a DataFrame for easier plotting
    df = pd.DataFrame({"Date": dates, "Avg Temp (°C)": avg_temps})
    df["Date"] = pd.to_datetime(df["Date"])

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(
        df["Date"],
        df["Avg Temp (°C)"],
        marker="o",
        linestyle="-",
        color="b",
        label="Average Temperature",
    )
    plt.title("Daily Average Temperature")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    """Main function to run the weather monitoring system."""
    while True:
        for city in CITIES:
            weather_data = fetch_weather(city)
            if weather_data.get("cod") == 200:  # Check for successful response
                process_weather_data(weather_data)
                current_temp = kelvin_to_celsius(weather_data["main"]["temp"])
                check_alerts(current_temp)
                # Trigger alert immediately for testing
                # trigger_alert()  # Uncomment to test email notification

            else:
                print(f"Error fetching data for {city}: {weather_data.get('message')}")

        daily_summary = summarize_daily_weather()
        print("\nDaily Weather Summaries:")
        for date, summary in daily_summary.items():
            print(
                f"{date}: Avg Temp: {summary['avg_temp']:.2f}°C, Max Temp: {summary['max_temp']:.2f}°C, Min Temp: {summary['min_temp']:.2f}°C, Dominant Weather: {summary['dominant_weather']}"
            )

        # Visualize the weather data
        visualize_weather_data()

        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
