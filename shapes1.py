import turtle
from turtle import *
from turtle import Screen
    
def emptySquare():
    pass  # TODO
    
def filledSquare():
  pass  # TODO

def emptyCircle():
    t = turtle.Turtle()
    t.circle(100)
    
def filledCircle():
    t= turtle.Turle()
    t.fillcolor('red')
    t.begin_fill()
    t.circle(100)
    t.end_fill()
  
while True:
    screen = Screen()
    answer = screen.textinput("Next Game","1 - Empty Square:")
    answer = screen.textinput("Next Game","2 - Filled Square:")
    answer = screen.textinput("Next Game","3 - Empty Circle:")
    answer = screen.textinput("Next Game","4 - Filled Circle:")

    if (answer is None):
        break
    elif (answer == '1'):
        emptySquare()
    elif (answer == '2'):
        filledSquare()
    elif (answer == "3"):
        emptyCircle()
    elif (answer == "4"):
        filledCircle()
 
