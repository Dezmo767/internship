#!/usr/bin/env python3

import turtle
import os

#Create a Window

wn = turtle.getscreen()
wn.bgcolor("black")
wn.setup(700,700)
wn.title("A Game")

#Create Pen

class Pen(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.color("white")
		self.penup()
		self.speed(0)

#Create levels list
levels = [""]

#Define fist level
level_1 = ["XXXXXXXXXXXXXXXXXXXXXXXXXX",
		   "X     XXXXXXXXXXXX       X",
		   "X      XXXXXXXXXXX       X",
		   "X       XXXXXXXXX    XXXXX",
		   "X       XXXXXXXXX    XXXXX",
		   "XXX                  XXXXX",   
		   "XXXX   XXX     XXX    XXXX",
		   "XXXX    X       X     XXXX",
		   "XXXX   XXX     XXX    XXXX",
		   "XXXXXX                XXXX",
		   "XXXXXXX     XX        XXXX",
		   "XXXXXXXXX   XX        XXXX",
		   "XXXXX   X        X    XXXX",
		   "XXXXX    XXXXXXXX     XXXX",
		   "XXXXXXXXXX            XXXX",
		   "XXXXXXXXXX            XXXX",              
		   "XXXXXXXXXX               X",
		   "XXXXXX                 XXX",
		   "XXXXXXXX                XX",
		   "XXXXXXX                 XX",
		   "XXXXXXXX             XXXXX",
		   "XXXXXXXXXXX           XXXX",
		   "XXXXXXXXXXXXXX   X   X   X",
		   "XXXXXXXXXXXXX    XX  X  XX"]

#Add maze to mazes list
levels.append(level_1)

#Create Level Setup Function
def setup_maze(level):
	for y in range(len(level)):
		for x in range(len(level[y])):
			#Get the character at each x,y coordinate
			#Note the order of y and x in the next line
			character = level[y][x]
			#Calculate the screen x,y coordinates
			screen_x = -288 + (x * 24)
			screen_y = 288 - (y * 24)
			
			#Check if it is an X (Representing a Wall)
			if character == "X":
				pen.goto(screen_x, screen_y)
				pen.stamp()

#Create Class instances
pen = Pen()

#Set up the level
setup_maze(levels[1])

#Main Game Loop
while True:
	pass









