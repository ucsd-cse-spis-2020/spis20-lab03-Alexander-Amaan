#1. The anonymous turtle is the turtle that was not explicitly defined, yet it still exists when called in commands like turtle.forward(100).
#2 Turtle() is a special function that creates the new turtle object, while turtle calls the library turtle. 
#3 Just call left(90) and then move myTurtle forward 100. myTurtle.left(90), myTurtle.forward(100) or myTurtle.sety(100)

import turtle
#turtle.forward(100)
myTurtle = turtle.Turtle()

def drawA(theTurtle, size):
	theTurtle.pensize(size)
	theTurtle.left(70)
	theTurtle.forward(200)
	theTurtle.right(140)
	theTurtle.forward(200)
	theTurtle.left(180)
	theTurtle.forward(100)
	theTurtle.left(90)
	theTurtle.forward(90)