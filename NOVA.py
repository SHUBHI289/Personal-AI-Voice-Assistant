"""Personal AI Voice Assistant - NOVA

A voice-activated assistant that understands voice commands and performs
various tasks like weather lookup, Wikipedia searches, web browsing, etc.

Author: Shubhi
Created: 2024
"""

import os
import sys
import time
import logging
import datetime
from typing import Optional
from pathlib import Path

import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize text-to-speech engine
try:
    if sys.platform == 'win32':
        engine = pyttsx3.init('sapi5')
    else:
        engine = pyttsx3.init()
    
    # Get available voices and set voice properties
    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[0].id)
        logger.info(f"Voice engine initialized with {len(voices)} voice(s) available")
    else:
        logger.warning("No voices available for text-to-speech")
except Exception as e:
    logger.error(f"Failed to initialize text-to-speech engine: {e}")
    sys.exit(1)


def speak(audio: str) -> None:
    """Convert text to speech and play it.
    
    Args:
        audio (str): The text to be spoken.
    """
    try:
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        logger.error(f"Error in text-to-speech: {e}")


def wish_me() -> None:
    """Greet the user based on the current time of day."""
    try:
        hour = int(datetime.datetime.now().hour)
        
        if 0 <= hour < 12:
            speak("Good morning! I am your personal assistant NOVA. How can I help you?")
            print("\n🌅 Good Morning! NOVA is ready to assist.")
        elif 12 <= hour < 18:
            speak("Good afternoon! I am your personal assistant NOVA. How can I help you?")
            print("\n☀️ Good Afternoon! NOVA is ready to assist.")
        else:
            speak("Good evening! I am your personal assistant NOVA. How can I help you?")
            print("\n🌙 Good Evening! NOVA is ready to assist.")
    except Exception as e:
        logger.error(f"Error in greeting: {e}")
        speak("Hello! I am NOVA. How can I help you?")


def take_command() -> str:
    """Listen for voice input from the user and convert it to text.
    
    Returns:
        str: The recognized command as text, or 'none' if recognition fails.
    """
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            print("\n🎤 Listening...")
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source, phrase_time_limit=5)
        
        print("🔄 Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"✅ You said: {query}\n")
        return query
    
    except sr.UnknownValueError:
        logger.warning("Could not understand audio")
        print("❌ Could not understand what you said. Please try again.\n")
        speak("Sorry, I didn't catch that. Please repeat.")
        return "none"
    
    except sr.RequestError as e:
        logger.error(f"Speech recognition error: {e}")
        print(f"❌ Error with speech recognition service: {e}\n")
        speak("There seems to be an issue with the speech recognition service.")
        return "none"
    
    except Exception as e:
        logger.error(f"Unexpected error in voice recognition: {e}")
        print(f"❌ Unexpected error: {e}\n")
        return "none"


def get_weather(city_name: str) -> None:
    """Fetch and announce weather information for a given city.
    
    Args:
        city_name (str): The name of the city.
    """
    try:
        api_key = os.getenv('WEATHER_API_KEY')
        
        if not api_key:
            logger.error("WEATHER_API_KEY not found in environment variables")
            speak("Weather API key is not configured. Please set up the .env file.")
            return
        
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        
        response = requests.get(complete_url, timeout=5)
        weather_data = response.json()
        
        if weather_data.get('cod') != '404':
            main_data = weather_data.get('main', {})
            weather_description_list = weather_data.get('weather', [])
            
            temperature = main_data.get('temp', 'N/A')
            humidity = main_data.get('humidity', 'N/A')
            weather_description = weather_description_list[0].get('description', 'N/A') if weather_description_list else 'N/A'
            
            weather_info = f"Temperature is {temperature} Kelvin with {humidity}% humidity and {weather_description} conditions."
            print(f"\n🌤️  Weather in {city_name}:")
            print(f"   Temperature: {temperature} K")
            print(f"   Humidity: {humidity}%")
            print(f"   Condition: {weather_description}\n")
            speak(f"The weather in {city_name} is: {weather_info}")
        else:
            logger.warning(f"City not found: {city_name}")
            print(f"\n❌ City '{city_name}' not found.\n")
            speak(f"I couldn't find weather information for {city_name}.")
    
    except requests.Timeout:
        logger.error("Weather API request timed out")
        speak("The weather service is taking too long to respond.")
    except requests.RequestException as e:
        logger.error(f"Error fetching weather data: {e}")
        speak("There was an error fetching weather information.")
    except Exception as e:
        logger.error(f"Unexpected error in get_weather: {e}")
        speak("An error occurred while fetching weather information.")


def open_application(app_name: str) -> None:
    """Open an application or website.
    
    Args:
        app_name (str): Name of the application to open.
    """
    try:
        if app_name.lower() == 'code' or app_name.lower() == 'vscode':
            if sys.platform == 'win32':
                os.startfile('code')  # Opens VS Code on Windows
            else:
                os.system('code')  # Opens VS Code on macOS/Linux
            speak(f"Opening {app_name}")
        else:
            speak(f"Sorry, I don't have {app_name} configured yet.")
    except Exception as e:
        logger.error(f"Error opening application {app_name}: {e}")
        speak(f"Could not open {app_name}")


def play_music() -> None:
    """Play music from the configured music directory."""
    try:
        music_dir = os.getenv('MUSIC_DIR')
        
        if not music_dir or not os.path.exists(music_dir):
            logger.warning(f"Music directory not configured or not found: {music_dir}")
            speak("Music directory is not configured. Please set MUSIC_DIR in the .env file.")
            return
        
        songs = os.listdir(music_dir)
        if not songs:
            speak("No songs found in the music directory.")
            return
        
        print(f"\n🎵 Found {len(songs)} song(s):")
        for idx, song in enumerate(songs[:5], 1):
            print(f"   {idx}. {song}")
        
        song_path = os.path.join(music_dir, songs[0])
        if sys.platform == 'win32':
            os.startfile(song_path)
        else:
            os.system(f'open "{song_path}"')  # macOS
        
        speak(f"Playing {songs[0]}")
        print(f"\n▶️  Now playing: {songs[0]}\n")
    
    except IndexError:
        speak("No songs available to play.")
    except Exception as e:
        logger.error(f"Error playing music: {e}")
        speak("Could not play music.")


def search_wikipedia(query: str) -> None:
    """Search Wikipedia and read the summary aloud.
    
    Args:
        query (str): The search term.
    """
    try:
        speak("Searching Wikipedia...")
        print("\n📚 Searching Wikipedia...")
        
        # Clean up the query
        query = query.replace("wikipedia", "").replace("search", "").strip()
        
        if not query:
            speak("Please specify what you'd like to search for.")
            return
        
        results = wikipedia.summary(query, sentences=2)
        print(f"\n📖 {query}:")
        print(f"   {results}\n")
        speak(f"According to Wikipedia: {results}")
    
    except wikipedia.exceptions.DisambiguationError as e:
        logger.warning(f"Disambiguation error for query: {query}")
        speak(f"Your search for {query} was ambiguous. Please be more specific.")
    except wikipedia.exceptions.PageError:
        logger.warning(f"Page not found for query: {query}")
        speak(f"I couldn't find a Wikipedia page for {query}.")
    except Exception as e:
        logger.error(f"Error searching Wikipedia: {e}")
        speak("There was an error searching Wikipedia.")


def main() -> None:
    """Main function to run the voice assistant."""
    print("\n" + "="*50)
    print("🤖  NOVA - Personal AI Voice Assistant")
    print("="*50)
    
    wish_me()
    
    print("\nAvailable Commands:")
    print("  - 'wikipedia [topic]' - Search Wikipedia")
    print("  - 'weather' - Get weather information")
    print("  - 'open youtube/google/stackoverflow' - Open websites")
    print("  - 'the time' - Get current time")
    print("  - 'play music' - Play music")
    print("  - 'open news' - Open news")
    print("  - 'exit/quit' - Stop the assistant")
    print("\n" + "="*50 + "\n")
    
    try:
        while True:
            query = take_command().lower()
            
            if not query or query == "none":
                continue
            
            # Exit commands
            if any(word in query for word in ['exit', 'quit', 'goodbye', 'bye']):
                speak("Thank you for using NOVA. Goodbye!")
                print("\n👋 NOVA shutting down. Goodbye!\n")
                break
            
            # Wikipedia search
            elif 'wikipedia' in query:
                search_wikipedia(query)
            
            # Weather
            elif 'weather' in query:
                speak("Which city would you like weather for?")
                city_name = take_command()
                if city_name and city_name != "none":
                    get_weather(city_name)
            
            # Open websites
            elif 'open youtube' in query:
                speak("Opening YouTube")
                webbrowser.open("https://youtube.com")
                print("\n▶️  Opening YouTube...\n")
            
            elif 'open google' in query:
                speak("Opening Google")
                webbrowser.open("https://google.com")
                print("\n🔍 Opening Google...\n")
            
            elif 'open stackoverflow' in query:
                speak("Opening Stack Overflow")
                webbrowser.open("https://stackoverflow.com")
                print("\n💻 Opening Stack Overflow...\n")
            
            # Time
            elif 'the time' in query:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The current time is {current_time}")
                print(f"\n⏰ Current time: {current_time}\n")
            
            # Open application
            elif 'open code' in query or 'open vscode' in query:
                open_application('VS Code')
                print("\n💻 Opening VS Code...\n")
            
            # Play music
            elif 'play music' in query:
                play_music()
            
            # News
            elif 'news' in query:
                speak("Opening news headlines from Times of India")
                webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                print("\n📰 Opening news headlines...\n")
                time.sleep(2)
            
            else:
                speak("I didn't understand that command. Please try again.")
                print("❓ Command not recognized. Please try again.\n")
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user. Shutting down...\n")
        speak("Shutting down. Goodbye!")
    except Exception as e:
        logger.error(f"Unexpected error in main loop: {e}")
        print(f"\n❌ An unexpected error occurred: {e}\n")
        speak("An error occurred. Please restart the application.")


if __name__ == "__main__":
    main()
