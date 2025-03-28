import speech_recognition as sr
import pyttsx3
import requests
import datetime
import webbrowser
import os
import wikipedia
import google_auth_oauthlib.flow
import googleapiclient.discovery

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Recognize speech from microphone
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("There was an error with the speech recognition service.")
        return ""

# Get weather information
def get_weather(city):
    API_KEY = "your_openweather_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        temperature = response["main"]["temp"]
        weather_desc = response["weather"][0]["description"]
        speak(f"The temperature in {city} is {temperature} degrees Celsius with {weather_desc}.")
    else:
        speak("I couldn't fetch the weather information. Please try again.")

# Get news headlines
def get_news():
    API_KEY = "your_newsapi_key"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
    response = requests.get(url).json()
    articles = response.get("articles", [])[:5]
    if articles:
        speak("Here are the top news headlines.")
        for article in articles:
            speak(article["title"])
    else:
        speak("I couldn't fetch the news at the moment.")

# Tell the current time
def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The current time is {current_time}.")

# Tell the current date
def tell_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%A, %B %d, %Y")
    speak(f"Today's date is {current_date}.")

# Search Google
def search_google(query):
    speak(f"Searching Google for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

# Search Wikipedia
def search_wikipedia(query):
    speak(f"Searching Wikipedia for {query}")
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(summary)
    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple results. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("I couldn't find anything on Wikipedia about that.")

# Open applications
def open_application(app_name):
    if "notepad" in app_name:
        os.system("notepad")
    elif "calculator" in app_name:
        os.system("calc")
    elif "browser" in app_name:
        webbrowser.open("https://www.google.com")
    else:
        speak("I can't open that application.")

# Integrate Google Calendar API
def add_google_calendar_event(event_name, event_time):
    speak("Adding event to Google Calendar.")
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        "credentials.json", ["https://www.googleapis.com/auth/calendar"]
    )
    creds = flow.run_local_server(port=0)
    service = googleapiclient.discovery.build("calendar", "v3", credentials=creds)
    event = {
        'summary': event_name,
        'start': {'dateTime': event_time, 'timeZone': 'UTC'},
        'end': {'dateTime': event_time, 'timeZone': 'UTC'},
    }
    service.events().insert(calendarId='primary', body=event).execute()
    speak("Event added successfully!")

# Main function
def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = recognize_speech()
        if "weather" in command:
            speak("Which city do you want the weather for?")
            city = recognize_speech()
            if city:
                get_weather(city)
        elif "news" in command:
            get_news()
        elif "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "search google for" in command:
            query = command.replace("search google for", "").strip()
            search_google(query)
        elif "search wikipedia for" in command:
            query = command.replace("search wikipedia for", "").strip()
            search_wikipedia(query)
        elif "open" in command:
            app_name = command.replace("open", "").strip()
            open_application(app_name)
        elif "add event" in command:
            speak("What is the event name?")
            event_name = recognize_speech()
            speak("What is the event time in YYYY-MM-DDTHH:MM:SS format?")
            event_time = recognize_speech()
            add_google_calendar_event(event_name, event_time)
        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
