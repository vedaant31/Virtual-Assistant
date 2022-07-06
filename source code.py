from cProfile import run
from distutils.cmd import Command
from multiprocessing.connection import Listener
import re
import speech_recognition as sr
import pyttsx3
Listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    #engine.say('I am Vedaant')
    #engine.say('what can i do for you')
    engine.runAndWait()
def take_Command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice=Listener.listen(source)
            Command=Listener.recognize_google(voice)
            Command=Command.lower()
            if 'alexa' in Command:
                Command=Command.replace('alexa','')
                print(Command)
            
    except:
        pass
    return Command

def run_alexa():
    Command=take_Command()
    if 'play' in Command:
        talk('playing')
        print('playing')


run_alexa()

