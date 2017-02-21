import pygame
import os
from car import *
from game import *
import pygame
import random
import time
from road import *
from pothole import *

height = 680
width = 600
os.environ['SDL_VIDEO_WINDOW_POS'] = "25,25"
pygame.init()
pygame.key.set_repeat(10,10)
screen = pygame.display.set_mode((width,height))
holelist = []
hole_counter = 0

def draw(game):
	#screen.fill(game.background_color)
	screen.blit(game.road.image, (game.road.x,game.road.y))
	screen.blit(game.road.image, (game.road.x,game.road.y2))
	screen.blit(game.road.image, (game.road.x,game.road.y3))
	for hole in game.holelist:
		screen.blit(hole.image, (hole.x, hole.y))
	screen.blit(game.car.image, (game.car.x,game.car.y))
	screen.blit(game.scoreSurface, (10, 10))
	pygame.display.flip()

def update(game):
	game.road.moveDown()
	game.hole_counter += 1
	if(game.hole_counter > 400):
		game.holelist.append(Pothole(game.road.x, game.road.x + game.road.width))
		game.hole_counter = 0
	for hole in game.holelist:
		hole.moveDown()
	return 1
	
def handle_keydown(game):
	keylist = pygame.key.get_pressed()
	if(keylist[pygame.K_LEFT]):
		game.car.moveLeft()
	if(keylist[pygame.K_RIGHT]):
		game.car.moveRight()

while 1:		
	game = Game(width, height)		
	loop = 1
	while loop == 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				os._exit(-1)
			if event.type == pygame.KEYDOWN:
				handle_keydown(game)
		draw(game)
		loop = update(game)
		if(loop == 0):
			break