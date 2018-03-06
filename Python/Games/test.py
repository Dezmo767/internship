#!/usr/bin/env python3
#Import same moduls
import pygame
import time
import random

pygame.init()

#Farben Def
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,155,0)
blue = (0,0,255)

display_w = 800
display_h = 600

gameDisplay = pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption("A Snake Game")


block_size = 10
FPS = 30

font = pygame.font.SysFont(None, 25)
clock = pygame.time.Clock()

def snake(block_size, snakelist):
	for XnY in snakelist:
		
		pygame.draw.rect(gameDisplay, green,[XnY[0],XnY[1],block_size,block_size])
	

def messag_to_screen(msg,color):
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text, [display_w/2, display_h/2])
	


def game_loop():
	
	gameExit = False
	gameOver = False

	lead_x = display_w/2
	lead_y = display_h/2
	lead_x_change = 0
	lead_y_change = 0
	
	snakelist = []
	snakeLength = 1
	
	
	randAppleX = round(random.randrange(0, display_w - block_size)/10.0)*10.0
	randAppleY = round(random.randrange(0, display_h - block_size)/10.0)*10.0

	while not gameExit:
		while gameOver == True:
			gameDisplay.fill(white)
			messag_to_screen("Game over, Press c to play again or q to Quit", red)
			pygame.display.update()
			
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_c:
						game_loop()
					
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -block_size
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					lead_x_change = block_size
					lead_y_change = 0
				elif event.key == pygame.K_UP:
					lead_y_change = -block_size
					lead_x_change = 0
				elif event.key == pygame.K_DOWN:
					lead_y_change = block_size
					lead_x_change = 0
			if lead_x > display_w or lead_x < 0 or lead_y > display_h or lead_y < 0:
				gameOver = True
			
					
		lead_x += lead_x_change
		lead_y += lead_y_change
				
		
				
				
		gameDisplay.fill(white)
		AppleThickness = 10
		pygame.draw.rect(gameDisplay, red,[randAppleX,randAppleY,AppleThickness ,AppleThickness ])
		
		
		snakehead = []
		
		snakehead.append(lead_x)
		snakehead.append(lead_y)
		
		snakelist.append(snakehead)
		
		if len(snakelist) > snakeLength:
			del snakelist[0]
		for eachSegment in snakelist[:-1]:
			if eachSegment == snakehead:
				gameOver = True
		
		snake(block_size, snakelist)
		
		
		"""if lead_x == randAppleX and lead_y == randAppleY:
			randAppleX = round(random.randrange(0, display_w - block_size)/10.0)*10.0
			randAppleY = round(random.randrange(0, display_h - block_size)/10.0)*10.0
			snakeLength += 2"""
		if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
			if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
				randAppleX = round(random.randrange(0, display_w - block_size)/10.0)*10.0
				randAppleY = round(random.randrange(0, display_h - block_size)/10.0)*10.0
				snakeLength += 2
			
			
		
		pygame.display.update()
		
		#Frames per Second
		clock.tick(FPS)
	

	pygame.quit()
	quit()
game_loop()

