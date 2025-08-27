
# JARVIS - Smart AI Assistant (Basic Functional Skeleton)

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import subprocess
import requests
import json
import pyautogui
import smtplib
import time

# Initialize the TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Speak Function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen Function
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-US')
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""

# Greet Function
def greet():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I help you today?")

# Weather Info
def get_weather(city="New York"):
    api_key = "YOUR_OPENWEATHER_API_KEY"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        speak(f"The weather in {city} is {weather} with a temperature of {temp} degrees Celsius.")
    else:
        speak("Unable to get weather information.")

# Web Search
def search_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

# Open App
def open_app(app_name):
    if "chrome" in app_name:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    elif "notepad" in app_name:
        subprocess.Popen(['notepad.exe'])
    # Add more apps as needed

# Tell Date and Time
def tell_time():
    now = datetime.datetime.now()
    speak(f"Current time is {now.strftime('%H:%M')} and date is {now.strftime('%A, %B %d, %Y')}")

# Main Jarvis Loop
def run_jarvis():
    greet()
    while True:
        command = listen()
        if not command:
            continue

        if "weather" in command:
            get_weather("your_city")
        elif "time" in command or "date" in command:
            tell_time()
        elif "open" in command:
            open_app(command)
        elif "search" in command:
            search_google(command.replace("search", ""))
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I can search that for you.")
            search_google(command)

if __name__ == "__main__":
    run_jarvis()
