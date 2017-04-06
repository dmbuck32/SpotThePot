import pygame
import os
import random

class Obstacle(object):
	def __init__(self, left_bound, right_bound, name, (width, height)):
		self.width = width
		self.height = height
		self.x = random.randrange(left_bound + 20, right_bound - self.width - 17)
		self.y = -50
		self.rect = pygame.Rect(self.x + 20,self.y + 20,self.width - 40,self.height - 40)
		self.image = pygame.transform.scale(pygame.image.load(name).convert_alpha(),(self.width,self.height))
		self.isMovingLeft = False
		self.isMovingRight = False
		self.isCollidable = True
		self.name = name
	
	def moveDown(self):
		if (self.name == 'Images/ambulance.png'):
			self.y += 2
			self.rect.y += 2
		else:
			self.y += 1
			self.rect.y += 1
		
	
	
		