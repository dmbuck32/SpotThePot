import pygame
import os

class Road(object):
	def __init__(self):
		self.x = 280
		self.y = 0
		self.y2 = 100 #I figure we have two y values since we'll be recycling two roads like a conveyer belt system, seems like it'd be more succint than making two road objects
		self.width = 100
		self.height = 100
		self.image = pygame.transform.scale(pygame.image.load('gameface.png').convert_alpha(),(self.width,self.height))
	
	def moveDown(self):
		self.y += 2;
		self.y2 += 2
			