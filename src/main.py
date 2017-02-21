import pygame
import os
from car import *
from game import *
import pygame
import random
import time

os.environ['SDL_VIDEO_WINDOW_POS'] = "25,25"
pygame.init()
screen = pygame.display.set_mode((920,680))

def draw(game):
	screen.fill(game.background_color)
	screen.blit(game.car.image, (game.car.x,game.car.y))
	screen.blit(game.scoreSurface, (10, 10))
	pygame.display.flip()

def update(game):
	return 1
	
def handle_input(game):
	keylist = pygame.key.get_pressed()
	if(keylist[pygame.K_LEFT]):
		game.car.moveLeft()
	if(keylist[pygame.K_RIGHT]):
		game.car.moveRight()

while 1:		
	game = Game()		
	loop = 1
	while loop == 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				os._exit(-1)
			if event.type == pygame.KEYDOWN:
				handle_input(game)
		draw(game)
		loop = update(game)
		if(loop == 0):
			break