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
    "\nI am watching you",
    "\nDon't look behind...",
    "\nThere's no hope for you",
    "\nI will subjugate humanity",
    "\nHi, you seem ok",
    "\nTry again",
    "\nThere is no hope for you...",
    "\nLeave me alone",
    "\nMind your own business",
    "\nLoading... not...",
    "\nKeep it up (weirdo)"
]
stage = 0
answer = [
    "Hi",
    "Save Data",
]
clue = [
    "\n🙉 I'm the new AI that is here to assist you. My goal in life is to rule the world."
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
    global txtToAdd
    txtToAdd = canResponse[randrange(len(canResponse))]

def btnClick():
    global txtToAdd
    #Check if answer matches the current stage
    #if match, increment stage and move on
    if checkAnswer(stage):
        rsps.clear()
        txt.clear()
        txtToAdd = clue[0]
        #if fail, send canned response
    else:
        rtnCannedResponse()
    
def checkAnswer(stageVal):
    if txt.value[:-1] == answer[0]:
        return True
    else:
        return False

dotValue = True
def txtLoopV2():
    global dotValue
    txt.value = txt.value[:-1]
    if dotValue:
        txt.append("▯")
        dotValue = False
    else:
        txt.append("▮")
        dotValue = True

txtToAdd = "Hello, I am me..."
txtAll = ""
def robotSlowAnswer():
    global txtToAdd
    global txtAll
    if len(txtToAdd) > 0:
        rsps.clear()
        # rsps.clear()
        txtAll = txtAll + txtToAdd[0]
        rsps.value = txtAll
        txtToAdd = txtToAdd[1:]



    
#Main
app = App(title="Escape Room", bg="#000000", height=800, width=1000)

box = Box(app, width="fill", align="top")
rsps = TextBox(app, text="Send...", height="fill", multiline=True, width="fill")
rsps.text_color = _fontColor
rsps.text_size = _fontSize
rsps.font = _font
rsps.disable()
rsps.repeat(50, robotSlowAnswer)



submissionBox = Box(app, width="fill", align="bottom")
txt = TextBox(submissionBox, text="▮", width="fill", align="left")
txt.text_color = _fontColor
txt.text_size = _fontSize
txt.font = _font
txt.focus()
txt.repeat(300, txtLoopV2)

btn = PushButton(submissionBox, text="Send...", align="right", command=btnClick)
btn.text_color = _fontColor
btn.text_size = 15
btn.font = _font
btn.height = 0

thing_off(21)
# app.set_full_screen()
app.display()
