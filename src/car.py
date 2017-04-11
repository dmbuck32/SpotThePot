import pygame
import os

class Car(object):
	def __init__(self):
		self.x = 190
		self.y = 650
		self.width = 100
		self.height = 100
		self.rect = pygame.Rect(self.x + 15,self.y + 15,self.width - 30,self.height - 45)
		self.image = pygame.transform.scale(pygame.image.load('Images/car.png').convert_alpha(),(self.width-12,self.height-12))
		self.image_left = pygame.transform.scale(pygame.image.load('Images/car_left.png').convert_alpha(),(self.width,self.height))
		self.image_right = pygame.transform.scale(pygame.image.load('Images/car_right.png').convert_alpha(),(self.width,self.height))
		self.isMovingLeft = False
		self.isMovingRight = False
	
	def moveLeft(self,speed):
		self.isMovingRight = False
		self.isMovingLeft = True
		self.x -= speed + 3
		self.rect.x -= speed + 3
		
	def moveRight(self,speed):
		self.isMovingLeft = False
		self.isMovingRight = True
		self.x += speed + 3
		self.rect.x += speed + 3
		
	def collided(self, otherlist):
		for other in otherlist:
			if other.isCollidable and self.rect.colliderect(other.rect):
				other.isCollidable = False
				return True
		return False