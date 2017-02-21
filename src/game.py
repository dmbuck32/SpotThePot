import pygame
from car import *

class Game(object):
	def __init__(self):
		self.score = 0
		pygame.font.init()
		self.myfont = pygame.font.SysFont('Arial',30)
		self.scoreSurface = self.myfont.render("Score: " + str(self.score),True,(255,255,255))
		self.background_color = (0,0,0)
		self.car = Car()