"""Task Manager - Holds all the commands eligble in the AI"""

import webbrowser
import pyautogui
import os

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
        elif 'play' in command:
            self.play_song(command)
        elif 'cpu' in command:
            self.report_cpu_usage()
        elif 'battery' in command:
            self.report_battery_status()
        elif 'joke' in command:
            self.tell_joke()
        elif 'logout' in command:
            self.logout()
        elif 'shutdown' in command:
            self.shutdown()
        elif 'restart' in command:
            self.restart()
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
        music_dir = '/Users/Mr.Finch/Desktop/CD Music'
        songs = os.listdir(music_dir)
        os.PathLike(os.path.join(music_dir, songs[33]))

    def report_cpu_usage(self):
        usage = self.system_monitor.get_cpu_usage()
        self.speech_engine.speak(f"CPU usage is at {usage} percent")

    def report_battery_status(self):
        battery_status = self.system_monitor.get_battery_status()
        self.speech_engine.speak(f"Battery is at {battery_status} percent")

    def tell_joke(self):
        joke = self.joke_teller.tell_joke()
        self.speech_engine.speak(joke)

# New function - Remember what I said and place it into a text and also able to read back what I asked to remember
   #  elif 'remember that' in query:
    #        speak("What should I remember sir?")
     #       data = takeCommand()
      #      speak("remembering" + data)
       #     remember = open('data.txt', 'w')
        #    remember.write(data)
         #   remember.close()
       # elif 'do you know anything' in query:
        #    remember = open('data.txt', 'r')
         #   speak("you said to remember that" + remember.read())
 
    def logout(self):
        os.system("shutdown -1")
    def shutdown(self):
        os.system("shutdown /s /t 1")
    def restart(self):
        os.system('shutdown /r /t 1')