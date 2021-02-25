#! /usr/bin/env python3

#icon attribution: <div>Icons made by <a href="https://www.flaticon.com/authors/alfredo-hernandez" title="Alfredo Hernandez">Alfredo Hernandez</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

from guizero import App, Text, TextBox, Picture, Box, PushButton
from random import randrange
import time

piEnvironment = False

if piEnvironment:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)

#Settings Variables
_font = "Courier"
_fontSize = 20
_fontColor = "#0dc900"

#Variables
canResponse = [
    "I am watching you",
    "Don't look behind...",
    "There's no hope for you",
    "I will subjugate humanity",
    "Hi, you seem ok",
    "Try again",
    "There is no hope for you...",
    "Leave me alone",
    "Mind your own business",
    "Loading... not...",
    "Keep it up (weirdo)"
]
stage = 0
answer = [
    "Hi",
    "Save Data",
]
clue = [
    "Hello! I'm the new AI that is here to assist you. My goal in life it to rule the world."
]



#Functions
def say_my_name():
    welcome_message.value = my_name.value

def thing_on(pin):
    if piEnvironment:
        GPIO.output(pin, GPIO.LOW)

def thing_off(pin):
    if piEnvironment:
        GPIO.output(pin, GPIO.HIGH)

def rtnCannedResponse():
    rsps.append(canResponse[randrange(len(canResponse))])

def btnClick():
    print("button was clicked")
    #Check if answer matches the current stage
    #if match, increment stage and move on
    if checkAnswer(stage):
        rsps.append(clue[0])
        #if fail, send canned response
    else:
        rtnCannedResponse()
    
def checkAnswer(stageVal):
    if txt.value == answer[0]:
        return True
    else:
        return False
    
#Main
app = App(title="Escape Room", bg="#000000")

box = Box(app, width="fill", align="top")
rsps = TextBox(app, text="Send...", height="fill", multiline=True, width="fill")
rsps.text_color = _fontColor
rsps.text_size = _fontSize
rsps.font = _font
rsps.disable()



submissionBox = Box(app, width="fill", align="bottom")
txt = TextBox(submissionBox, text="type here", width="fill", align="left")
txt.text_color = _fontColor
txt.text_size = _fontSize
txt.font = _font

btn = PushButton(submissionBox, text="Send...", align="right", command=btnClick)
btn.text_color = _fontColor
btn.text_size = 15
btn.font = _font
btn.height = 0

thing_off(21)
app.set_full_screen()
app.display()
