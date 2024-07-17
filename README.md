# Samaritan AI Assistant

## Overview

Samaritan is a personal AI assistant that performs various tasks such as web searches, system monitoring, and telling jokes. This project demonstrates skills in Python and uses several libraries for text-to-speech, speech recognition, and system control.

## Features

- **Text-to-Speech (TTS)**: Converts text to speech using the `gTTS` library.
- **Speech Recognition**: Recognizes speech commands using the `speech_recognition` library.
- **System Monitoring**: Monitors system performance and battery status using `psutil`.
- **Joke Telling**: Tells jokes using the `pyjokes` library.
- **Task Management**: Executes various tasks based on voice commands, such as web searches, screenshots, and more.

## Requirements

- Python 3.11

### Required Packages

To install the required packages, use pip:

```bash
pip install gTTS sounddevice numpy scipy speech_recognition psutil pyjokes pyautogui playsound