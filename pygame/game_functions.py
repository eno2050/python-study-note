#_*_ coding:utf-8 _*_

import pygame
import sys
from module.Bullet import Bullet
from module.Alien import Alien
def check_keydown_event(event,settings,screen,ship,bullets):
	# 实现向右移动
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True

	# 实现向左移动
	elif event.key == pygame.K_LEFT:

		ship.moving_left = True

	# 创建子弹
	elif event.key == pygame.K_SPACE:
		fire_bullet(settings,screen,ship,bullets)	
	elif event.key == pygame.K_q:
		sys.exit()
		
def fire_bullet(settings,screen,ship,bullets):
	if len(bullets) <= settings.allow_bullets_number-1:
		new_bullet = Bullet(settings,screen,ship)
		# bullets 这是一个子弹编组,将子弹的对象实例添加到编组当中
		bullets.add(new_bullet)

def update_bullet(bullets):
	# 绘制子弹
	bullets.update()
	# 删除超出屏幕的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)


def get_alien_allow_x(settings,alien_width):
	# 计算屏幕长度方向允许几个外星人
	alien_x = settings.screen_width - 2*settings.alien_between
	alien_x_number = int(alien_x / (alien_width+settings.alien_between))
	return alien_x_number

def create_alien(settings,screen,index,alien_width,alien_height,aliens,row):

	alien = Alien(settings,screen)
	alien.rect.x = index*alien_width+(index+1)*settings.alien_between 
	alien.rect.y = alien_height*row+(row+1)*settings.alien_between
	aliens.add(alien)		
	

def get_alien_allow_y(settings,alien_height):
	# 计算高度方向允许几个外星人
	alien_y = settings.screen_height - 2*settings.alien_between - alien_height
	alien_y_number = int(alien_y /(alien_height+settings.alien_between))
	return alien_y_number



def create_aliens(settings,screen,aliens):
	'''创建飞船'''
	alien = Alien(settings,screen)
	# 获取外星人的宽度
	alien_width = alien.rect.width
	# 获取外星人的高度
	alien_height = alien.rect.height

	for item in range(get_alien_allow_y(settings,alien_height)):
		for index in range(get_alien_allow_x(settings,alien_width)):
			create_alien(settings,screen,index,alien_width,alien_height,aliens,item)
		
	

def check_keyup_event(event,ship):

	if event.key == pygame.K_RIGHT:

		ship.moving_right = False

	elif event.key == pygame.K_LEFT:

		ship.moving_left = False


	
	
	

def check_events(settings,screen,ship,bullets):
	'''响应按键和鼠标事件'''
	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			sys.exit()

		elif event.type == pygame.KEYDOWN:

			check_keydown_event(event,settings,screen,ship,bullets)

		elif event.type == pygame.KEYUP:

			check_keyup_event(event,ship)



		
def update_screen(settings,screen,ship,bullets,aliens):
	'''更新屏幕上的图像，并切换到新屏幕'''

	# 首先绘制屏幕
	screen.fill(settings.bg_color)
	ship.blitem()
	# 绘制子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	# 添加外星人
	aliens.draw(screen)
	# 显示
	pygame.display.flip()

def update_aliens(settings,aliens):
	'''更新外星人的位置'''
	check_alien_edges(settings,aliens)
	aliens.update()
	

def check_alien_edges(settings,aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_alien_direction(settings,aliens)
			break

def change_alien_direction(settings,aliens):
	for alien in aliens.sprites():
		alien.rect.y += settings.alien_speed_drop

	settings.alien_direction *= -1

