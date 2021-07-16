from tkinter.constants import S
from pyttsx3 import engine
import speech_recognition as sr
import os
import time
from gtts import gTTS
import playsound
import pyttsx3
import pyautogui

greetings = {"hi" : "Hi Emir, How can i help you ?",
            "welcome" : "Welcome again Emir",
            "goodmorning" : "Good Morning Emir",
            "goodafternoon" : "Good Afternoon Emir",
            "goodevening" : "Good Evening Emir",
            "goodnight" : "Good Night Emir, Have a nice sleep."
            }

goodbye = {"goodbye" : "Goodbye Emir, Have a good day."}


def callback(recognizer, audio):                          # this is called from the background thread
    try:
        print("You said " + recognizer.recognize_google(audio))  # received audio data, now need to recognize it
        if "darling" in recognizer.recognize_google(audio):
            speak(greetings["hi"])
            check_command()
    except sr.UnknownValueError:
        pass

def speak(text):
    tts = pyttsx3.init()
    tts.setProperty("rate", 150)
    voices = tts.getProperty('voices')
    tts.setProperty('voice', voices[1].id)
    tts.say(text)
    tts.runAndWait()
    tts.stop()

def get_audio():
    command = ""
    r = sr.Recognizer()
    with sr.Microphone() as src:
        r.adjust_for_ambient_noise(src, duration=0.2)
        audio = r.listen(src)
        said = ''
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            speak("I didn't understand you.")
    if isinstance(said, str):
        command = said
    return command

def check_command():
    while True:
        print(1)
        command = get_audio().lower()
        print(f"You said as a command {command}")
        if "good morning" in command:
            speak(greetings["goodmorning"])
        elif "good evening" in command:
            speak(greetings["goodevening"])
        elif "good night" in command:
            speak(greetings["goodnight"])
        elif "goodafternoon" in command:
            speak(greetings["goodafternoon"])
        elif "hi" in command:
            speak(greetings["welcome"])
        elif "lol" in command or "league of legends" in command:
            speak("Okay, I am opening League of Legends.")
            os.startfile("E:\Riot Games\League of Legends\LeagueClient.exe")
            speak("Done, Do you want anything else ?")
            command_account = get_audio().lower()
            if "login" in command_account or "account" in command_account:
                speak("Okay, I am logging into your account.")
                pyautogui.write("emirulurak", interval=0.1)
                pyautogui.press('tab')
                pyautogui.write("EndfireValorant123", interval=0.1)
                pyautogui.press('enter')
                speak("Done")
        elif "quit" in command or "exit" in command:
            speak(goodbye["goodbye"])
            stop_listening(wait_for_stop=False)
            break
        time.sleep(0.5)


def main():
    pass

if __name__ == "__main__":
    main()

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source, duration=0.2)
stop_listening = r.listen_in_background(m, callback=callback)
while True:
    time.sleep(0.1)