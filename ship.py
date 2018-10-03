import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		#初始化飞船，并设置其起飞位置
		super(Ship,self).__init__()

		self.screen = screen
		self.ai_settings = ai_settings

		#加载飞船图像
		self.image = pygame.image.load('ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#飞船放在底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#飞船center中存储小数值
		self.center = float(self.rect.centerx)
		self.center2 = float(self.rect.centery)

		#移动标志
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		#更新飞船center值
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > 0:
			self.center2 -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom< self.screen_rect.bottom:
			self.center2 += self.ai_settings.ship_speed_factor

		#更新rect对象
		self.rect.centerx = self.center
		self.rect.centery = self.center2

	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		#让飞船在屏幕上居中
		self.center = self.screen_rect.centerx