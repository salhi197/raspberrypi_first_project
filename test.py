# -*- coding: utf8 -*
import pyttsx3
engine = pyttsx3.init()
voice = engine.getProperty('voices')[0] # the french voice
engine.setProperty('voice', voice.id)

engine.say('Siiifou ') # it works!!

engine.runAndWait()    
