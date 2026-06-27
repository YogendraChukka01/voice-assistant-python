"""Voice Assistant for Desktop Automation.

Project: Voice Assistant for Desktop Automation
Author: Yogendra Chukka
Version: 1.0.0
Description: A Python-based desktop voice assistant for speech recognition,
text-to-speech, browser automation, and keyboard automation.
Year: 2024
"""

import datetime
import os
import webbrowser
from time import sleep

import pyautogui
import pyttsx3
import pywhatkit
import speech_recognition as sr

PASSWORD = "example_password_123"

engine = pyttsx3.init()


def speak(text):
    """Speak the provided text."""
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen for user speech and return recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("User said:", query)
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        query = None
    except sr.RequestError as e:
        print("Sorry, could not request results; {0}".format(e))
        query = None

    return query


def wish():
    """Greet the user according to the current time."""
    hour = datetime.datetime.now().hour
    current_time = datetime.datetime.now().strftime("%I:%M %p")

    if hour < 12:
        greeting = "GOOD MORNING SIR, I AM SREE YOUR VIRTUAL ASSISTANT"
    elif hour < 15:
        greeting = "GOOD AFTERNOON SIR, I AM SREE YOUR VIRTUAL ASSISTANT"
    elif hour < 18:
        greeting = "GOOD EVENING SIR, I AM SREE YOUR VIRTUAL ASSISTANT"
    else:
        greeting = "HELLO SIR, I AM YOUR SREE YOUR VIRTUAL ASSISTANT"

    speak(greeting)
    print(greeting)
    speak(f"sir current time is {current_time}")


def open_website(query):
    """Open a website based on the recognized query text."""
    target = query.replace("website", "").strip()
    if not target:
        return

    speak(f"opening {target} sir")
    print(f"opening {target} sir")
    webbrowser.open(f"https://www.{target}.com")
    sleep(0.5)


def open_youtube():
    """Open YouTube in the default browser."""
    speak("opening youtube sir")
    print("opening youtube sir")
    webbrowser.open("https://www.youtube.com")
    sleep(0.5)


def type_in_notepad():
    """Type text into Notepad and respond to simple voice commands."""
    speak("sir, opening Notepad sir")
    print("This function is used to write or type in Notepad.")

    try:
        os.startfile(
            "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
        )
    except Exception as exc:
        print("Notepad could not be opened:", exc)
        speak("Sorry sir, I could not open Notepad.")
        return

    sleep(1)
    while True:
        text = listen()
        if not text:
            continue

        if "stop writing" in text.lower() or "exit" in text.lower():
            speak("ok sir, I stopped writing")
            print("ok sir , I stopped writing")
            break

        pyautogui.write(text)

    while True:
        save = listen()
        if not save:
            continue

        save_text = save.lower()
        if "save" in save_text:
            pyautogui.hotkey("ctrl", "s")
            pyautogui.hotkey("ctrl", "a")
            pyautogui.press("backspace")
            filename = listen()
            if filename:
                pyautogui.write(filename)
                pyautogui.press("enter")
            sleep(0.3)
        elif "copy" in save_text:
            pyautogui.hotkey("ctrl", "a")
            pyautogui.hotkey("ctrl", "c")
            sleep(0.5)
        elif "paste" in save_text:
            pyautogui.hotkey("ctrl", "v")
            sleep(0.1)
        elif "exit" in save_text:
            speak("ok sir, exiting notepad menu")
            break
        elif "clear" in save_text:
            pyautogui.hotkey("ctrl", "a")
            pyautogui.press("backspace")
            sleep(0.3)
        elif "create" in save_text:
            pyautogui.hotkey("alt", "f")
            pyautogui.hotkey("alt", "n")
            sleep(0.5)
        else:
            speak("exiting notepad and saving")
            pyautogui.hotkey("ctrl", "n")
            pyautogui.hotkey("ctrl", "s")
            break


def main():
    """Run the voice assistant main loop."""
    speak("This file is password protected sir. Please enter the password sir")
    print("This file is password protected sir. Please enter the password sir")
    pass_in = input("Enter the password sir :\n")

    if PASSWORD != pass_in:
        speak("Sorry sir, the password is incorrect.")
        print("Sorry sir, the password is incorrect.")
        return

    speak("Welcome I am sree your virtual assistant sir")
    print("Welcome I am sree your virtual assistant sir")
    wish()
    speak("I am sree your Virtual Assistant sir")
    sleep(0.5)

    while True:
        query = listen()
        if not query:
            continue

        query = query.lower()
        if "time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"sir current time is {current_time}")
            print(f"sir current time is {current_time}")
            sleep(0.5)
        elif "youtube" in query:
            open_youtube()
        elif "website" in query:
            open_website(query)
        elif "type" in query:
            type_in_notepad()
        else:
            speak("sir something problem sir")


if __name__ == "__main__":
    main()
