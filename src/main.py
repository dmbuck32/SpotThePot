import pygame, os, pygame, random, time, sys
from car import *
from game import *
from road import *
from pothole import *
from menu import *

# Global Variables
height = 800
width = 480
timeUntilNextObstacle = 0

clk = pygame.time.Clock()
FPS = 120
paused = False

def main():
	# Window Position Initialization
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	# Initialize Pygame
	pygame.init()
	# Initialize Screen
	screen = pygame.display.set_mode((width,height), pygame.NOFRAME)
	pygame.display.set_caption("Spot the Pot (c) 2017")
	# Ignore Mouse movement
	pygame.event.set_blocked(pygame.MOUSEMOTION)
	# Pothole Mechnics
	holelist = []
	hole_counter = 0
	# Color Constants
	BLACK = (0,0,0)
	WHITE = (255,255,255)
	
	
	initial_draw = True
	main_menu = True
	
	exit = False
	
	menu(screen)
	
def menu(screen):
	# Load background image
	bkg = pygame.image.load('Images/main_menu.png')

	screen.blit(bkg, (0,0))
	pygame.display.flip
	
	# Menu Stuff
	menu = cMenu(width/2+15, height - 175, 10, 75, 'vertical', 3, screen,
               [('Start Game', 1, None),
                #('Options',    2, None),
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
		
def pauseMenu(screen):
	global paused
	
	# Load background image
	bkg = pygame.image.load('Images/pause.png')
	
	screen.blit(bkg, (0,0))
	pygame.display.flip
	
	# Menu Stuff
	menu = cMenu(width/2+15, height - 175, 10, 75, 'vertical', 2, screen,
               [('Resume', 1, None),
			    ('Quit', 2, None)])
				
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
				paused = False
				break
			else:
				pygame.quit()
				sys.exit()
				
		# Update the screen
		pygame.display.update(rect_list)
		
def gameOverMenu(screen):	
	# Load background image
	bkg = pygame.image.load('Images\game_over.png')
	
	screen.blit(bkg, (0,0))
	pygame.display.flip
	
	# Menu Stuff
	menu = cMenu(width/2+15, height - 175, 10, 75, 'vertical', 2, screen,
               [('New Game?', 1, None),
			    ('Quit', 2, None)])
				
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
				game.gameOverState = True
				break
			else:
				pygame.quit()
				sys.exit()
				
		# Update the screen
		pygame.display.update(rect_list)
		
def game(screen):	
	global paused
	game = Game(width, height)		
	loop = True
	while loop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				os._exit(-1)
			if event.type == pygame.KEYDOWN:
				handle_keydown(game)
			else:
				game.car.isMovingLeft = False
				game.car.isMovingRight = False
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			pygame.key.set_repeat() 
			paused = True
		if paused:
			pygame.key.set_repeat() 
			pauseMenu(screen)
			game.initDraw = True
			pygame.key.set_repeat(10, 10)
		draw(screen, game)
		loop = update(game)
		clk.tick(FPS)
		if(not loop):
			pygame.key.set_repeat()	
			gameOverMenu(screen)
			break	
	

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
	rects.append(screen.blit(game.road.image, (game.road.x, game.road.y)))
	pygame.time.delay(2)
	for hole in game.holelist:
		rects.append(screen.blit(hole.image, (hole.x, hole.y)))
	if((game.car.isMovingRight) == True):
		rects.append(screen.blit(game.car.image_right, (game.car.x,game.car.y)))
	elif((game.car.isMovingLeft) == True):
		rects.append(screen.blit(game.car.image_left, (game.car.x,game.car.y)))
	else:
		rects.append(screen.blit(game.car.image, (game.car.x,game.car.y)))	
	rects.append(screen.blit(game.scoreSurface, (10, 10)))
	rects.append(screen.blit(game.livesSurface, (10, 35)))
	if(game.gameOverState):
		rects.append(screen.blit(game.gameOverSurface, (10, 60)))
	pygame.display.update(rects)

def update(game):
	global timeUntilNextObstacle 
	game.updateScoreCounter()
	game.hole_counter += 1
	if(game.hole_counter > timeUntilNextObstacle):
		game.holelist.append(Pothole(game.road.lbound, game.road.rbound, choose_obstacle()))
		game.hole_counter = 0
		timeUntilNextObstacle = random.randint(80,170)
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
			
def choose_obstacle():
	choice = random.randint(1,8)
	if (choice == 0):return 'Images/pothole.png'
	if (choice == 1):return 'Images/pothole1.png'
	if (choice == 2):return 'Images/pothole2.png'
	if (choice == 3):return 'Images/pothole3.png'
	if (choice == 4):return 'Images/pothole4.png'
	if (choice == 5):return 'Images/bottle1.png'
	if (choice == 6):return 'Images/bottle2.png'
	if (choice == 7):return 'Images/mouse.png'
	if (choice == 8):return 'Images/ambulance.png'
			
# Run the script
if __name__ == "__main__":
   main()