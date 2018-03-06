#!/usr/bin/env python3
#Import same moduls
import os
import sys
import turtle

#Create a Window
wn = turtle.getscreen()
wn.bgcolor("black")
wn.setup(700,700)
wn.title("That Good Game")

#Create a Help Window


#Create a Border
border_pen = turtle.Turtle()
border_pen.setposition(-300,-300)
border_pen.penup()
border_pen.speed()
border_pen.pensize(3)
border_pen.pencolor("red")
border_pen.pendown()
border_pen.fd(600)
for side in range(3):
        border_pen.pencolor("white")
        border_pen.left(90)
        border_pen.fd(600)
		
border_pen.hideturtle()

#Create a Shape for Player


#Create Player
Player = turtle.Turtle()
Player.setposition(0, -280)
Player.color("Blue")
Player.shape("")
Player.setheading(90)
Player.penup()

playerspeed = 20

#Create Controlls
def move_left():
        x = Player.xcor()
        x -= playerspeed
        if x < -285:
                x = -285
        Player.setx(x)

def move_right():
        x = Player.xcor()
        x += playerspeed
        if x > 285:
                x = 285
        Player.setx(x)
        
	
def game_exit():
	exit()



#Key bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(game_exit, "Escape")


#Window hold
print("Keys: Arrows to move and w to draw")
print("")
print("Space to stop drawing, ESC to exit the Game")
print("")
display = input("Press Escape to close the Game")

