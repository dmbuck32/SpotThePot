import pygame
import os

class Road(object):
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.x = 0
		self.y = 0
		self.image = pygame.transform.scale(pygame.image.load('gameface.png').convert_alpha(),(self.width,self.height))
			