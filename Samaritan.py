import speech_engine
import task_manager
import system_monitor
import joke_teller
from datetime import datetime

class Samaritan:
    def __init__(self):
        self.speech_engine = speech_engine.SpeechEngine()
        self.system_monitor = system_monitor.SystemMonitor()
        self.joke_teller = joke_teller.JokeTeller()
        self.task_manager = task_manager.TaskManager(self.speech_engine, self.system_monitor, self.joke_teller)

    def greet_user(self):
        now = datetime.now()
        current_hour = now.hour

        if 0 <= current_hour < 12:
            greeting = "Good morning"
        elif 12 <= current_hour < 17:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"

        cpu_usage = self.system_monitor.get_cpu_usage()
        battery_status = self.system_monitor.get_battery_status()

        greeting_message = (f"{greeting}! I am Samaritan, your personal AI assistant. "
                            f"Your CPU usage is at {cpu_usage} percent and your battery is at {battery_status} percent. "
                            "Everything is fully operational and ready for the next project.")

        self.speech_engine.speak(greeting_message)

    def run(self):
        self.greet_user()
        while True:
            command = self.speech_engine.listen_command()
            if command:
                self.task_manager.execute(command)

if __name__ == "__main__":
    samaritan = Samaritan()
    samaritan.run()
