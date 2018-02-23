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

#Create a Border
border_pen = turtle.Turtle()
border_pen.setposition(-300,300)
border_pen.penup()
border_pen.speed(0)
border_pen.pensize(3)
for side in range(4):
        border_pen.pendown()
        border_pen.pencolor("white")
        border_pen.fd(600)
        border_pen.right(90)

border_pen.hideturtle()

#Create Player
Player = turtle.Turtle()
Player.setposition(0, -280)
Player.color("Blue")
Player.shape("triangle")
Player.setheading(90)
Player.penup()

playerspeed = 15
#Create Controlls left and right
def move_left():
        x = Player.xcor()
        x -= playerspeed
        if x < -280:
                x = -280
        Player.setx(x)

def move_right():
        x = Player.xcor()
        x += playerspeed
        if x > 280:
                x = 280
        Player.setx(x)

def move_up():
        y = Player.ycor()
        y += playerspeed
        if y > 280:
                y = 280
        Player.sety(y)

def move_down():
        y = Player.ycor()
        y -= playerspeed
        if y < -280:
                y = -280
        Player.sety(y)


#Key bindings
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_up, "Up")
turtle.onkeypress(move_down, "Down")

#display = input("Press Enter to Start the Game")

