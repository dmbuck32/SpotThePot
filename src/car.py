import pygame
import os

class Car(object):
	def __init__(self):
		self.x = 280
		self.y = 450
		self.width = 100
		self.height = 100
		self.rect = pygame.Rect(self.x + 15,self.y + 15,self.width - 30,self.height - 30)
		self.image = pygame.transform.scale(pygame.image.load('car.png').convert_alpha(),(self.width,self.height))
		self.isMovingLeft = False
		self.isMovingRight = False
	
	def moveLeft(self):
		self.x -= 2
		self.rect.x -= 2
		
	def moveRight(self):
		self.x += 2
		self.rect.x += 2
		
	def collided(self, otherlist):
		for other in otherlist:
			if other.isCollidable and self.rect.colliderect(other.rect):
				other.isCollidable = False
				return True
		return False