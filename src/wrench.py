import pygame
import os
import random

class Wrench(object):
	def __init__(self, left_bound, right_bound):
		self.width = 33
		self.height = 33
		self.x = random.randrange(left_bound + 20, right_bound - self.width - 17)
		self.y = -50
		self.rect = pygame.Rect(self.x + 20,self.y + 20, 10, 10)
		self.image = pygame.transform.scale(pygame.image.load("Images\wrench.png").convert_alpha(),(self.width,self.height))
		self.isMovingLeft = False
		self.isMovingRight = False
		self.isCollidable = True
	
	def moveDown(self, speed):
		self.y += speed + 1
		self.rect.y += speed + 1
