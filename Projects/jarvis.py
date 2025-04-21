import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import os

# Set up speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Voice Output
def talk(text):
    output_label.config(text=text)
    engine.say(text)
    engine.runAndWait()

# Get weather info
def get_weather(city):
    API_KEY = "your_openweather_api_key_here"
 # Replace with your API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url)
    data = res.json()
    if data.get("main"):
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"The temperature in {city} is {temp}°C with {desc}"
    else:
        return "City not found."

# Listen for commands
def take_command():
    try:
        with sr.Microphone() as source:
            command_label.config(text="Listening...")
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '').strip()
            command_label.config(text=f"You said: {command}")
            return command
    except:
        command_label.config(text="Sorry, I didn't catch that.")
        return ""

# Handle commands
def run_jarvis():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'The current time is {time}')

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, sentences=1)
        talk(info)

    elif 'weather' in command:
        city = command.replace('weather in', '').strip()
        weather_info = get_weather(city)
        talk(weather_info)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)

    elif 'open notepad' in command:
        os.system("notepad.exe")

    elif 'open chrome' in command:
        os.system("start chrome")

    elif 'exit' in command:
        talk("Goodbye!")
        root.destroy()

    else:
        talk("Sorry, I didn't understand that.")

# GUI Setup
root = tk.Tk()
root.title("Jarvis - Virtual Assistant")
root.geometry("500x400")
root.configure(bg="#2e3f4f")

listener = sr.Recognizer()

title = tk.Label(root, text="🎙️ Jarvis - Virtual Assistant", font=("Helvetica", 20, "bold"), bg="#2e3f4f", fg="white")
title.pack(pady=20)

command_label = tk.Label(root, text="", font=("Arial", 12), bg="#2e3f4f", fg="lightgray")
command_label.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 12, "italic"), wraplength=400, bg="#2e3f4f", fg="white")
output_label.pack(pady=10)

btn_frame = tk.Frame(root, bg="#2e3f4f")
btn_frame.pack(pady=20)

start_btn = tk.Button(btn_frame, text="Start Listening", command=run_jarvis, bg="#00aaff", fg="white", font=("Arial", 12), width=15)
start_btn.grid(row=0, column=0, padx=10)

exit_btn = tk.Button(btn_frame, text="Exit", command=root.destroy, bg="#ff4444", fg="white", font=("Arial", 12), width=10)
exit_btn.grid(row=0, column=1)

root.mainloop()
