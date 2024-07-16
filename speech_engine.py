"""Speech Eninge"""

from gtts import gTTS
import os
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr

class SpeechEngine:
    def __init__(self):
        self.fs = 44100  # Sample rate
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        try:
            tts = gTTS(text=text, lang='en', tld='com.au')  # Can change the language here 
            tts.save("samaritan.mp3")
            os.system("afplay samaritan.mp3")  # Use 'afplay' for macOS to play audio file
        except Exception as e:
            print(f"Error in text-to-speech: {e}")

    def listen_command(self, duration=5):
        try:
            print("Listening...")
            audio = sd.rec(int(duration * self.fs), samplerate=self.fs, channels=1, dtype='int16')
            sd.wait()  # Wait until recording is finished
            wav.write("recording.wav", self.fs, audio)
            print("Recording saved as recording.wav")
            
            # Use speech recognition to convert the audio to text
            with sr.AudioFile("recording.wav") as source:
                audio_data = self.recognizer.record(source)
                command = self.recognizer.recognize_google(audio_data)
                print(f"Recognized command: {command}")
                return command.lower()  # Return the recognized command in lowercase
        except Exception as e:
            print(f"Error in audio recording or recognition: {e}")
            return None
