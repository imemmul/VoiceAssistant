from tkinter.constants import S
from types import coroutine
from pyttsx3 import engine
import speech_recognition as sr
import os
import time
from datetime import date, datetime
from gtts import gTTS
import playsound
import pyttsx3
import pyautogui
from yeelight import discover_bulbs, Bulb

greetings = {"hi" : "Hi",
            "welcome" : "Welcome again Emir",
            "goodmorning" : "Good Morning Emir",
            "goodafternoon" : "Good Afternoon Emir",
            "goodevening" : "Good Evening Emir",
            "goodnight" : "Good Night Emir"
            }

goodbye = {"goodbye" : "Goodbye Emir, Have a good day",
            "todolist" : "Okay Emir, I am done",
            "not_understand": "I didn't understand"}

answers = {"lol" : "Okay, I am opening League of Legends",
            "else" : "Do you need anything else ?",
            "account" : "I am logging into your account",
            "helping" : "How can i help you ?",
            "answer_going" : "I am very well Emir, How are you ?",
            "todolist_add" : "What do yo want to add your to do list ?",
            "event_question" : "what do you want to add as event",
            "off_lights": "Okay, I turned off the lights",
            "on_lights": "Okay, I turned on the lights"}

class to_do():
    def __init__(self, text):
        self.created_date = date.today().strftime("%m/%d/%y")
        self.to_do = text


to_do_list = []
event_list = []

class myBulb():
    def __init__(self):
        self.bulb = Bulb("192.168.1.2")
    def turn_on(self):
        self.bulb.turn_on()
    def turn_off(self):
        self.bulb.turn_off()

class myevent():
    def __init__(self, text):
        self.created_date = date.today().strftime("%m/%d/%y")
        self.myevent = text

myBulb1 = myBulb()

def callback(recognizer, audio):                          # this is called from the background thread
    try:
        print("You said " + recognizer.recognize_google(audio))  # received audio data, now need to recognize it
        if "jarvis" in (recognizer.recognize_google(audio)).lower():
            speak(greetings["hi"] + " , "+ reply_by_time() + answers["helping"])
            execute_commands()
    except sr.UnknownValueError:
        pass

def speak(text):
    tts = pyttsx3.init()
    tts.setProperty("rate", 125)
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
        except sr.UnknownValueError as e:
            pass
    if isinstance(said, str):
        command = said
    return command

def reply_by_time(): # this function provides that program answers different dialogs depends on time.
    h = datetime.today().strftime("%I")
    m = datetime.today().strftime("%M")
    ap = datetime.today().strftime("%p")
    answer_time = ''
    if ap.lower() == "am" and int(h) > 6:
        answer_time = greetings["goodmorning"]
    else:
        if int(h) < 5 and ap.lower() == "pm":
            answer_time = greetings["goodafternoon"]
        elif int(h) > 5 and int(h) < 8 and ap.lower() == "pm":
            answer_time = greetings["goodevening"]
        else:
            answer_time = greetings["goodnight"]
    return answer_time

def execute_commands():  # below commands are basically nested if else statements to get wanted behavior from program.
    t = 5
    while t > 0:
        print("---IN COMMAND LOOP---")
        command = get_audio().lower()
        if len(command) > 2:
            print(f"You said as a command {command}")
            if "morning" in command:
                speak(greetings["goodmorning"])
                t += 1
            elif "evening" in command:
                speak(greetings["goodevening"])
                t += 1
            elif "night" in command:
                speak(greetings["goodnight"])
                t += 1
            elif "afternoon" in command:
                speak(greetings["goodafternoon"])
                t += 1
            elif "lol" in command or "league of legends" in command:
                speak(answers["lol"])
                os.startfile("E:\Riot Games\League of Legends\LeagueClient.exe")
                time.sleep(3)
                speak("Done, " + answers["else"])
                z = 5
                while z > 0:
                    command_account = get_audio().lower()
                    if "login" in command_account or "account" in command_account:
                        speak("Okay, " + answers["account"])
                        pyautogui.write("emirulurak")
                        pyautogui.press('tab')
                        pyautogui.write("EndfireValorant123")
                        pyautogui.press('enter')
                        speak("Done, " + answers["else"])
                        break
                    z -= 1
                t += 1
            elif "quit" in command or "exit" in command:
                speak(goodbye["goodbye"])
                t = 0
                break
            elif "how are you" in command or "it is going" in command:
                speak(answers["answer_going"])
                t += 1
            elif ("to-do list" in command or "to do list" in command) and "add" in command: # i gonna leave this command line for after
                speak(answers["todolist_add"])
                add_to_do()
                speak(goodbye["todolist"])
            elif "event" in command:
                speak(answers["event_question"])
                add_event()
            elif "lights" in command:
                if "on" in command:
                    myBulb1.turn_on()
                    speak(answers["on_lights"])
                elif "off" in command:
                    myBulb1.turn_off()
                    speak(answers["off_lights"])
            elif ("to-do list" in command or "to do list" in command) and "read" in command:
                for index, item in enumerate(to_do_list):
                    if isinstance(item, to_do):
                        speak("Okay Emir, I am reading your to do list   ")
                        speak(f"{index + 1}" + "," + item.to_do)
            else:
                speak(goodbye["not_understand"])
        t -= 1
        time.sleep(1)
    speak(goodbye["goodbye"])

def add_to_do():
    while True:
        command = get_audio().lower()
        print("You said " + command + " as to do")
        if "no" not in command and command != None and "quit" not in command and len(command) > 2:
            mytodo = to_do(command)
            to_do_list.append(mytodo)
            speak(f"Okay, I have added {command} to to do list, Do you want to add anything else ?")
        elif "no" in command or "exit" in command or "quit" in command:
            speak(goodbye["todolist"])
            print(len(to_do_list))
            break

def add_event():
    while True:
        command = get_audio().lower()
        print("You said " + command + "as event")
        if command != "no" and command != None and command != "quit" and len(command) > 2:
            myEvent = myevent(command)
            event_list.append(myEvent)
            speak(f"Okay, I have added {command} as a event, Do you want to add anything else ?")
        elif command == "no" or command == "exit" or command == "quit":
            speak(goodbye["todolist"])
            print(len(event_list))
            break

def listen_in_back():
    while True:
        get_audio()
def main():
    pass

if __name__ == "__main__":
    main()
# here i couldnt implement this code block inside of a function so i did belowings
r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source, duration=0.2)
stop_listening = r.listen_in_background(m, callback=callback)
while True:
    time.sleep(0.1)