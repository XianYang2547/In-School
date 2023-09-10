# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/8/30 15:20
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : p216.py
# @Software: PyCharm
"p216动手试一试"
import sys

import pygame
class Ship():
    "创建飞船"
    def __init__(self,screen):
        "初始化飞船图像并设置其初始位置"
        self.screen=screen
        #加载飞船图像 并获取矩形数据
        self.image=pygame.image.load('../images/ship.bmp')
        self.rect=self.image.get_rect()#获取图片矩形
        self.screen_rect=screen.get_rect()#获取屏幕矩形

        #将每个新飞船放在屏幕底部中央
         #飞船矩形属性  ==  屏幕矩形属性
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
    def blitme(self):
        "在指定位置绘制飞船"
        self.screen.blit(self.image,self.rect)

while 1:
    pygame.init()
    screen=pygame.display.set_mode((1200,800))
    screen.fill((0,0,0))

    ship=Ship(screen)
    ship.blitme()

    pygame.display.flip()
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            print(event.type)
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            print(event.type)