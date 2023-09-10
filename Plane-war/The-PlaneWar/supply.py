import pygame
from random import *


class Bullet_Supply(pygame.sprite.Sprite):
    "子弹火力供应"
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("images/bullet_supply.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = \
            randint(0, self.width - self.rect.width), -100#y轴上设置-100，游戏中先播放补给到来的音效，过一会补给包就掉下来了，给玩家一个准备接收的时间
        self.speed = 5
        self.active = False
        #self.active = False 默认情况下我们就不开启他，只有每30秒我们就触发他一次，
        # 当active为True的时候，就让他降落move
        self.mask = pygame.mask.from_surface(self.image)
    
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False
    
    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = \
            randint(0, self.width - self.rect.width), -100


class Bomb_Supply(pygame.sprite.Sprite):
    "超级炸弹供应"
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("images/bomb_supply.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = \
            randint(0, self.width - self.rect.width), -100
        self.speed = 5
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)
    
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False
    
    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = \
            randint(0, self.width - self.rect.width), -100


class Life_Supply(pygame.sprite.Sprite):
    "生命供应"
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/life_supply.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = \
            randint(0, self.width - self.rect.width), -100
        self.speed = 5
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = \
            randint(0, self.width - self.rect.width), -100

