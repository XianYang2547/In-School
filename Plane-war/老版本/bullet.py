# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/8/31 10:11
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : bullet.py
# @Software: PyCharm
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    "一个对飞机发射的子弹进行管理的类"
    def __init__(self,ai_settings,screen,ship):
        super().__init__()
        self.screen=screen

        #在（0，0）处创建一个表示子弹的矩形，再设置它的位置
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        #储存用小数表示的子弹位置
        self.y=float(self.rect.y)
        #储存子弹颜色和速度
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        "向上移动子弹"
        #更新表示子弹位置的小数值
        self.y-=self.speed_factor
        #更新表示子弹的rect位置
        self.rect.y=self.y

    def draw_bullet(self):
        "在屏幕上显示子弹"
        pygame.draw.rect(self.screen,self.color,self.rect)
