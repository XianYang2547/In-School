import pygame

"玩家飞机类,pygame.sprite模块里面包含了一个名为Sprite类，他是pygame本身自带的一个精灵。"
class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        #添加战机图片
        # convert_alpha()更改图像的像素格式，包括每个像素的alpha,相当于图片背景变为透明
        self.image1 = pygame.image.load("images/me1.png").convert_alpha()
        self.image2 = pygame.image.load("images/me2.png").convert_alpha()
        #添加战机破坏图片
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/me_destroy_1.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_2.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_3.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_4.png").convert_alpha() \
            ])
        # get_rect()是一个处理矩形图像的方法，返回值包含矩形的居中属性,这里返回飞机图片1的位置,可以获取图片的宽高等属性
        self.rect = self.image1.get_rect()
        #把传入的屏幕参数本地化，在下面上下左右的方法里方便直接使用
        self.width, self.height = bg_size[0], bg_size[1]#屏幕属性 宽480 高700
        # 飞机的初始化位置,x轴就是游戏窗口的宽度减去这个飞机图像矩形对象的宽度再除以2，
        # y轴就是用游戏窗口的高度减去矩形对象的高度再多减去60，然后把这两个值给，玩家飞机rect矩形对象的left，和top
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.speed = 10#飞机速度
        self.active = True#飞机存活标志，一开始是存活的
        self.invincible = False#飞机一开始的无敌状态标志
        # 飞机碰撞检测，会忽略掉图片中白色的背景部分,从指定 Surface 对象中返回一个 Mask
        # 用于快速实现完美的碰撞检测，Mask 可以精确到 1 个像素级别的判断。
        # Surface 对象中透明的部分设置为 1，不透明部分设置为 0。
        self.mask = pygame.mask.from_surface(self.image1)

    "战机上下左右移动"
    def moveUp(self):
        if self.rect.top > 0:#还未到达游戏界面上边界
            self.rect.top -= self.speed
        else:                # 说明移动到达上边界了
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height - 60:# 底部需要划出60的高度用来展示其他数据（炸弹数，生命数等）
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    def autoMove(self):
        pass



    def reset(self):
        "战机重生时的位置  状态变为无敌"
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.active = True
        self.invincible = True
'''
实现重生后无敌几秒的思路：
重生后，invincible值为1，事先随便定义一个事件，重生后用一个定时器来触发这个事件（多少多少秒后触发），再捕获到这个事件的发生，把invincible
改为0.当检测碰撞时，除了精灵组外，还有invincible这个值，当它为1时，敌机和玩家的active值不会为false
        碰撞：
      enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
            if enemies_down and not me.invincible:#无敌状态不能撞敌机，无敌时me.invincible为True
                me.active = False
                for e in enemies_down:
                    e.active = False
pygame坐标
(0,0)
-------------------->x轴480
|
|
|
|
|
|           ✈  -->飞机在此
|
|
|
y轴 700
'''