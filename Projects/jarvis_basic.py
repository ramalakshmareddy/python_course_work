import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os

# Initialize recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def talk(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '').strip()
                print("Command:", command)
                return command
            else:
                return ""
    except:
        return ""

def run_jarvis():
    command = take_command()
    if not command:
        talk("Please start your command with 'Jarvis'")
        return

    if 'play' in command:
        song = command.replace('play', '')
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'Current time is {time}')

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, sentences=1)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'open notepad' in command:
        os.system('notepad')

    elif 'open chrome' in command:
        os.system('start chrome')

    elif 'exit' in command or 'stop' in command:
        talk("Goodbye!")
        exit()

    else:
        talk("Sorry, I didn't understand that.")

# Keep Jarvis running in a loop
while True:
    run_jarvis()
