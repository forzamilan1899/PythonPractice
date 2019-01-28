#import sys
import pygame
from  settings import Settings
from  ship import Ship
import  game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个外星人
    #alien = Alien(ai_settings, screen)

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建外星人群
    aliens = Group()
    gf.create_fleet(ai_settings, screen,ship, aliens)

    # 设置背景色：
    #bg_color = (255, 150, 0)

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        '''
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        #bullets.update()
        gf.update_bullets(bullets)
        '''
        #每次循环都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()
        '''
        #for bullet in bullets.copy():
        #    if bullet.rect.bottom <=0:
         #       bullets.remove(bullet)
        #print(len(bullets ))
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
