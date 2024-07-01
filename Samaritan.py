"""Main File for AI Assistant Samaritan"""

import speech_engine
import task_manager
import system_monitor
import joke_teller

class Samaritan:
    def __init__(self):
        self.speech_engine = speech_engine.SpeechEngine()
        self.system_monitor = system_monitor.SystemMonitor()
        self.joke_teller = joke_teller.JokeTeller()
        self.task_manager = task_manager.TaskManager(self.speech_engine, self.system_monitor, self.joke_teller)

    def run(self):
        self.speech_engine.speak("Hello! I am Samaritan, your personal AI assistant.")
        while True:
            command = self.speech_engine.listen_command()
            if command:
                self.task_manager.execute(command)

if __name__ == "__main__":
    samaritan = Samaritan()
    samaritan.run()
