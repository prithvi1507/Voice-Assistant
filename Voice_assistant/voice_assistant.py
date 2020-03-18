from ttkthemes import themed_tk as tk
from tkinter import ttk
from time import ctime
import time
import speech_recognition as sr
import pyaudio
import webbrowser
import os
import playsound
import random
import tkinter
from gtts import gTTS


#root
root=tk.ThemedTk()
root.get_themes()
root.set_theme("scidgreen")
root.resizable(0,0)
root.configure(background="white")
root.title("voice Assistant")
#task
def task():
#buttons
task_btn = ttk.Button(root,text="Command",width=10,command=task).grid(row=0,column=0,ipady=20,ipadx=90)
save_btn = ttk.Button(root,text="Exit",width=10,command=root.destroy).grid(row=1,column=0,ipady=20,ipadx=90)

root.mainloop()

def speak(audio_string):
    tts = gTTS(text=audio_string,lang='en')

    r = random.randint(1,1000000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

def record_audio(ask=False):
    r =sr.Recognizer()
    with sr.Microphone as source:
        if ask:
            speak(ask)
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('did not get that sir')
        except sr.RequestError:
            speak('server is down')
        return voice_data
def respond(voice_data):
        if 'name' in voice_data:
            speak('hi,my name is lathika')
        if 'current time' in voice_data:
            speak(ctime())
        if 'search' in voice_data:
            search = record_audio('what do you want to search for ?')
            url = 'https://google.com/search?q='+str(search)
            webbrowser.get().open(url)
            speak("here is what i found for"+str(search))
        if  'find location' in voice_data:
            location = record_audio('which place you want to search for')
            url ='https://google.nl/maps/place'+str(location)
            webbrowser.get().open(url)
            speak("here is your location"+str(location)+'/&amp;')
        if 'exit' in voice_data:
            speak('ok bye take care and a have a great day')
            root.destroy()
def task():
    speak("how can i help you")
    voice_data = record_audio()
    respond(voice_data)
 




