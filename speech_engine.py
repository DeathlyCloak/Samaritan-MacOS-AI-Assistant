from gtts import gTTS
import os
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr

class SpeechEngine:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.fs = 44100  # Sample rate

    def speak(self, text):
        try:
            tts = gTTS(text=text, lang='en')
            tts.save("samaritan.mp3")
            os.system("afplay samaritan.mp3")  # Use 'afplay' for macOS to play audio file
        except Exception as e:
            print(f"Error in text-to-speech: {e}")

    def listen_command(self):
        with sr.Microphone() as source:
            print("Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = self.recognizer.recognize_google(audio)
                print(f"Command received: {command}")
                return command.lower()
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
                self.speak("Sorry, I did not understand that.")
                return None
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                self.speak(f"Could not request results; {e}")
                return None
            except Exception as e:
                print(f"An error occurred: {e}")
                self.speak(f"An error occurred: {e}")
                return None

    def record_audio(self, duration=5):
        try:
            print("Recording...")
            audio = sd.rec(int(duration * self.fs), samplerate=self.fs, channels=1, dtype='int16')
            sd.wait()
            wav.write("recording.wav", self.fs, audio)
            print("Recording saved as recording.wav")
        except Exception as e:
            print(f"Error in audio recording: {e}")
