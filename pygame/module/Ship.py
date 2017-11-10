# _*_ coding:utf-8 _*_
import pygame 

class Ship(object):
	'''创建一个飞船模型'''

	def __init__(self,screen,settings):
		'''初始化飞船，并设置其初始位置'''
		self.screen = screen
		# 加载飞船图像，并获取图像信息
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# 设置移动标志
		self.moving_right = False 
		self.moving_left = False

		# 获取飞船设置参数
		self.settings = settings

		# 将飞船放到屏幕的中间
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# 在飞船的属性center中存储小数值
		self.center = float(self.rect.centerx)

	def blitem(self):
		'''在指定位置绘制飞船'''
		self.screen.blit(self.image,self.rect)



	def update(self):
		'''更新屏幕'''
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.settings.ship_speed_factor

		if self.moving_left and self.rect.left > 0:
			self.center -= self.settings.ship_speed_factor

		# 更新飞船中心坐标
		self.rect.centerx = self.center



	

		
