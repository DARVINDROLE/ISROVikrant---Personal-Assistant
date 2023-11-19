import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import openai 
openai.api_key = "sk-q9mLTl4x5UXE9JK6BNFkT3BlbkFJTMttWjqmZrgytuTestsh"


r = sr.Recognizer()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):                               # function which speaks
    engine.say(audio)
    engine.runAndWait()
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]    
    
def wishme():                                     #function which wish me good morning
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir i am jarvis your personal ASSISTANT , what can i do for you")
    elif hour>=12 and hour<18:
        speak("good afternoon sir i am jarvis your personal A I ,what can i do for you")
    else :
        speak("good evening sir i am jarvis your personal A I , what can i do for you")       
   
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognising....")  
        query=r.recognize_google(audio,language='en-in')
        print(f"user said :{query}\n")

    except:
       #speak("say that again please...")
       return "none"
    return query

if __name__ == "__main__":                      # last running programm
    wishme()   
    while True:
        query =takecommand().lower()
        if "gpt" in query:
         pan=takecommand().lower()
         response=generate_response(pan)
         print(f"gpt3 say:{response}")
         speak(response)
        if  "search for" in query:
            speak("searching...")
            query=query.replace("tell me about" or "search for", '')
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia" + results)
        elif 'time' in query:
           time = datetime.datetime.now().strftime('%I:%M %p')
           speak('Current time is ' + time)
        elif 'date with me' in query:
           speak('sorry, I have a headache')
        elif 'are you single' and 'are you in a relationship' in query:   
            speak('I am in a relationship with wifi')
        elif 'can you walk' and "can you run" in query:
         speak("no i can't ")    
        elif 'can you eat' and 'food' in query:
         speak("because i am an artificial intelligence i can't eat ")    
        elif 'not for you' and 'nothing' in query:
         speak("sorry")    
        elif 'study' in query:
         speak('yes why not , ask me any thing') 
        elif 'thanks' in query:
          speak('welcome') 
        elif 'how are you' and 'what about you' in query:
           speak('i am fine ')   
        elif "youtube" in query:
            webbrowser.open("youtube.com") 
        elif "google" in query:
            webbrowser.open("google.com")   
        elif "sandeep university" in query:
            webbrowser.open("https://www.sandipuniversity.edu.in/erp-login.php")       
        elif 'nothing' in query:
           speak('ok sorry')      
        elif "open pie chart" in query:
          path ="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1\\bin\\pycharm64.exe"  
          os.startfile(path)
        elif "open vs code" in query:
          path ="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1\\bin\\pycharm64.exe"  
          os.startfile(path)  
        elif "can you play" in query:
            speak("no i cannot as i am a software i could not play with tirtha") 
        elif 'play' in query:
         song = query.replace('play', '')
         speak('playing ' + song)
         pywhatkit.playonyt(song)
        elif "send message" in query:
            mom='+918369716942'
            time = datetime.datetime.now().strftime('%I:%M %p')
            #time.replace( ':' ,' ')
            perfect =(time[0] + time[1])
            mortal =(time[3] + time[4])
            subject=query.replace("send message",'')
            if 1+1==2: 
             send = takecommand().lower()
            pywhatkit.sendwhatmsg(mom, send, int(perfect) , int(mortal)+2)
        elif "take a note" in query:
            query.replace("note",'')
            if 1+1==2:
                main = takecommand().lower()
        elif "read the note" in query:
            speak(main)   
       
 
            
          
        
