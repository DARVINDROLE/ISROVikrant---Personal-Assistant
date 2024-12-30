# **Assistant Voice Interaction and Automation Tool**

This project is a voice-driven tool combining OpenAI language capabilities with local APIs, browser automation, and other utility functions for dynamic interaction. It leverages text-to-speech (TTS), speech-to-text (STT), Wikipedia integration, and automated file downloads to provide an AI-assisted user experience.

## **Features**

1. **Voice Interaction:**  
   * Recognizes speech commands via `speech_recognition`.  
   * Provides voice responses using `pyttsx3`.  
2. **OpenAI GPT Integration:**  
   * Generates conversational responses and Python code for API interactions.  
3. **Dynamic Web Interaction:**  
   * Opens specified URLs based on spoken keywords.  
   * Offers brief descriptions of URLs using OpenAI.  
4. **Bhuvan API Code Generation:**  
   * Uses OpenAI to generate Python code for downloading data from the Bhuvan API.  
   * Includes functionality to dynamically execute generated code.  
5. **Automated File Downloads:**  
   * Downloads files with progress monitoring using `tqdm`.  
6. **Wikipedia Integration:**  
   * Summarizes Wikipedia articles based on queries.  
7. **Custom Data Management:**  
   * Provides preconfigured URL mappings and keywords for quick data access.  
8. **Utility Functions:**  
   * Multi-purpose functionalities like `wishme()` to provide greeting messages based on the time of the day.

## **Setup and Requirements**

To use this project, ensure you have the following dependencies installed:

**pip install openai requests pyttsx3 wikipedia pywhatkit tqdm SpeechRecognition gTTS**

## **How to Run**

1. **Set OpenAI API Key:** Replace `"sk-xxxx"` with your valid OpenAI API key in the script from [https://platform.openai.com/settings/organization/api-keys](https://platform.openai.com/settings/organization/api-keys)  
2. **Install Required Libraries:** Install dependencies listed in `requirements.txt`.  
3. **Launch the Application:** Run the main script `python main.py` to initiate the voice assistant.  
4. **Interactive Commands:** Speak clearly into the microphone to interact with the tool.

## **Key Functionalities**

### **Bhuvan API Interaction:**

* Say, "Generate code to download the file." The assistant will create and execute a Python script to download data from the Bhuvan API.

### **Wikipedia Search:**

* Use commands like, "Tell me about \[topic\]," or "Search for \[topic\]."

### **Open URLs with Keywords:**

* Use keywords specified in the `data_dictionary` to launch relevant web pages.

### **Code Execution:**

* Dynamically generate and execute Python scripts for specific tasks, such as file downloading from APIs.

### **Greeting Based on Time:**

* Receive context-appropriate greetings, such as "Good morning" or "Good evening."

## **Contributing**

Contributions to improve functionality or enhance the user interface are welcome. Feel free to open pull requests or issues on the GitHub repository.

**Credits**

* **Libraries Used:** OpenAI API, SpeechRecognition, pyttsx3, Wikipedia, tqdm.  
* **Data:** Keyword-to-URL mappings sourced from Bhuvan API.

