#! /usr/bin/env python3

#icon attribution: Uicons by <a href="https://www.flaticon.com/uicons">Flaticon</a>

from guizero import App, Text, TextBox, PushButton, Slider, Picture, Waffle
import RPi.GPIO as GPIO
import time

#Variables
One = "white"
Two = "red"
Three = "green"

solution = [
    [One, One, One],
    [One, Two, Two],
    [One, One, Three]]

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)


#Functions
def say_my_name():
    welcome_message.value = my_name.value
def togglePixel(x,y):
    if waffle.get_pixel(x,y) == One:
        waffle[x,y].color = Two
    elif waffle.get_pixel(x,y) == Two:
        waffle[x,y].color = Three
    else:
        waffle[x,y].color = One
def waffleClick(x,y):
    print("x,y : " + str(x) + "," + str(y))
    togglePixel(x,y)
    print(waffle.get_all())
    print(solution)
    checkSolution()
def checkSolution():
    thing_off(21)
    if solution == waffle.get_all():
        message.value = "Success"
        thing_on(21)
    else:
        message.value = "un-Success"
        thing_off(21)

def thing_on(pin):
    GPIO.output(pin, GPIO.LOW)
def thing_off(pin):
    GPIO.output(pin, GPIO.HIGH)


    
    
#Main
app = App(title="Hello world")

message = Text(app, text="hmmm", size=40, font="Times New Roman", color="black")

waffle = Waffle(app, dotty=True, pad=20, dim=50, command=waffleClick)

thing_off(21)
app.set_full_screen()
app.display()
