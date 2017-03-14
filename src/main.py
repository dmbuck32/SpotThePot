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
os.environ['SDL_VIDEO_WINDOW_POS'] = "100,100"
pygame.init()
pygame.key.set_repeat(10,10)
screen = pygame.display.set_mode((width,height),pygame.DOUBLEBUF)
holelist = []
hole_counter = 0
initial_draw = True
pause_menu = False
main_menu = True
gameplay = True
exit = False
BLACK = (0,0,0)
WHITE = (255,255,255)

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
	game.updateScoreCounter()
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
	if(keylist[pygame.K_ESCAPE]):
		pause_menu = not pause_menu
	if(keylist[pygame.K_LEFT]):
		if(game.car.x > game.road.lbound):
			game.car.moveLeft()
	if(keylist[pygame.K_RIGHT]):
		if(game.car.x + game.car.width < game.road.rbound):
			game.car.moveRight()
			
def handle_menu_keydown():
	keylist = pygame.key.get_pressed()
	if (keylist[pygame.K_UP]):
		main_menu = False
	if (keylist[pygame.K_DOWN]):
		main_menu = False
			
def draw_title_screen(screen):
	font = pygame.font.Font('Square.ttf', 40)
	titleScreen = font.render('Spot The Pot', False, WHITE)
	titleRect = titleScreen.get_rect()
	titleRect.center = (width/2, 150)
	font2 = pygame.font.Font('Square.ttf', 20)
	titleScreen2 = font2.render('Press any key to Continue...', False, WHITE)
	titleRect2 = titleScreen2.get_rect()
	titleRect2.center = (width/2, height/2)
	screen.blit(titleScreen, titleRect)
	screen.blit(titleScreen2, titleRect2)
	pygame.display.flip()

draw_title_screen(screen)	
while main_menu:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			os._exit(-1)
		if event.type == pygame.KEYDOWN:
			handle_menu_keydown()
			main_menu = False

while gameplay:		
	game = Game(width, height)		
	loop = True
	while loop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				os._exit(-1)
			if event.type == pygame.KEYDOWN:
				handle_keydown(game)
		draw(game)
		loop = update(game)
		if(not loop):
			break
		if pause_menu:
			draw_title_screen()
	game.gameOverState = True
	draw(game)
	time.sleep(5)