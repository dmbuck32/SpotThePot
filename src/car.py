import pygame
import os

class Car(object):
	def __init__(self):
		self.x = 280
		self.y = 280
		self.width = 30
		self.height = 30
		self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
		self.image = pygame.image.load('car.png').convert_alpha()
	
	def moveLeft(self):
		if(self.x > 0): 
			self.x = self.x - 2;
			self.rect.x -= 2
			
	def moveRight(self):
		if(self.x < 840): 
			self.x = self.x + 2;
			self.rect.x += 2