# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/9/3 9:11
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : scoreboard.py
# @Software: PyCharm
import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard():
    "显示得分信息的类"
    def __init__(self,ai_settings,screen,stats):
        "初始化显示得分涉及的属性"
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats
        #显示得分信息时使用的字体信息
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        #准备初始得分图像，最高分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_ships()
    def prep_score(self):
        "将得分转换为一幅渲染的图像"
        # score_str=str(self.stats.score)#将分数转为字符串  下面函数要传入的数值
        score_str = '{:,}'.format(round(self.stats.score))#用逗号作为千分位分隔符5,100,000
        self.score_image=self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        #将得分放在屏幕右上角
        self.score_rect=self.score_image.get_rect()#得到score_image的rect属性
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20

    def prep_high_score(self):
        "将最高得分转换为一幅渲染的图像"
        # score_str=str(self.stats.score)#将分数转为字符串  下面函数要传入的数值
        high_score_str= self.stats.high_score#用逗号作为千分位分隔符5,100,000
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)
        #将最高得分放在屏幕顶部中间
        self.high_score_rect=self.high_score_image.get_rect()#得到score_image的rect属性
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=20

    def prep_ships(self):
        "显示还剩下多少条命，飞机图标的形式"
        self.ships=Group()#创建一个编组
        for ship_number in range(self.stats.ships_left):#遍历每条命，生成一个飞机，设置其位置
            ship=Ship(self.ai_settings, self.screen)#参数由init传入的
            ship.rect.x=self.screen_rect.right-ship_number*ship.rect.width-48
            ship.rect.y=self.screen_rect.bottom-35
            self.ships.add(ship)
    def show_score(self):
        "在屏幕上显示得分"
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.ships.draw(self.screen)#把def prep_ships(self):中的飞机画在屏幕上
