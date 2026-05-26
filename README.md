# NOVA - Personal AI Voice Assistant

A Python-based voice-activated personal assistant that understands voice commands and performs various tasks like weather lookup, Wikipedia searches, web browsing, music playback, and more.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

---

## 🌟 Features

- 🎤 **Voice Recognition** - Understand natural voice commands using Google Speech-to-Text API
- 🔊 **Text-to-Speech** - Respond to user commands with natural-sounding voice output
- 🌤️ **Weather Information** - Get real-time weather data for any city using OpenWeatherMap API
- 📚 **Wikipedia Search** - Search and summarize information from Wikipedia
- 🌐 **Web Browsing** - Open popular websites (YouTube, Google, Stack Overflow)
- 🎵 **Music Player** - Play music from your local directory
- 📰 **News Headlines** - View latest news from Times of India
- ⏰ **Time Display** - Get current time in spoken and text format
- 💻 **Application Launcher** - Open VS Code and other applications
- 📋 **Smart Command Routing** - Intelligent keyword-based command processing
- 🔒 **Secure Configuration** - Environment-based API key management

---

## 📋 Prerequisites

- Python 3.8 or higher
- Microphone for voice input
- Internet connection (for API calls)
- Windows 10+ / macOS / Linux

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/SHUBHI289/Personal-AI-Voice-Assistant.git
cd Personal-AI-Voice-Assistant
```

### 2. Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root directory and add your API keys:

```bash
# .env file
WEATHER_API_KEY=your_openweathermap_api_key_here
MUSIC_DIR=/path/to/your/music/directory
```

#### Getting API Keys:

1. **OpenWeatherMap API Key**:
   - Visit: https://openweathermap.org/api
   - Sign up for a free account
   - Generate an API key from your account dashboard
   - Add it to the `.env` file

2. **Music Directory**:
   - Set the path to your local music folder
   - Example on Windows: `MUSIC_DIR=D:\Music`
   - Example on macOS/Linux: `MUSIC_DIR=/Users/username/Music`

---

## 🎯 Usage

### Start the Assistant

```bash
python NOVA.py
```

### Available Voice Commands

| Command | Example | Action |
|---------|---------|--------|
| **Wikipedia Search** | "wikipedia python" | Searches and reads Wikipedia summary |
| **Weather** | "weather" | Asks for city name and provides weather info |
| **Open Websites** | "open youtube" | Opens YouTube in browser |
| | "open google" | Opens Google search |
| | "open stackoverflow" | Opens Stack Overflow |
| **Time** | "the time" | Announces current time |
| **Music** | "play music" | Plays first song from music directory |
| **News** | "news" | Opens latest news headlines |
| **VS Code** | "open code" | Launches Visual Studio Code |
| **Exit** | "exit" or "quit" | Stops the assistant |

---

## 📁 Project Structure

```
Personal-AI-Voice-Assistant/
├── NOVA.py                  # Main voice assistant application
├── multilang.py             # Multi-language support (Flask-based)
├── requirements.txt         # Project dependencies
├── .env.example            # Example environment variables
├── .gitignore              # Git ignore file
├── README.md               # Project documentation
└── __pycache__/            # Python cache (auto-generated)
```

---

## 🔧 Technology Stack

### Core Libraries
- **pyttsx3** - Text-to-speech synthesis (cross-platform)
- **speech_recognition** - Voice-to-text conversion using Google API
- **wikipedia** - Wikipedia API wrapper for searching and summarization
- **requests** - HTTP library for API calls
- **python-dotenv** - Environment variable management

### External APIs
- **Google Speech-to-Text API** - Voice command recognition
- **OpenWeatherMap API** - Real-time weather data
- **Wikipedia API** - Information retrieval and summarization

### Additional Tools
- **Flask** - Web framework (for multi-language support)
- **Flask-Babel** - Internationalization support

---

## 🔒 Security Features

- ✅ **API Key Protection** - Credentials stored in `.env` file (not in version control)
- ✅ **Environment Variable Management** - Uses `python-dotenv` for secure configuration
- ✅ **Error Handling** - Comprehensive exception handling for API failures
- ✅ **Timeout Protection** - Request timeouts to prevent hanging
- ✅ **.gitignore Configuration** - Sensitive files excluded from Git

---

## 🛠️ Configuration Guide

### Customizing Voice Settings

Edit the voice engine settings in `NOVA.py`:

```python
engine.setProperty('rate', 150)  # Speed of speech (default: 200)
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)
```

### Adding New Commands

1. Add a new conditional block in the `main()` function:

```python
elif 'your_command' in query:
    speak("Performing your command")
    # Your command logic here
```

2. Update the available commands list in the `main()` function
3. Test the new command

### Changing Speech Language

Modify the language code in `take_command()` function:

```python
query = recognizer.recognize_google(audio, language='es-ES')  # Spanish
query = recognizer.recognize_google(audio, language='fr-FR')  # French
```

---

## 📊 Troubleshooting

### Issue: "Microphone not detected"
**Solution**: Ensure your microphone is connected and set as the default input device in system settings.

### Issue: "ModuleNotFoundError: No module named..."
**Solution**: Run `pip install -r requirements.txt` in your virtual environment.

### Issue: "WEATHER_API_KEY not found in environment variables"
**Solution**: Create a `.env` file with your OpenWeatherMap API key (see Installation section).

### Issue: "Speech recognition not working"
**Solution**: 
- Check your internet connection (Google Speech API requires internet)
- Ensure microphone permissions are granted
- Try speaking more clearly

### Issue: "No voices available for text-to-speech"
**Solution**: 
- On Windows: Install text-to-speech engines from Settings > Accessibility > Speech
- On macOS: System already has voices installed
- On Linux: Install `espeak` via package manager

---

## 🚀 Future Enhancements

- [ ] **Natural Language Processing (NLP)** - Better command understanding using BERT/GPT models
- [ ] **Machine Learning** - Learn user preferences and personalize responses
- [ ] **Database Integration** - Store interaction history and user preferences
- [ ] **Smart Home Control** - Integrate with IoT devices (lights, thermostats)
- [ ] **Email Integration** - Send emails via voice commands
- [ ] **Calendar Integration** - Schedule meetings and reminders
- [ ] **Mobile App** - Cross-platform mobile application
- [ ] **Local Speech Recognition** - Privacy-focused offline speech processing using Vosk
- [ ] **Multi-language Support** - Automatic language detection and switching
- [ ] **GUI Interface** - Desktop application with graphical interface

---

## 📝 Code Examples

### Adding a New API Integration

```python
def get_stock_price(symbol: str) -> None:
    """Fetch stock price for a given symbol."""
    try:
        api_key = os.getenv('STOCK_API_KEY')
        url = f"https://api.example.com/quote?symbol={symbol}&apikey={api_key}"
        response = requests.get(url, timeout=5)
        data = response.json()
        price = data.get('price')
        speak(f"The current price of {symbol} is ${price}")
    except Exception as e:
        logger.error(f"Error fetching stock price: {e}")
        speak("Could not fetch stock information.")
```

### Adding Error Recovery

```python
def retry_operation(func, max_retries=3, delay=1):
    """Retry a function with exponential backoff."""
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(delay * (2 ** attempt))
            else:
                raise e
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**Shubhi Gupta**
- GitHub: [@SHUBHI289](https://github.com/SHUBHI289)
- Email: [Add your email if desired]

---

## 🙏 Acknowledgments

- **pyttsx3** - Cross-platform text-to-speech library
- **SpeechRecognition** - Voice recognition library
- **OpenWeatherMap** - Weather data provider
- **Wikipedia** - Information source
- **Flask** - Web framework

---

## 📞 Support

If you encounter any issues, please:
1. Check the troubleshooting section
2. Review the GitHub issues
3. Create a new issue with detailed description

---

## ⭐ Show Your Support

If you find this project helpful, please consider:
- Giving it a star ⭐
- Sharing it with others
- Contributing improvements
- Reporting bugs and suggesting features

---

**Last Updated**: 2024  
**Python Version**: 3.8+  
**Status**: Active Development
