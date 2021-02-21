import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
#import smtplib  #for mailing ....only works on some python versions
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import cv2 
import numpy as np
import winshell

##wolfarm alpha
##things that can be added
##integration with google caleder,NEWS,WEATHER APIs
##SMS Automation
#import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

count=0

def screenshot():
    img = pyautogui.screenshot()
    img.save()

def search_yt(query):
    index =query.lower().split().index("youtube")
    search = query.split()[index+ 1 : ]
    webbrowser.open("http://www.youtube.com/results?search_query=" + "+".join(search))
    speak("Opening " + str(search) + " on youtube")

def search_google(query):
    index =query.lower().split().index("google")
    search = query.split()[index+ 1 : ]
    webbrowser.open("https://www.google.com/search?q=" + "+".join(search))
    speak( "Opening " + str(search) + " on google") 

def empty_rb():
    winshell.recycle_bin().empty(confirm=True, show_progress=True, sound=True)
    speak("Recycle Bin Emptied")

    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def location(query):
    index =query.lower().split().index("is")
    location = query.split()[index+ 1 : ]
    webbrowser.open("https://www.google.com/maps/place" + "+".join(location))
    speak("Opening " + str(search) + " on google")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        date()

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        date()

    else:
        speak("Good Evening!")
        date()

    speak("Hello I am Siri. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

"""
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
"""
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at "+ str(battery.percent))

def jokes():
    speak(pyjokes.get_joke(language="en", category="all"))

def screen_recorder():
    resolution = (1920, 1080)
    codec = cv2.VideoWriter_fourcc(*"XVID")
    filename = "Recording.avi"
    
    #count=count+1
    fps = 60.0
    out = cv2.VideoWriter(filename, codec, fps, resolution) 
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Live", 480, 270)

    while(1): 
        
        img = pyautogui.screenshot() 
  
        frame = np.array(img) 
  
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
  
        out.write(frame) 
      
        # Optional: Display the recording screen 
        cv2.imshow('Live', frame) 
      
        # Stop recording when we press 'q' 
        if cv2.waitKey(1) == ord('q'): 
            break

    out.release() 
  
    # Destroy all windows 
    cv2.destroyAllWindows()


    
    
    
if __name__ == "__main__":
    count=0
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'search in youtube' in query:
            search_yt(query)

        elif 'search in google' in query:
            search_google(query)

        elif 'play music' in query:
            music_dir = 'songs'
            #music_dir = 'YOUR MUSIC DIRECTORY'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "PATH OF VS CODE"
            os.startfile(codePath)

        #ends the program here
        elif 'offline' in query:
            quit()

        elif 'remember that ' in query:
            speak("What shoul i remember")
            data = takeCommand()
            speak("You said to remember" + data)
            #create a data.txt file for successful compilation of the code
            date=datetime.datetime.now()
            #file_name = str(date).replace(':','-') + "note.txt"
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'am i missing ' in query:      
            remember = open('data.txt','r')
            speak("You said me to remember that " + remember.read())

        elif "screenshot" in query :
            screenshot()
            speak("Screenshot taken successfully")

        elif 'cpu' in query :
            cpu()

        elif 'jokes' in query:
            jokes()

        elif 'screen record' in query:
            screen_recorder()

        elif 'empty recyclebin'in query:
            empty_rb()

        elif 'where is' in query:
            location(query)
            
        #shut down the computer in the below queries
            
        elif 'logout' in query :
            os.system("locking -l")

        elif 'restart' in query :
            os.system("restsrting /r /t 1")

        elif 'shutdown' in query :
            os.system("shutdown /s /t 1")
