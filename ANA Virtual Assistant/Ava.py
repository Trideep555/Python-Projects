import pyautogui as pg
import pywhatkit
import pyttsx3 as p
import datetime as d
import os
import speech_recognition as sr
import wikipedia
import webbrowser
import time
import smtplib
import pyjokes
import requests
import json
import random
import calendar



    

engine = p.init()
voices1 = engine.getProperty('voices')
engine.setProperty('voice', voices1[1].id)
engine.setProperty('rate', 180)
username = os.getlogin()
username = username[:username.index(" ")]


  
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def start():
    timer = int(d.datetime.now().hour)
    if timer >= 4 and timer <= 12:
        print(f"Good Morning! {username}")
        speak(f"Good Morning! {username}")
    if timer > 12 and timer <= 17:
        print(f"Good Afternoon! {username}")
        speak(f"Good Afternoon!{username}")
    if timer > 17 and timer < 4:
        print(f"Good Evening! {username}")
        speak(f"Good Evening!{username}")
    print("I am Your Assistant Ava. How Can I help you?")
    speak("I am Your Assistant Ava. How Can I help you?")


def commands():
    speeching = sr.Recognizer()
    with sr.Microphone() as sound:
        print("Listening...")
        speeching.pause_threshold = 0.8
        audio = speeching.listen(sound, phrase_time_limit=5)
    try:
        print("Recognising....")
        query = speeching.recognize_google(audio, language="en-in")
        print(query)
    except Exception as e:
        print("Sorry Could not Understand Please Repeat Again")
        return "None"
    return query

def whatsapp(num, msg):
    pywhatkit.sendwhatmsg_instantly('+91' + num, msg)
    time.sleep(5)
    pg.click(1920 / 2, 1080 / 2)
    pg.press("enter")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pritic1108@gmail.com', 'qwerty@123')
    server.sendmail('pritic1108@gmail.com', to, content)
    server.close()


def readnews(category="NULL"):
    if category=="NULL":
        url='https://newsapi.org/v2/top-headlines?country=in&apiKey=62495f7692b8421ca0fe177aaa3877a1'
    else:
        url=f'https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey=62495f7692b8421ca0fe177aaa3877a1'
    news=requests.get(url).json()
    i=random.randint(0,10)
    print(news['articles'][i]['title'])
    speak(news['articles'][i]['title'])
    print(news['articles'][i]['description'])
    speak(news['articles'][i]['description'])


def quote_of_the_day():
	response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
	if response.status_code == 200:    
		json_data = response.json()
		data = json_data['data']
		print("\""+data[0]['quoteText']+"\" \n -By "+data[0]['quoteAuthor']);speak(f"{data[0]['quoteText']} Told By {data[0]['quoteAuthor']}")
        
                     
	else:
			print("Error while getting quote")
    

def showweather(city_name="Kolkata"):
    api_key = "d6d3f3bbcba101eb2f5314222dfc963f"
 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    
    x = requests.get(complete_url).json()
    

    
    if x["cod"] != "404":
    
        y = x["main"]
    
        current_temperature = (int)(y["temp"]-273)
        current_pressure = y["pressure"]
    
        current_humidity = y["humidity"]
    
        z = x["weather"]
    
        weather_description = z[0]["description"]
        print(" Temperature = " + str(current_temperature) +" Degree Celcius\n atmospheric pressure= " +str(current_pressure) +"Hpa\n humidity = " +str(current_humidity) +"%\n description = " +str(weather_description))    
        speak(f"Temperature= {str(current_temperature)} Degree Celcius. Atmospheric pressure = {str(current_pressure)} hpa. Humidity  ={str(current_humidity)} percentage. Currently {str(weather_description)}")
        
    
    else:
        print(" City Not Found ")


def command_list():
    print("/-----------------------------AVA Commands---------------------------------")
    print("1.Wikipedia")
    print("2. Search")
    print("3.Open Youtube")
    print("4.Open Google")
    print("5. Jokes")
    print("6.Open WhatsApp")
    print("7.WhatsApp Someone")
    print("8.Open my website 1.doctor 2.tuition 3.blobtech")
    print("9.Send Mail")
    print("10. Open code")
    print("11. Open C++")
    print("12. Open submile")
    print("13. Open Calculator")
    print("14. Open Text")
    print("15. News")
    print("16. Business News")
    print("17.Sports News")
    print("18. Technology News")
    print("19.Entertainment News")
    print("20. Medical News")
    print("21. Weather Here")
    print("22. Show weather in")
    print("23.Email")
    print("24.Time")
    print("25. Calendar")
    print("26.Quote_of_the_day")
    print("27.Who are you?")
    print("28.Who created you?")
    print("29.Pause for __ seconds (10-99 seconds)")
    print("30.Pause for __ minutes (1-9 minutes)")
    print("31.Shutdown My Computer")
    print("32.Restart My Computer")
    print("33. Thank You")
    print("34. Commands")
    print("35.Open Facebook")
    print("36.Close/Quit/Stop")
    
def actions(query):
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(f"According To Wikipedia {result}")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open code' in query:
            os.startfile("C:\\Users\\TRIDEEP BANERJEE\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif 'open submile text' in query:
            os.startfile("C:\\Program Files\\Sublime Text 3\\sublime_text.exe")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open my website' in query:
            print("Which one do you wanna open?")
            speak("Which one do you wanna open")
            query2 = commands().lower()
            if 'doctor' in query2:
                webbrowser.open("animalacocllections.com/doctor")
            elif 'tution' in query2:
                webbrowser.open("schoolcodehub.com")
            elif 'blobtech' in query2:
                webbrowser.open("blobtech.co.in")
            else:
                speak("No such Website you created")
        elif 'open whatsapp' in query:
            os.startfile("C:\\Users\\TRIDEEP BANERJEE\AppData\Local\\WhatsApp\\WhatsApp.exe")
        elif 'open chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif 'search' in query:
            pywhatkit.search(query)
        elif 'whatsapp someone' in query:
            speak("Enter number")
            num = input("Enter number\n")
            speak("Enter message")
            msg = input("The message\n")
            whatsapp(num, msg)
        elif 'email' in query:
            speak("Enter Mail ID")
            mail = input("Enter Mail ID\n")
            speak("Enter message")
            msg2 = input("The message\n")
            sendEmail(mail, msg2)

        elif 'shutdown computer' in query:
            os.system('shutdown -s')
        elif 'restart computer' in query:
            os.system('shutdown /r /t 1')
        elif 'who are you' in query:
            print("I am Ava")
            speak('I am Ava')
        elif 'who created you' in query:
            print("Trideep made me.I am very happy to be alive")
            speak("Trideep made me I am very happy to be alive")
        elif 'joke' in query or 'jokes' in query:
            jokes = pyjokes.get_joke()
            print(jokes)
            speak(jokes)
        elif 'news' in query:
            readnews()
        elif 'business news' in query:
            readnews("business")
        elif 'entertainment news' in query:
            readnews("entertainment")
        elif 'sports news' in query:
            readnews("sports")
        elif 'medical news' in query:
            readnews("health")
        elif 'technology news' in query:
            readnews("technology")
        elif 'weather here' in query:
            showweather()
        elif 'show weather' in query:
            speak("Please Enter the city name")
            city_name = input("Please Enter the city name")
            showweather(city_name)
        elif 'time' in query:
            print(d.datetime.now().strftime("%I:%M:%S"))
            speak(d.datetime.now().strftime("%I:%M:%S"))
        elif 'thank you' in query:
            speak("Your Welcome. What else can i do for you")
            print("Your Welcome What else can I do for you?")
        elif 'calendar' in query:
            year=d.datetime.now().year
            month=d.datetime.now().month
            print(calendar.month(year,month))
        elif 'calculator' in query:
            os.system("python D:\\tkinter\\Calculator\\Calculator.py 1")
        elif 'open text' in query:
            os.system("python D:\\tkinter\\Project Codes\\Texter.py")
        elif 'open chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif 'open c++' in query or 'c plus plus' in query:
            os.startfile("C:\\Program Files (x86)\\Embarcadero\\Dev-Cpp\\devcpp.exe")
        elif 'pause for' in query and 'seconds' in query:
            pause=int(query[10:12])
            print("Paused")
            time.sleep(pause)
        elif 'pause for' in query and 'minutes' in query:
            pause=int(query[10:11])
            print("Paused")
            time.sleep(pause*60)
        elif 'quote of the day' in query:
            quote_of_the_day()
        elif 'close' in query or 'quit' in query or 'goodbye' in query or 'stop' in query:
            print("Thank You! Hope You have a nice day")
            speak("Thank You! Hope You have a nice day")
            quit()
        elif 'commands' in query:
            command_list()
        elif 'none' in query:
            pass
        else:
            print("I am sorry I do not know that")
            print("Please Contact Trideep if u want to add this answer")
            speak("I am sorry I do not know that")



if __name__ == '__main__':
    start()
    while True:
        query=commands().lower()
        actions(query)
