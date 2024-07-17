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


# Usage

### Clone the repository:
git clone https://github.com/DeathlyCloak/Samaritan-AI-Assistant.git

### Navigate to the project directory:
cd Samaritan-AI-Assistant

### Install the required packages:
```bash
pip install gTTS sounddevice numpy scipy speech_recognition psutil pyjokes pyautogui playsound
```

### Run the main script:
```python3 Samaritan.py```

### Interact with the assistant:
- Speak commands to the assistant, such as "search," "screenshot," "music," "cpu," "battery," "joke," "remember," or "recall."
- The assistant will respond based on the command given.

# Disclaimer
- The AI records audio commands and saves them as files on your local machine, along with screenshots and text files.
- This project is inspired by the Udemy course "Learn To Create AI Assistant (JARVIS) with Python" by Arbaz Khan.
- Minimal Python knowledge is required to use this project.
- The music playback feature does not work, due to licencing of Apple Music.
- For macOS users, the afplay command is used for audio playback. Windows users may need to replace this with start in the speech_engine.py file.