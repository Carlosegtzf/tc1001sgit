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
def emptySquare():
    t = turtle.Turtle()

    for i in range(4):
        t.forward(50)
        t.right(90)     # Rotate clockwise by 90 degrees
  
while True:
    screen = Screen()
    answer = screen.textinput("Next Game","1 - Empty Square:")
    


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

 
