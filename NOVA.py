import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser 
import os
import requests
import time

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishMe():
   hour= int(datetime.datetime.now().hour)
   if hour==0 and hour<12:
         speak("good morning!")
   elif hour==12 and hour<18:
        speak("good afternoon!")
        speak('Hii mam . I AM your nova . Give me command')
   else:
    speak("good evening") 
    speak(" hello shubhi . I am nova mam . how may I help you ")
       
        
def takecommand():
        #it takes  microphone input from that user and returns string output 

         r=sr.Recognizer()
         with sr.Microphone() as source: 
            print("listening...")
            r.pause_threshold = 1
            audio= r.listen(source , phrase_time_limit=4 )
         try:
               print("Recognizing....")
               query = r.recognize_google(audio,language='en-in')
               print(f"user said: {query}\n")

         except Exception as e:
            print(e)

            print("say that again please...")
            return "none"
         return query   


if __name__=="__main__":
     wishMe()
while True:
# if 1:
     query= takecommand().lower()
   #  logic for executing tasks based on query
     if 'wikipedia' in query:
         speak('searching wikipedia...')
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query,sentences=1)
         speak("According to wikipedia")
         print(results)
         speak(results)

         def sendEmail(to,content):
           webbrowser.open('mailto:bhagwatigupta1958@gmail.com')
     
     elif 'open youtube' in query:
          webbrowser.open("youtube.com")
         
     elif 'open google'in query:
         webbrowser.open("google.com")

     elif 'open stackoverflow'in query:
         webbrowser.open("stackoverflow.com")  
     elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"MAM,the time is {strTime}")
     elif 'open code' in query:  
         Codepath="C:\\Users\\shubh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk" 
         os.startfile(Codepath)
     elif 'play music' in query:
          music_dir = 'D:\\Lesson 4\\songs'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir , songs[2]))
     
     elif "weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takecommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

     elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
 
    






























     


                


    

    
            
        

     


    

