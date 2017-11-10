# _*_ coding:utf-8 _*_

# 设置系统参数

class Settings(object):
	"""存储外星人所有设置的类"""

	# 初始化的设置
	def __init__(self):
		"""初始化游戏设置"""

		# 屏幕设置
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (0,0,0)

		# 设置飞船速度
		self.ship_speed_factor = 1.5

		# 设置子弹参数
		self.bullet_speed_factor = 0.1
		self.bullet_width = 3
		self.bullet_height = 16
		self.bullet_color = 60,60,60
		self.allow_bullets_number = 30000000000

		# 设置外星人间距
		self.alien_between = 30
		self.alien_speed_factor = 0.1

		# 设置向下移动的速度
		self.alien_speed_drop = 10
		# 1 向右移动 2 向左移动
		self.alien_direction = 1
