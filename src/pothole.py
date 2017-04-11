import pygame
import os
import random

class Pothole(object):
	def __init__(self, left_bound, right_bound, name):
	
		self.image = pygame.image.load(name).convert_alpha()
		self.width = (self.image).get_width()/5
		self.height = (self.image).get_height()/5
		self.image = pygame.transform.scale(self.image,(self.width,self.height))
		self.x = random.randrange(left_bound + 20, right_bound - self.width - 17)
		self.y = -80
		self.rect = pygame.Rect(self.x + 20,self.y + 20,self.width - 40,self.height - 40)		
		self.isMovingLeft = False
		self.isMovingRight = False
		self.isCollidable = True
		self.name = name
	
	def moveDown(self,speed):
		if (self.name == 'Images/ambulance.png'):
			self.y += speed + 2
			self.rect.y += speed + 2
		else:
			self.y += speed + 1
			self.rect.y += speed + 1
		
	
	
#		self.image = pygame.transform.scale(pygame.image.load(name).convert_alpha(),(self.width,self.height))
