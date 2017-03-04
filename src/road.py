import pygame
import os

class Road(object):
	def __init__(self,width,height,lbound,rbound):
		self.width = width
		self.height = height
		self.x = 0
		self.y = 0
		self.lbound = lbound
		self.rbound = rbound
		self.image = pygame.transform.scale(pygame.image.load('gameface.png').convert_alpha(),(self.width,self.height))
			