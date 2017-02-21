import pygame
import os

class Road(object):
	def __init__(self,bottom_bound):
		self.width = 600
		self.height = 342
		self.x = 280
		self.y = -self.height
		self.y2 = 0 #I figure we have two y values since we'll be recycling two roads like a conveyer belt system, seems like it'd be more succint than making two road objects
		self.y3 = self.height
		self.image = pygame.transform.scale(pygame.image.load('gameface.png').convert_alpha(),(self.width,self.height))
		self.bottom_bound = bottom_bound
	
	def moveDown(self):
		self.y += .5
		self.y2 += .5
		self.y3 += .5
		if(self.y > self.bottom_bound):
			self.y = -330
		if(self.y2 > self.bottom_bound):
			self.y2 = -330
		if(self.y3 > self.bottom_bound):
			self.y3 = -330
			