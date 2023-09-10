# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/9/1 9:27
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : alien.py
# @Software: PyCharm
import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    "表示单个敌机的类"
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        #加载图片，获取rect属性
        self.image=pygame.image.load('images/alien.png')
        self.rect=self.image.get_rect()
        #每个飞机最初放置在屏幕左上角
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #储存飞机的准确位置
        self.x=float(self.rect.x)
    def blitme(self):
        "在指定位置绘制飞机"
        self.screen.blit(self.image,self.rect)
    def check_edges(self):
        "检测作用 如果敌机位于屏幕边缘，就返回True"
        screen_rect=self.screen.get_rect()#获取屏幕属性
        if self.rect.right>=screen_rect.right:#检查敌机的rect属性和屏幕的关系
            return True
        elif self.rect.left<=0:
            return True
    def update(self):
        "移动飞机  飞机的速度*fleet_direction[它有正负值，给定正值，一开始往右边移动   "
        self.x+=(self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x=self.x

