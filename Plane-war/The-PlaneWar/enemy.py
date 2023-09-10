import pygame
from random import *
#导入啊，初始化啊，加载图片啊，获取Surface对象，矩形对象，bg_size本地化啊
"敌机类"
class SmallEnemy(pygame.sprite.Sprite):
    "小型敌机类"
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        #加载敌机图片
        self.image = pygame.image.load("images/enemy1.png").convert_alpha()
        #添加战机破坏图片
        self.destroy_images = []
        self.destroy_images.extend([ \
            pygame.image.load("images/enemy1_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy1_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy1_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy1_down4.png").convert_alpha() \
            ])
        #获取敌机图片rect属性，方便下面放置其位置
        self.rect = self.image.get_rect()# get_rect()是一个处理矩形图像的方法，返回值包含矩形的各属性,这里返回敌机图片的位置,可以获取图片的宽高等属性
        self.width, self.height = bg_size[0], bg_size[1]
        #敌机速度
        self.speed = 2
        self.active = True
        #敌机位置随机从屏幕顶部出现 # 随机生成飞机的位置,randint(a,b)即生成a<=n<=b,即在屏幕宽度，以及负5倍的高度下随机生成
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)#0到屏幕宽度-敌机宽度这个范围，一个负数到0的范围
        # 飞机碰撞检测，会忽略掉图片中白色的背景部分
        self.mask = pygame.mask.from_surface(self.image)

    ## 飞机还未飞出屏幕外，就向下运动
    #  飞机飞出屏幕外后，别浪费，重置其位置（或者摧毁也行，反正得处理，不然内存会炸）
    def move(self):
        if self.rect.top < self.height:#飞机的顶部值小于屏幕底部 就一直往下移动
            self.rect.top += self.speed
        else:                           #如果移动到屏幕最下面了，就重新放置
            self.reset()
    '''x方向就是在0，到self.width - self.rect.width 屏幕宽度减去敌机矩形宽度的范围随机生成，
    y轴就是让小型敌机在-5个屏幕到0之间随机生成就会好了，也就是游戏窗口上方看不见的位置初始化,小中大型 -5个 -10个 -15个屏幕间隔'''
    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)

class MidEnemy(pygame.sprite.Sprite):
    "中型敌机类"
    energy = 8
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("images/enemy2.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy2_hit.png").convert_alpha()#子弹打到敌机上  特效
        self.destroy_images = []
        self.destroy_images.extend([ \
            pygame.image.load("images/enemy2_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy2_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy2_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy2_down4.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-10 * self.height, -self.height)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = MidEnemy.energy#  self.energy =8
        self.hit = False#默认没有被子弹打到
    
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()
    
    def reset(self):
        self.active = True
        self.energy = MidEnemy.energy
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-10 * self.height, -self.height)

class BigEnemy(pygame.sprite.Sprite):
    "大型敌机类"
    energy = 20
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image1 = pygame.image.load("images/enemy3_n1.png").convert_alpha()
        self.image2 = pygame.image.load("images/enemy3_n2.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy3_hit.png").convert_alpha()#子弹打到敌机上  特效
        self.destroy_images = []
        self.destroy_images.extend([ \
            pygame.image.load("images/enemy3_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down4.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down5.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down6.png").convert_alpha() \
            ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-15 * self.height, -5 * self.height)
        self.mask = pygame.mask.from_surface(self.image1)
        self.energy = BigEnemy.energy
        self.hit = False
    
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()
    
    def reset(self):
        self.active = True
        self.energy = BigEnemy.energy
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-15 * self.height, -5 * self.height)
