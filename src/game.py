import pygame
from car import *
from road import *
from pothole import *

class Game(object):
	def __init__(self, width, height):
		self.height = height
		self.width = width
		self.score = 0
		self.lives = 4
		pygame.font.init()
		self.myfont = pygame.font.SysFont('Arial',30)
		self.scoreSurface = self.myfont.render("Score: " + str(self.score),True,(255,255,255))
		self.livesSurface = self.myfont.render("Lives: " + str(self.lives),True,(255,255,255))
		self.gameOverSurface = self.myfont.render("Game Over",True,(255,255,255))
		self.background_color = (112,132,55)
		self.car = Car()
		self.road = Road(width, height, 100, 370)
		self.holelist = []
		self.hole_counter = 0
		self.score_counter_threshold = 200
		self.score_counter = 0
		self.initDraw = True
		self.gameOverState = False
	
	def updateScoreCounter(self):
		self.score_counter += 1
		if self.score_counter >= self.score_counter_threshold:
			self.score_counter = 0
			self.updateScore()
		
	def updateScore(self):
		self.score += 1
		self.scoreSurface = self.myfont.render("Score: " + str(self.score),True,(255,255,255))
		
	def updateLives(self):
		self.lives -= 1
		self.livesSurface = self.myfont.render("Lives: " + str(self.lives),True,(255,255,255))