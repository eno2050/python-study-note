# _*_ coding:utf-8 _*_

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

	def __init__(self,settings,screen):
		super(Alien,self).__init__()
		self.screen = screen
		self.settings = settings

		#加载外星人图像
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		#设定图像的初始位置

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#存储外星人的位置
		self.x = float(self.rect.x)

	def blitem(self):

		self.screen.blit(self.image,self.rect)


	
	def update(self):

		'''向右移动'''
		self.x += self.settings.alien_speed_factor*self.settings.alien_direction
		self.rect.x = self.x

	
	def check_edges(self):
		screen_rect = self.screen.get_rect()
		print(self.rect.right)
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
