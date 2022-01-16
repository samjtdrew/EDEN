#AUDIO LISTENER
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import speech_recognition as sr


#def transcript(path):
#    sound = AudioSegment.from_wav(path)
#    chunks = split_on_silence(sound, min_silence_len = 500, silence_thresh = sound.dBFS-14, keep_silence=500)
#    if not os.path.isdir(mwd + "/SYSTEM/SpeechRecognition/audio-chunks"):
#        os.makedirs(mwd + "/SYSTEM/SpeechRecognition/audio-chunks")
#    whole_text = ""
#    for i, audio_chunk in enumerate(chunks, start=1):
#        chunk_filename = os.path.join(mwd + "/SYSTEM/SpeechRecognition/audio-chunks", f"chunk{i}.wav")
#        audio_chunk.export(chunk_filename, format="wav")
#        with sr.AudioFile(chunk_filename) as source:
#            audio_listened = r.record(source)
#            try:
#                text = r.recognize_google(audio_listened)
#            except sr.UnknownValueError as errortype:
#                print(">> ERROR - " + str(errortype))
#            else:
#                text = f"{text.capitalize()}. "
#                print(chunk_filename, ":", text)
#                whole_text += text
#    return whole_text

#def listen(length):
#    with sr.Microphone() as source:
#        print(">> Listening")
#        audio_data = r.record(source, duration=length)
#        print(">> Synthesizing Speech")
#        text = r.recognize_google(audio_data, language="en-US")
#        print(text)


##locate directorys
#cwd = os.getcwd()
#cwd = cwd.replace("\\", "/")
#os.chdir("../")
#mwd = os.getcwd()
#mwd = mwd.replace("\\", "/")
#os.chdir(cwd)

#filename = mwd + "/SYSTEM/SpeechRecognition/16-122828-0002.wav"

##initialise the speech recognizer
#r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour()
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-US')
            print(f"user said:{statement}\n")
        except Exception as e:
            speak("Please repeat")
            return "None"
        return statement


pid = os.getpid()
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')