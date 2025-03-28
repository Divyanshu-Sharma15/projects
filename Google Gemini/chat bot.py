import google.generativeai as genai
import requests
from serpapi import *



# Configure Google Gemini API
GENAI_API_KEY = "your_google_gemini_api_key"
genai.configure(api_key=GENAI_API_KEY)

# Configure Google Search API
SEARCH_API_KEY = "your_serpapi_key"

# Memory system to store conversation history
conversation_history = []

def google_search(query):
    """Fetch real-time data using SerpAPI's Google Search API."""
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": SEARCH_API_KEY
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if "organic_results" in data and len(data["organic_results"]) > 0:
            return data["organic_results"][0]["snippet"]
        else:
            return "No search results found."
    else:
        return f"Error: {response.status_code}, {response.text}"


def generate_response(user_input):
    """Generates AI response using Google Gemini API."""
    
    # Check if the query requires real-time data
    if "price of bitcoin" in user_input.lower() or "weather in" in user_input.lower():
        return google_search(user_input)
    
    # Append user message to history
    conversation_history.append({"role": "user", "message": user_input})
    
    # Generate response using Gemini AI
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(conversation_history)
    
    # Extract AI response
    ai_response = response.text if response else "Sorry, I couldn't generate a response."
    
    # Store AI response in memory
    conversation_history.append({"role": "ai", "message": ai_response})
    
    return ai_response

# Chatbot Loop
if __name__ == "__main__":
    print("Welcome to Google Gemini AI Chatbot! Type 'exit' to quit.")
    
    while True:
        user_message = input("You: ")
        if user_message.lower() == "exit":
            break
        
        ai_reply = generate_response(user_message)
        print(f"AI: {ai_reply}")


