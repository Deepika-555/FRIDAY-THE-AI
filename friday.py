import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Maam!")
    
    elif hour>=12 and hour<18:
        speak("Good Efternoon Maam!")
    
    else:
        speak("Good Evening Maam!")
        
    speak("hello Maam This is your artificial intelligence Friday here, how may i help you today.")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...") 
        return "None"
    return query
        
        
     
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            print('searching Wikipedia.....')
            query = query.replace("wikipedia","")
            results =wikipedia.summary(query,sentences= 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'youtube' in query:
            speak("Sure Maam")
            webbrowser.open("youtube.com")   
            
        elif 'google' in query:
            speak("Sure Maam")
            webbrowser.open("google.com")
            
        elif 'facebook' in query:
            speak("Sure Maam")
            webbrowser.open("facebook.com")
            
        elif 'instagram' in query:
            speak("Sure Maam")
            webbrowser.open("instagram.com")
        
        elif 'github' in query:
            speak("Sure Maam")
            webbrowser.open("github.com")        

        elif 'gmail' in query:
            speak("Sure Maam")
            webbrowser.open('gmail.com')
            
        elif 'song' in query:
            music_dir = 'D:\\songs\\n songs'
            songs = os.listdir(music_dir)
            print (songs) 
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Maam, the time is {strTime}")
            
        elif 'code' in query:
            speak("Sure Maam")
            codePath = "C:\\Users\\abhay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'yourself' in query:
            speak("I am FRIDAY, speed 1 terahertz, memory 1 zettabyte")
            

            
        
            
            