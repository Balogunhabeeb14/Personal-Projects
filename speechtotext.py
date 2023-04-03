# import the pyttsx module inside program
import pyttsx3

# initializing the module
engine = pyttsx3.init()

import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate')
engine.say('Hi i am an assistant developed by Habeeb ')
engine.runAndWait()