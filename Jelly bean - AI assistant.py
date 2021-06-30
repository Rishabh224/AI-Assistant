#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyttsx3    # convert text to speech    #### pip install pyttsx3 (to install the module first and then import)
import datetime   # for date & time or calendar purpose
import speech_recognition as sr    # to recognize our voice  #### pip install Speech_Recognition(to install first)
                                                             ####  pip install pipwin (to run the upper module)
import wikipedia       # to search on the wikipedia on the web     #### pip install wikipedia
import smtplib        # to access the server 
import webbrowser as wb   # to perform web search
import os                 # to access/interact the system
import pyautogui        #### pip install pyautogui
import psutil           ### pip install psutil
import pyjokes         #### pip install pyjokes
import json    
import requests
import wolframalpha     # to compute expert level answers using algorithms   #### pip intstall wolframalpha

Engine = pyttsx3.init()
voices = Engine.getProperty("voices")
Engine.setProperty("voice",voices[1].id)
newVoiceRate = 160
Engine.setProperty("rate",newVoiceRate)
def speak(audio):
    Engine.say(audio)
    Engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime('%H:%M:%S')
    speak('Current time is')
    speak(Time)
    print(Time)

def date():
    Date = datetime.datetime.now().strftime('%D')
    speak('Current date is')
    speak(Date)
    print(Date)

def greet():
    speak('Welcome back Sir')
    hour = datetime.datetime.now().hour
    if hour >= 5 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 17:
        speak('Good afternoon')
    elif hour >= 17 and hour < 22:
        speak('Good Evening')
    else:
        speak('Good night')
        
    speak('Jelly Bean at your service! How may I help you?')

def takeCommand():    # take user's command
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print('Listening.....')
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio)
    
    except Exception as e:
        print(e)
        speak('Sorry! I could not recognize your voice! Say that again please...')
        print('Sorry! I could not recognize your voice! Say that again please.......!!!')
        return 'None'
    return query

def sendmail(to,content):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('alienbunny30@gmail.com','jerryismyuniverse')
    server.sendmail('alienbunny30@gmail.com',to,content)
    server.quit()

def screenshot():
    img = pyautogui.screenshot()
    img.save('D:/SOFTWARE/Pictures/screenshots/1.jpg')

def cpu():     # compute cpu & battery %
    usage = str(psutil.cpu_percent())
    speak('CPU is at:' + usage)
    print('CPU:' + usage)
    
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)
    print('Battery:' + str(battery.percent))
    
def jokes():
    speak(pyjokes.get_joke())
    
if __name__ == '__main__':
    
    ##### main function  ######
    greet()
    
    while True:
        query = takeCommand().lower()
        print(query)
        
        if 'offline' in query or 'stop' in query:
            speak('Shutting down, Goodbye have a nice day!')
            print('Shutting down, Goodbye have a nice day!')
            break
        
        elif 'time' in query:
            time()
            
        elif 'date' in query:
            date()
        
        elif 'thank you' in query:
            speak('Its my pleasure to serve you,Thank You!')
            print('Its my pleasure to serve you,Thank You!')
            
        elif 'wikipedia' in query:
            speak('searching....')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=2)
            speak(result)
            
        elif 'change my name to' in query:
            query = query.replace('change my name to','')
            new_name = query
            speak('Hello' + new_name)
            print('Hello' + new_name + '....')
            
        elif 'email' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = 'rishabhkumar316@gmail.com'
                sendmail(to,content)
                print('Email sent successfully')
                speak('Email sent successfully')
                
            except Exception as e:
                speak(e)
                print('unable to send the mail')
                speak('unable to send the mail')
                
        elif 'search' in query:
            speak('What do you want search?')
            microsoftpath = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
            search = takeCommand().lower()
            wb.get(microsoftpath).open_new_tab(search + '.com')
        
        elif 'news' in query:
            news = wb.open_new_tab('https://timesofindia.indiatimes.com/home/headlines')
            speak('Here are some headlines from the Times of India, Happy reading')
            
        elif 'logout' in query:
            os.system('shutdown - l')
            
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')
            
        elif 'restart' in query:
            os.system('shutdown /r /t 1')
        
        elif 'songs' in query or 'play' in query:
            songs_dir = 'D:/SOFTWARE/Music'
            songs = os.listdir(songs_dir)
            random = os.startfile(os.path.join(songs_dir, songs[1]))
        
        elif 'set reminder' in query:
            speak('What reminder do u want me to set?:')
            data = takeCommand()
            speak('You told me to remind that:' + data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        
        elif 'what is my reminder' in query:
            remember = open('data.txt','r')
            speak('U said me to remind that:' + remember.read())
        
        elif 'screenshot' in query:
            screenshot()
            speak('Screenshot captured')
            
        elif 'cpu' in query:
            cpu()
            
        elif 'joke' in query:
            jokes()
        
        elif 'good morning' in query:
            speak('A warm' + query)
            speak('How are you mister' + new_name)
        
        elif 'good night' in query:
            speak('Good night')
            speak('Sleep tight and have sweet dreams' + new_name)
        
        elif 'how are you' in query:
            speak('I am perfectly fine,i am glad to hear from you')
        
        elif 'i love you' in query:
            speak('Thats so sweet of you to say to me, love you so more')
        
        elif 'weather' in query:
            api_key="c8cb985c0a0142f981be9f23ca7f8e14"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            print(city_name)
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = int(y["temp"] - 273.15)
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in celcius unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")
        
        elif 'question' in query:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question = takeCommand()
            print(question)
            app_id = "Q2K7YV-AX6U28TYGV "
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        
        elif 'where is' in query:
            query = query.replace('where is', '')
            location = query
            speak('You asked me to locate:')
            speak(location)
            wb.open('https://www.google.nl/maps/place/' + location + '')
            
        
        elif 'who are you' in query or 'what can you do' in query:
            speak('I am blueberry one point zero , I am your virtual assistant as I can do a lot of things for you'
                  'like i can tell u the time or date,predict weather,search for you on the web'
                 'I can search for the latest news for you, play songs,and set a reminder for you')
            
        elif 'who made you' in query or 'who created you' in query:
            speak('I was built by Mr. Rishabh')

