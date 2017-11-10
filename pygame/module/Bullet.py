# _*_ coding:utf-8 _*_

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	'''子弹管理'''
	def __init__(self,settings,screen,ship):
		
		super(Bullet,self).__init__()
		self.screen = screen

		# 在(0,0)处创建一个表示子弹的矩形，在设置正确的位置
		self.rect = pygame.Rect(0,0,settings.bullet_width,settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# 存储小数表示子弹的位置
		self.y = float(self.rect.y)

		self.color = settings.bullet_color
		self.speed_factor = settings.bullet_speed_factor

	def update(self):
		'''子弹向上移动'''
		self.y -= self.speed_factor
		# 更新子弹的rect的位置
		self.rect.y = self.y

	def draw_bullet(self):
		'''把子弹绘制在屏幕上'''
		pygame.draw.rect(self.screen,self.color,self.rect)

		

