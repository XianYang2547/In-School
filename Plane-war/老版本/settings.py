import pygame
from pygame.sprite import Sprite
class Settings(Sprite):
    # 储存游戏 所有设置的 类
    def __init__(self):
        super().__init__()
        # 初始化游戏的设置
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #设置飞机的移动速度..生命条数
        # self.ship_speed_factor=1.8
        self.ship_limit=3
        #子弹设置
        # self.bullet_speed_factor=3
        self.bullet_width=5
        self.bullet_height=15
        self.bullet_color=255,0,0
        #敌机移动
        # self.alien_speed_factor=1#移动的速度
        self.fleet_drop_speed=10#撞边缘后向下移的速度
        # self.fleet_direction= 1 #########值为1表示右移  -1表示左移
        #以什么样的速度加快游戏节奏  系数，在下面的    def increase_speed(self):中调用
        self.speed_scale=1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):#方便重新开始游戏时调用，重置速度
        "设置了初始飞机速度，子弹速度，敌机速度"
        self.ship_speed_factor=1.8
        self.bullet_speed_factor=3
        self.alien_speed_factor=0.5#移动的速度
        self.fleet_direction= 1 #########值为1表示右移  -1表示左移
        self.alien_points=500

    def increase_speed(self):
        "提高速度设置"
        self.ship_speed_factor+=self.speed_scale
        self.bullet_speed_factor+=self.speed_scale
        self.alien_speed_factor+=self.speed_scale

