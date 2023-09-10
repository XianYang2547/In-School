import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    "创建飞船"
    def __init__(self,ai_settings,screen):
        "初始化飞船图像并设置其初始位置"
        super().__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        #加载飞船图像 并获取矩形数据
        self.image=pygame.image.load('images/ship1.png').convert_alpha()
        self.rect=self.image.get_rect()#获取图片矩形
        self.screen_rect=screen.get_rect()#获取屏幕矩形

        #将每个新飞船放在屏幕底部中央
         #飞船矩形属性  ==  屏幕矩形属性
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        "在飞机的属性center中存储小数值"
        self.centerx=float(self.rect.centerx)#self.rect.centerx转为浮点数，方便加上 self.ship_speed_factor=1.5
        self.centery=float(self.rect.centery)
        "移动标志 上下左右"
        self.moving_right=False
        self.moving_left = False
        self.moving_up=False
        self.moving_down=False

    def blitme(self):
        "在指定位置绘制飞船"
        self.screen.blit(self.image,self.rect)
    def update(self):
        "控制飞机左右移动    根据移动标志来调整位置，按住不放为True，一直移动"
        "更新飞机的center值，而不是rect，因为rect的centerx只能储存整数值"
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.centerx+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>self.screen_rect.left:#不用elif，因为同时按住左右键，会优先往右移动
            self.centerx-=self.ai_settings.ship_speed_factor
        "控制飞机上下移动    根据移动标志来调整位置，按住不放为True，一直移动"
        if self.moving_up and self.rect.top>self.screen_rect.top:
            self.centery-=self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:#不用elif，因为同时按住左右键，会优先往右移动
            self.centery+=self.ai_settings.ship_speed_factor

        "用中间值self.center来更新rect对象"
        self.rect.centerx=self.centerx
        self.rect.centery=self.centery
    def center_ship(self):
        "飞机命减一后，将它居中"
        self.centerx=self.screen_rect.centerx
        self.centery=self.screen_rect.bottom-18

