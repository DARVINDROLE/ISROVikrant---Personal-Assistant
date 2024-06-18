# Darvin---Your-Personal-Assistant
Darvin: Your Personal Voice Assistant
Darvin is an advanced personal voice assistant built using Python and AI technologies. It integrates speech recognition, natural language processing, and web APIs to perform a variety of tasks seamlessly through voice commands.

Key Features:
Voice Interaction: Communicate with Darvin using natural language commands.
Information Retrieval: Fetch information from Wikipedia, check the current time, and more.
Web Browsing: Open websites like Google, YouTube, and Sandeep University directly from voice commands.
Entertainment: Play YouTube videos and schedule messages using PyWhatKit.
AI Capabilities: Utilizes OpenAI's GPT-3 for generating responses and engaging in conversations.
Usage:
Installation: Clone the repository and install dependencies (pyttsx3, speech_recognition, wikipedia, pywhatkit, openai).
Setup: Configure the voice and API keys as per instructions in the README.
Execution: Run python darvin.py to activate Darvin and start giving voice commands.
Future Enhancements:
Incorporate more AI capabilities for enhanced user interaction.
Improve speech recognition accuracy and response time.
Expand functionality to include more applications and services.

# ISROVikrant ----- made for ISRO
Bhuvan Assistant
Overview
This Python script acts as a virtual assistant powered by various APIs and AI models to perform tasks such as generating responses, downloading files from Bhuvan API, navigating to Bhuvan categories, and providing information from Wikipedia.

Features:
Voice Interaction: Utilizes speech recognition (via speech_recognition library) and text-to-speech capabilities (via pyttsx3) for user interaction.
OpenAI Integration: Uses OpenAI's GPT-3 model for generating responses and Python code snippets dynamically.
Bhuvan API Interaction: Downloads zipped files from Bhuvan API using generated Python code.
Web Scraping: Opens Bhuvan web pages based on user queries using webbrowser.
Wikipedia Integration: Provides summaries of topics using wikipedia API.

Dependencies:
openai: for accessing OpenAI's API
requests: for making HTTP requests
pyttsx3: for text-to-speech conversion
wikipedia: for fetching information from Wikipedia
webbrowser: for opening URLs in the web browser
speech_recognition: for voice recognition
gtts: for Google Text-to-Speech API
tqdm: for displaying progress bars

Setup
Install dependencies
Copy code
"pip install openai requests pyttsx3 wikipedia pywhatkit SpeechRecognition gtts tqdm"
Set up OpenAI API key in the script (openai.api_key = "your_api_key").

Usage:
Run the script (python bhuvan_assistant.py).
The assistant will greet you based on the time of the day.
Speak or enter a query.
Based on the query:
Download files from Bhuvan API.
Fetch information from Wikipedia.
Open Bhuvan web pages related to specific categories.
Voice Commands
Download: To initiate file download using generated code.
Aditya: To generate responses based on user input.
Specific Keywords: Directs to specific Bhuvan categories based on user input.
Tell me about / Search for: Retrieves information from Wikipedia based on the query.

