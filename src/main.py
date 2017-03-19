import pygame, os, pygame, random, time, sys
from car import *
from game import *
from road import *
from pothole import *
from menu import *

# Global Variables
height = 680
width = 600

escape = False
gameplay = True

def main():
	# Window Position Initialization
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	# Initialize Pygame
	pygame.init()
	
	
	screen = pygame.display.set_mode((width,height), pygame.NOFRAME)
	pygame.display.set_caption("Spot the Pot (c) 2017")
	pygame.event.set_blocked(pygame.MOUSEMOTION)
	holelist = []
	hole_counter = 0
	BLACK = (0,0,0)
	WHITE = (255,255,255)
	
	initial_draw = True
	main_menu = True
	
	exit = False
	
	menu(screen)
   
   
	
	draw_title_screen(screen)	
	
	while main_menu:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				os._exit(-1)
			if event.type == pygame.KEYDOWN:
				handle_menu_keydown()
				main_menu = False

	
	
def menu(screen):
	# Menu Stuff
	menu = cMenu(width/2+15, height - 175, 10, 75, 'vertical', 3, screen,
               [('Start Game', 1, None),
                ('Options',    2, None),
                ('Exit',       3, None)])
				
	# Center the menu on the draw_surface (the entire screen here)
	menu.set_center(True, False)

	# Center the menu on the draw_surface (the entire screen here)
	menu.set_alignment('center', 'center')

	# Create the state variables (make them different so that the user event is
	# triggered at the start of the "while 1" loop so that the initial display
	# does not wait for user input)
	state = 0
	prev_state = 1

	# rect_list is the list of pygame.Rect's that will tell pygame where to
	# update the screen (there is no point in updating the entire screen if only
	# a small portion of it changed!)
	rect_list = []
	
	# Load background image
	bkg = pygame.image.load('main_menu.png')
	
	screen.blit(bkg, (0, 0))
	pygame.display.flip()
   
	# The main while loop
	while 1:
		# Check if the state has changed, if it has, then post a user event to
		# the queue to force the menu to be shown at least once
		if prev_state != state:
			pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
			prev_state = state

		# Get the next event
		e = pygame.event.wait()

		# Update the menu, based on which "state" we are in - When using the menu
		# in a more complex program, definitely make the states global variables
		# so that you can refer to them by a name
		if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
			if state == 0:
				rect_list, state = menu.update(e, state)
			elif state == 1:
				# Set Key Repeat
				pygame.key.set_repeat(10, 10)
				game(screen)
				# remove Key Repeat
				pygame.key.set_repeat()	
				screen.blit(bkg, (0, 0))
				pygame.display.flip()
				state = 0
			elif state == 2:
				print 'Options!'
				state = 0				
			else:
				pygame.quit()
				sys.exit()

		# Quit if the user presses the exit button
		if e.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		# Update the screen
		pygame.display.update(rect_list)
		
def game(screen):
	global gameplay
	while gameplay:		
		game = Game(width, height)		
		loop = True
		while loop:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					os._exit(-1)
				if event.type == pygame.KEYDOWN:
					handle_keydown(game)
			draw(screen, game)
			loop = update(game)
			if(not loop):
				break
			if escape:
				while escape:
					print "paused"
		game.gameOverState = True
		gameplay = False

def getDrawRectFromCollisionRect(rect, n): #Not tested, may not be working right?
	drawrect = pygame.Rect(rect.x - n, rect.y - n, rect.width + 2*n, rect.height + 2*n)
	return drawrect

def draw(screen, game):
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
	global escape
	keylist = pygame.key.get_pressed()
	if(keylist[pygame.K_ESCAPE]):
		escape is not escape
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

# Run the script
if __name__ == "__main__":
   main()