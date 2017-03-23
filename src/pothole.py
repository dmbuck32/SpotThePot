import pygame
import os
import random

class Pothole(object):
	def __init__(self, left_bound, right_bound):
		self.width = 50
		self.height = 50
		self.x = random.randrange(left_bound + 20, right_bound - self.width - 17)
		self.y = -50
		self.rect = pygame.Rect(self.x + 20,self.y + 20,self.width - 40,self.height - 40)
		self.image = pygame.transform.scale(pygame.image.load('Images\pothole.png').convert_alpha(),(self.width,self.height))
		self.isMovingLeft = False
		self.isMovingRight = False
		self.isCollidable = True
	
	def moveDown(self):
		self.y += 1
		self.rect.y += 1
		
	
	
		