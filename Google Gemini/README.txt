# Google Gemini AI Chatbot with Real-Time Search

## Overview
This project implements a chatbot using Google Gemini AI and integrates real-time data retrieval via the SerpAPI-powered Google Search API. The chatbot can remember conversation history and provide live information such as Bitcoin prices and weather updates.

## Features
- **Conversational AI** powered by Google Gemini
- **Real-time search** using SerpAPI
- **Memory retention** to track conversation history
- **Easy-to-use interface** via command-line interaction

## Requirements
Ensure you have the following installed:
- Python 3.11+
- Required Python libraries:
  - `requests`
  - `serpapi`

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/chatbot-project.git
   cd chatbot-project
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up SerpAPI**
   - Create an account at [SerpAPI](https://serpapi.com/)
   - Get your API key and replace `your_serpapi_key` in the code.

## Usage
Run the chatbot with:
```bash
python chatbot.py
```
Example conversation:
```
Welcome to Google Gemini AI Chatbot! Type 'exit' to quit.
You: price of bitcoin
Bot: The current price of Bitcoin is $64,500 (as of latest data).
```

## Troubleshooting
- **ModuleNotFoundError?** Install missing dependencies with `pip install requests serpapi`.
- **RecursionError?** Ensure you're not calling `google_search()` inside itself.
- **API Key Error?** Double-check your SerpAPI key in the script.

