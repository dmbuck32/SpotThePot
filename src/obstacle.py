import pygame
import os
import random

class Obstacle(object):
	def __init__(self, left_bound, right_bound, name, (width, height)):
		self.name = name
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
                pygame.mixer.init()
                pygame.mixer.pre_init(44100, 16, 2, 4096)
                pygame.init()
                
                
	def moveDown(self,speed):
		if (self.name == 'Images/ambulance.png'):
			self.y += speed + 2
			self.rect.y += speed + 2

			#if pygame.mixer:
				#amb = os.path.join("music", 'ambulance_siren.wav')
					#sounds = pygame.mixer.Sound(amb)
				#pygame.mixer.Sound.play(sounds, 0)
		else:
			self.y += speed + 1
			self.rect.y += speed + 1
		
	
	
		
