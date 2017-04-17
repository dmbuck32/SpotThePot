import pygame
from car import *
from road import *
from obstacle import *

class Game(object):
	def __init__(self, width, height):
		self.height = height
		self.width = width
		self.score = 1
		self.lives = 4
		self.level = 1
		self.minTime = 200
		self.maxTime = 300
		pygame.font.init()
		self.myfont = pygame.font.SysFont('Arial',30)
		self.scoreSurface = self.myfont.render("Score: " + str(self.score),True,(255,255,255))
		self.livesSurface = self.myfont.render("Lives: " + str(self.lives),True,(255,255,255))
		self.livesImage = pygame.transform.scale(pygame.image.load('Images/4lives.png').convert_alpha(),(65,120))
		self.gameOverSurface = self.myfont.render("Game Over",True,(255,255,255))
		self.levelSurface = self.myfont.render("Level: "+ str(self.level), True, (255,255,255))
		self.levelUpMessageSurface = self.myfont.render("", True, (255,215, 0))
		self.bonusLifeSurface = self.myfont.render("", True, (255, 215, 0))
		self.background_color = (112,132,55)
		self.car = Car()
		self.road = Road(width, height, 100, 370)
		self.holelist = []
		self.hole_counter = 0
		self.wrench_counter = 0
		self.wrench_on_screen = []
		self.score_counter_threshold = 200
		self.score_counter = 0
		self.initDraw = True
		self.gameOverState = False
		self.scoreLevelUpdater = 15
	
	def updateScoreCounter(self):
		self.score_counter += 1
		if self.score_counter >= self.score_counter_threshold:
			self.score_counter = 0
			self.updateScore()
		
	def updateScore(self):
		self.score += 1
		self.scoreSurface = self.myfont.render("Score: " + str(self.score),True,(255,255,255))
		self.updateLevel()
		
	def updateLives(self, upOrDown):
		if (not(upOrDown>0 and self.lives >= 4)):
			self.lives += upOrDown
		print self.lives
		livesImageWidth = 65
		livesImageHeight = 120
		if self.lives >= 4:
			self.livesImage = pygame.transform.scale(pygame.image.load('Images/4lives.png').convert_alpha(),(livesImageWidth,livesImageHeight))
		elif self.lives == 3:
			self.livesImage = pygame.transform.scale(pygame.image.load('Images/3lives.png').convert_alpha(),(livesImageWidth,livesImageHeight))
		elif self.lives == 2:
			self.livesImage = pygame.transform.scale(pygame.image.load('Images/2lives.png').convert_alpha(),(livesImageWidth,livesImageHeight))
		elif self.lives == 1:
			self.livesImage = pygame.transform.scale(pygame.image.load('Images/1life.png').convert_alpha(),(livesImageWidth,livesImageHeight))
		elif self.lives ==0:
			self.livesImage = pygame.transform.scale(pygame.image.load('Images/0lives.png').convert_alpha(),(livesImageWidth,livesImageHeight))
			
		self.livesSurface = self.myfont.render("Lives: " + str(self.lives),True,(255,255,255))
	
	def updateLevel(self):
		if ((self.score > 0) and (self.score % self.scoreLevelUpdater == 0)):
			self.level += 1
			self.levelUpMessageSurface = self.myfont.render("NEXT LEVEL!", True, (255,215, 0))
			if self.level > 1 and self.level % 5 == 0 and self.lives < 4:
				self.lives += 1 # Bonus life every 5 levels, if they can take it
				self.livesSurface = self.myfont.render("Lives: " + str(self.lives),True,(255,255,255))
				self.bonusLifeSurface = pygame.font.SysFont('Aria', 25).render("Bonus Life!", True, (255,215,0))
			else: 
				self.bonusLifeSurface = self.myfont.render("", True, (255,215,0))
			if self.minTime == 200:
				self.minTime -= 100
				self.maxTime -= 100
			elif self.minTime == 100:
				self.minTime -= 50
				self.maxTime -= 50
			elif self.minTime <= 50:
				self.minTime -= 10
				self.maxTime -= 15
			self.levelSurface = self.myfont.render("Level: "+ str(self.level), False, (255,255,255))
			#print "minTime: %d\nmaxTime: %d" %(self.minTime, self.maxTime)
		else:
			self.levelUpMessageSurface = self.myfont.render("", True, (255,215, 0))
			self.bonusLifeSurface = self.myfont.render("", True, (255,215,0))
		
