Voice-Activated Personal Assistant

Overview
--------
This is a voice-activated personal assistant that performs tasks such as setting reminders, checking the weather, reading the news, 
and adding events to Google Calendar. It integrates with speech recognition and text-to-speech libraries to create an interactive experience.

Features
--------
- Speech Recognition: Uses Google Speech Recognition to understand voice commands.
- Text-to-Speech: Uses pyttsx3 to provide voice responses.
- Weather Forecast: Fetches real-time weather data from OpenWeather API.
- News Updates: Reads top headlines using NewsAPI.
- Reminders: Sets reminders and alerts the user after a specified time.
- Google Calendar Integration: Adds events to Google Calendar using Google Calendar API.

Prerequisites
-------------
Ensure you have Python installed on your system. You can check your Python version by running:
    python --version

Installation
------------
Step 1: Clone the Repository
    git clone https://github.com/your-repository/voice-assistant.git
    cd voice-assistant

Step 2: Install Required Python Packages
    pip install SpeechRecognition pyttsx3 requests schedule google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

Step 3: Set Up API Keys
------------------------
1. OpenWeather API (for weather data):
   - Sign up at https://home.openweathermap.org/users/sign_up
   - Get your API key and replace 'your_openweather_api_key' in the assistant.py file.

2. NewsAPI (for news updates):
   - Sign up at https://newsapi.org/register
   - Get your API key and replace 'your_newsapi_key' in assistant.py.

3. Google Calendar API (for event scheduling):
   - Go to https://console.cloud.google.com/
   - Create a new project and enable the Google Calendar API.
   - Create OAuth 2.0 Client ID credentials.
   - Download the credentials.json file and place it in the same directory as assistant.py.

Usage
-----
Run the assistant script using:
    python assistant.py

Commands you can say:
- "Check the weather in [city]"
- "Read the news"
- "Set a reminder for [task] in [time] seconds"
- "Add event [event name] on [date-time]"
- "Exit" (to stop the assistant)

Troubleshooting
---------------
- If you get a ModuleNotFoundError, install missing dependencies with `pip install -r requirements.txt`.
- Ensure your microphone is working properly for speech recognition.
- Make sure your API keys are correct and have necessary permissions.
