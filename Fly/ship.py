import pygame
import settings

class Ship():

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        '''
        首先将表示屏幕的矩形存储在 self.screen_rect 中（见❸），再将 self.rect.centerx （飞船中心的 x 坐标）设置为表示屏幕
的矩形的属性 centerx （见❹），并将 self.rect.bottom （飞船下边缘的 y 坐标）设置为表示屏幕的矩形的属性 bottom 。 Pygame 将使用这些 rect 属性来放置飞船图像，
使其与屏幕下边缘对齐并水平居中。
        '''
        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        self.centery= float(self.rect.centery)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

        self.moving_forward = False
        self.moving_back = False

    def update(self):
        """ 根据移动标志调整飞船的位置 """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_forward and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_back and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        # 根据self.centerx更新rect对象
        self.rect.centerx = self.center
        self.rect.centery = self.centery

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)