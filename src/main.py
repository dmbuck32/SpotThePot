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
screen = pygame.display.set_mode((width,height),pygame.DOUBLEBUF)
holelist = []
hole_counter = 0
initial_draw = True

def getDrawRectFromCollisionRect(rect, n): #Not tested, may not be working right?
	drawrect = pygame.Rect(rect.x - n, rect.y - n, rect.width + 2*n, rect.height + 2*n)
	return drawrect

def draw(game):
	rects = []
	if game.initDraw:
		screen.blit(game.road.image, (game.road.x,game.road.y))
		pygame.display.flip()
		game.initDraw = False 
	screen.blit(game.road.image, (game.road.x,game.road.y))
	for hole in game.holelist:
		rects.append(screen.blit(hole.image, (hole.x, hole.y)))
	rects.append(screen.blit(game.car.image, (game.car.x,game.car.y)))
	rects.append(screen.blit(game.scoreSurface, (10, 10)))
	rects.append(screen.blit(game.livesSurface, (10, 35)))
	if(game.gameOverState):
		rects.append(screen.blit(game.gameOverSurface, (10, 60)))
	pygame.display.update(rects)

def update(game):
	game.hole_counter += 1
	if(game.hole_counter > 400):
		game.holelist.append(Pothole(game.road.lbound, game.road.rbound))
		game.hole_counter = 0
	for hole in game.holelist:
		hole.moveDown()
		if hole.y > game.height:
			game.holelist.remove(hole)
	if game.car.collided(game.holelist):
		game.updateLives()
	if game.lives == 0:
		return 0
	return 1
	
def handle_keydown(game):
	keylist = pygame.key.get_pressed()
	if(keylist[pygame.K_LEFT]):
		if(game.car.x > game.road.lbound):
			game.car.moveLeft()
	if(keylist[pygame.K_RIGHT]):
		if(game.car.x + game.car.width < game.road.rbound):
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
	game.gameOverState = True
	draw(game)
	time.sleep(5)