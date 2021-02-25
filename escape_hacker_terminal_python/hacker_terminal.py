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



#Functions
def say_my_name():
    welcome_message.value = my_name.value

def thing_on(pin):
    if piEnvironment:
        GPIO.output(pin, GPIO.LOW)

def thing_off(pin):
    if piEnvironment:
        GPIO.output(pin, GPIO.HIGH)

def btnClick():
    print("button was clicked")
    computerRespond()
    # Text(box, font=_font, text="something", size=_fontSize, color=_fontColor, align="left")
#     textyBox.append("""\
# Hey""")

def computerRespond():
    textyBox.append(canResponse[randrange(len(canResponse))])
    
    
#Main
app = App(title="Escape Room", bg="#000000")

# message = Text(app, text="hmmm", size=40, font="Times New Roman", color="white")

box = Box(app, width="fill", align="top")
# body = Text(box, font=_font, text="hi", size=_fontSize, color=_fontColor, align="left")
textyBox = TextBox(app, text="Send...", height=15, multiline=True, width="fill")
textyBox.text_color = _fontColor
textyBox.text_size = _fontSize
textyBox.font = _font
textyBox.disable()



submissionBox = Box(app, width="fill", align="bottom")
text = TextBox(submissionBox, text="type here", width="fill", align="left")
text.text_color = _fontColor
text.text_size = _fontSize
text.font = _font

btn = PushButton(submissionBox, text="Send...", align="right", command=btnClick)
btn.text_color = _fontColor
btn.text_size = 15
btn.font = _font
btn.height = 0

thing_off(21)
# app.set_full_screen()
app.display()
