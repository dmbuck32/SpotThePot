import pygame
import os
import random

class Pothole(object):
	def __init__(self, left_bound, right_bound):
		self.width = 50
		self.height = 50
		self.x = random.randrange(left_bound, right_bound - self.width)
		self.y = -50
		self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
		self.image = pygame.transform.scale(pygame.image.load('pothole.png').convert_alpha(),(self.width,self.height))
		self.isMovingLeft = False
		self.isMovingRight = False
	
	def moveDown(self):
		self.y += .5
		self.rect.y += .5
		
	def collided(self, other):
		if self.rect.colliderect(other.rect):
			return true
		return false
		