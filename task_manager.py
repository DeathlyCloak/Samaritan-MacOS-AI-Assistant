import webbrowser
import pyautogui
import os
from playsound import playsound

class TaskManager:
    def __init__(self, speech_engine, system_monitor, joke_teller):
        self.speech_engine = speech_engine
        self.system_monitor = system_monitor
        self.joke_teller = joke_teller

    def execute(self, command):
        if 'search' in command:
            self.search_web(command)
        elif 'screenshot' in command:
            self.take_screenshot()
        elif 'music' in command:
            self.play_song(command)
        elif 'cpu' in command:
            self.report_cpu_usage()
        elif 'battery' in command:
            self.report_battery_status()
        elif 'joke' in command:
            self.tell_joke()
        elif 'remember' in command:
            self.remember()
        elif 'recall' in command:
            self.recall()
        else:
            self.speech_engine.speak("Sorry, I didn't understand that command.")

    def search_web(self, command):
        self.speech_engine.speak("What should I search for?")
        query = self.speech_engine.listen_command()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            self.speech_engine.speak(f"Here are the search results for {query}")

    def take_screenshot(self):
        img = pyautogui.screenshot()
        img.save('screenshot.png')
        self.speech_engine.speak("Screenshot has been taken.")

    def play_song(self, command):
        self.speech_engine.speak("Due to Apple Music and Apple wanting more money I can not play your music. Sorry Sir")

    def report_cpu_usage(self):
        usage = self.system_monitor.get_cpu_usage()
        self.speech_engine.speak(f"CPU usage is at {usage} percent")

    def report_battery_status(self):
        battery_status = self.system_monitor.get_battery_status()
        self.speech_engine.speak(f"Battery is at {battery_status} percent")

    def tell_joke(self):
        joke = self.joke_teller.tell_joke()
        self.speech_engine.speak(joke)

    def remember(self):
        self.speech_engine.speak("What should I remember?")
        data = self.speech_engine.listen_command()
        if data:
            self.speech_engine.speak("Remembering " + data)
            with open('remember.txt', 'w') as remember_file:
                remember_file.write(data)
            self.speech_engine.speak("I have remembered that.")

    def recall(self):
        try:
            with open('remember.txt', 'r') as remember_file:
                data = remember_file.read()
            if data:
                self.speech_engine.speak("You asked me to remember: " + data)
            else:
                self.speech_engine.speak("There is nothing to recall.")
        except FileNotFoundError:
            self.speech_engine.speak("There is nothing to recall.")
