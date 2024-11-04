import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour == 0 and hour<12:
        speak("Good Morning")
    elif hour<18:
        speak("Good Evening")
    else:
        speak("Good Night! Sweet dreams")
    speak("My name is Lucy ! 1001 111 1001 ehhhh 1001 111 1001 11111 1010100 1010100 1010100 1010100 1010100 ")

if __name__ == "__main__":
    wishMe()
    