#SOS Morse Code challenge - 101computing.net/morse-code-encoder/
import turtle
import time

#Initalise the turtle
myPen = turtle.Turtle()
myPen.speed(0)
myPen.shape("arrow")
myPen._delay(0)
myScreen = turtle.Screen()
myScreen.bgcolor("#000055")
myPen.penup()
myPen.goto(0,-100)
myPen.pendown()

#Function to switch off the light for a given duration in ms.
def switchOn(duration):
  myPen.color("#FFFF55")
  myPen.begin_fill()
  myPen.circle(100)
  myPen.end_fill()
  myPen._delay(duration)
  myPen.color("#FFFF55")
  myPen._delay(0)  

#Function to switch off the light for a given duration in ms.
def switchOff(duration):
  myPen.color("#000055")
  myPen.begin_fill()
  myPen.circle(100)
  myPen.end_fill()
  myPen._delay(duration)
  myPen.color("#000055")
  myPen._delay(0) 

#################### Main Program Starts Here ##########################################################
#Just turning on and off the lights to create the following sequence: ... --- ... (SOS in Morse Code)
#Letter "S" - Morse Code: ...
switchOn(500) #Light is On for 500ms (half a second = dot)
switchOff(500) #Light is Off for 500ms
switchOn(500) #Light is On for 500ms (half a second = dot)
switchOff(500) #Light is Off for 500ms
switchOn(500) #Light is On for 500ms (half a second = dot)
switchOff(1500) #Light is Off for 1500ms (space between two letters - duration three times the duration of a dot)
#Letter "O" - Morse Code: ---
switchOn(1500) #Light is On for 1500 seconds (A dash is three times the duration of a dot)
switchOff(500) #Light is Off for 500ms
switchOn(1500) #Light is On for 1500 seconds (A dash is three times the duration of a dot)
switchOff(500) #Light is Off for 500ms
switchOn(1500) #Light is On for 1500 seconds (A dash is three times the duration of a dot)
switchOff(1500) #Light is Off for 1500ms
#Letter "S" - Morse Code: ...
switchOn(500) #Light is On for 500ms (half a second = dot)
switchOff(500) #Light is Off for 500ms
switchOn(500) #Light is On for 500ms (half a second = dot)
switchOff(500) #Light is Off for 500ms
switchOn(500) #Light is On for 500ms (half a second = dot)
switchOff(1500) #Light is Off for 500ms

###############################################################################################
# Your challenge consists of replacing this code to ask the user to type a message            #
# our program will convert this message into Morse code                                       #
# Your program should then create the corresponding light signals.                            #
###############################################################################################


#Leave this instruction at the end of your program.
myPen.getscreen().update()	