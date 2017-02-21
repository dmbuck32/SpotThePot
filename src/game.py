import pygame
from car import *
from road import *

class Game(object):
	def __init__(self, width, height):
		self.height = height
		self.width = width
		self.score = 0
		pygame.font.init()
		self.myfont = pygame.font.SysFont('Arial',30)
		self.scoreSurface = self.myfont.render("Score: " + str(self.score),True,(255,255,255))
		self.background_color = (112,132,55)
		self.car = Car()
		self.road = Road(height)