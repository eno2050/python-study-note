# _*_ coding:utf-8 _*_

import pygame
from setting.Settings import Settings
from module.Ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
	pygame.init()
	# 引入设置类
	settings = Settings()
	# 首先创建一个用于显示的屏幕，这个很重要，后面一直在他上面显示
	screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
	# 设置标题
	pygame.display.set_caption('大战外星人')
	# 设置背景颜色
	bg_color = settings.bg_color
	# 创建飞船
	ship = Ship(screen,settings) 
	# 创建子弹编组
	bullets = Group()
	# 创建一个外星人编组
	aliens = Group()
	# 创建外星人
	gf.create_aliens(settings,screen,aliens)
	#开始游戏的主循环
	while True:
		# 监视鼠标和键盘事件
		gf.check_events(settings,screen,ship,bullets)
		# 根据上面返回的结果，处理飞船
		ship.update()
		# 绘制子弹
		gf.update_bullet(bullets)
		# 外星人移动
		gf.update_aliens(settings,aliens)
		#绘制屏幕
		gf.update_screen(settings,screen,ship,bullets,aliens)
		
	

run_game()

