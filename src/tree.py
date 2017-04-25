import pygame
import os
import random

class Tree(object):
	def __init__(self, left_bound, right_bound, name):
		self.name = name
		self.width = 50
		self.height = 50
		if(int(random.random() * 10) % 2 == 0):
			self.x = random.randrange(0, left_bound-self.width)
		else:
			self.x = random.randrange(right_bound, right_bound + 50)
		self.y = -50
		self.rect = pygame.Rect(self.x + 20,self.y + 20, 10, 10)
		self.image = pygame.transform.scale(pygame.image.load(name).convert_alpha(),(self.width,self.height))
		self.isMovingLeft = False
		self.isMovingRight = False
		self.isCollidable = False
	
	def moveDown(self, speed):
		self.y += speed + 1
		self.rect.y += speed + 1
