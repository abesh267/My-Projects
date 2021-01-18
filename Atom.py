import pyttsx3 #text to speech library
import speech_recognition as sr #speech input
import datetime  #date-time module
import wikipedia  #taking wikipedia library for infos
import webbrowser #webbrowser module to use websites
import os  #for opening files from desktop


engine = pyttsx3.init('sapi5') #sapi5 is a microsoft API which allows speech recognition. You can change the voice of this code
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):  #created speech function to make this code speak
    engine.say(audio)
    engine.runAndWait() #runAndWait for running the code and waiting for the user to speak


def talkToMe(): #A function to speak 
    hour = int(datetime.datetime.now().hour) #current time. wishes you based on time everytime you open it
    if hour>=0 and hour<12:
        speak("Hello! Good Morning!")

    elif hour>=12 and hour<18:
        speak("Hello! Good Afternoon!")   

    else:
        speak("Hello! Good Evening!")  

    speak("I am Atom. Your personal virtual assistant created by Abesh. How may I help you?")       

def takeCommand(): #Function to take commands from the user
    

    r = sr.Recognizer() #Recognizing the speech 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #threshold of the speech
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #using google for taking and searching queries. Could've used bing or others.
        print(f"User said: {query}\n")

    except:
            
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    talkToMe()
    #while True: (For Infinite time of asking)
    if 1:
    
        query = takeCommand().lower() #taking everything in lowercase to make the code understand

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1) #will speak out only one sentence. can change it as your will
            speak("According to Wikipedia") #by defaul says this line
            print(results)
            speak(results)

        elif 'open youtube' in query:   #the following strings in query are in lower case because used .lower() in the line 57
            speak("Opening youtube")    #by defaul says this line
            webbrowser.open("youtube.com")  #opens youtube from your default browser
        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            speak("Opening facebook")
            webbrowser.open("facebook.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  #the VScode path of my desktop. Can open any file just by speaking to it
            os.startfile(codePath)  #opens the file. You can also play music from your PC in the same way
        elif "atom let's wish happy birthday to you" in query:
            speak("Happy birthday to you.")


'''
Created by,
MD. Mustakin Alam Abesh
Department of Computer Science and Engineering, BRAC University

With help from YouTube Channel - Code With Harry
'''
        

