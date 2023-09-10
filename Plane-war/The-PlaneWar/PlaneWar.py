# main.py
import pygame
import sys
import traceback
import myplane
import enemy
import bullet
import supply

from pygame.locals import *
'''rom pygame.locals import * 这个就是把pygame当地的常量都导入，比如pygame.QUIT，等一些事件，就不用加pygame这个前缀，直接写事件的名字的就可以了。'''
from random import *
#pygame初始化，导入声音初始化
pygame.init()
pygame.mixer.init()

#设置窗口、背景
bg_size = width, height = 480, 700#实际上它是个元组
screen = pygame.display.set_mode(bg_size)#设置屏幕窗口
pygame.display.set_caption("他们都爱打飞机 ")#窗口名字
background = pygame.image.load("images/background.png").convert()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 载入游戏音乐
pygame.mixer.music.load("sound/game_music.ogg")
pygame.mixer.music.set_volume(0.2)###设置音量
#载入音效
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")#从文件或缓冲区对象中创建新的声音（Sound）对象
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)


def add_small_enemies(group1, group2, num):
    "调用此函数时，传入一个小型飞机组，敌机汇总组以及要创建的小飞机数量"
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)#创建一个小飞机的实例
        group1.add(e1)
        group2.add(e1)


def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)


def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)


def inc_speed(target, inc):
    #定义一个增加速度的函数，传入一个列表和一个速度值
    for each in target:
        each.speed += inc


def main():
    #播放主背景音乐，-1表示循环播放
    pygame.mixer.music.play(-1)

    "pygame.sprite.Group()函数可以创建一个精灵组，从而统一管理"
    # 生成我方飞机
    me = myplane.MyPlane(bg_size)
    #创造一个enemies敌机的汇总,就是把所有的敌机都放到这个组里边去
    enemies = pygame.sprite.Group()
    
    # 生成敌方小型飞机
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 15)
    
    # 生成敌方中型飞机
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 4)
    
    # 生成敌方大型飞机
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 2)
    
    # 生成普通子弹
    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 4
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1(me.rect.midtop))
    
    # 生成超级子弹
    bullet2 = []
    bullet2_index = 0
    BULLET2_NUM = 12
    for i in range(BULLET2_NUM // 3):#for i in range(4):  相当于下面的每个位置存4颗子弹 i=0 1 2 3 共在bullet2中存12颗
        bullet2.append(bullet.Bullet2((me.rect.centerx - 33, me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx + 30, me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.midtop)))
    # 创建时钟对象（可以控制游戏循环频率）
    clock = pygame.time.Clock()
    
    # 中弹图片索引
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0
    
    # 统计得分
    score = 0
    score_font = pygame.font.Font("font/font.ttf", 36) # 得分的字体
    
    # 标志是否暂停游戏
    paused = False  #默认为非暂停状态
    ### 设置 导入暂停和继续的图片  当鼠标在图片区域时，显示出按压效果（颜色加深）
    pause_nor_image = pygame.image.load("images/pause_nor.png").convert_alpha()
    pause_pressed_image = pygame.image.load("images/pause_pressed.png").convert_alpha()

    resume_nor_image = pygame.image.load("images/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("images/resume_pressed.png").convert_alpha()
    ### 放置暂停图片的位置，屏幕右上角
    paused_rect = pause_nor_image.get_rect()
    paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10
    paused_image = pause_nor_image
    
    # 设置难度级别
    level = 1
    
    # 全屏炸弹
    bomb_image = pygame.image.load("images/bomb.png").convert_alpha()
    bomb_rect = bomb_image.get_rect()
    bomb_font = pygame.font.Font("font/font.ttf", 48)#返回一个字体对象  炸弹数量的字体
    bomb_num = 7
    
    # 补给包设置
    bullet_supply = supply.Bullet_Supply(bg_size)#实例化补给包
    bomb_supply = supply.Bomb_Supply(bg_size)#实例化补给包
    life_supply=supply.Life_Supply(bg_size)
    SUPPLY_TIME = USEREVENT#我们的自定义事件
    pygame.time.set_timer(SUPPLY_TIME, 10 * 1000)#定时器，每10秒触发SUPPLY_TIME这个事件，在后面当我们检测到这个事件时，就发放补给
    ''' pygame.time.set_timer(SUPPLY_TIME, 10 * 1000)功能：在事件队列上重复创建事件
        属性：
        set_timer(eventid, milliseconds) -> None
        set_timer(eventid, milliseconds, once) -> None
        将事件类型设置为每隔给定的毫秒出现在事件队列中。第一个事件在经过一定时间后才会出现。
        每个事件类型都可以附加一个单独的计时器。最好使用 pygame.USEREVENT 和 pygame.NUMEVENTS的值。
        若要禁用事件的计时器，请将毫秒参数设置为0。
        如果once参数为True，则只发送计时器一次。'''

    
    # 超级子弹定时器
    DOUBLE_BULLET_TIME = USEREVENT + 1
    
    # 标志是否使用超级子弹
    is_double_bullet = False
    
    # 解除我方无敌状态定时器
    INVINCIBLE_TIME = USEREVENT + 10
    
    # 生命数量
    life_image = pygame.image.load("images/life.png").convert_alpha()
    life_rect = life_image.get_rect()
    life_num = 3
    
    # 用于阻止重复打开记录文件
    recorded = False
    
    # 游戏结束画面
    gameover_font = pygame.font.Font("font/font.TTF", 48)
    again_image = pygame.image.load("images/again.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("images/gameover.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()
    
    # 用于控制玩家飞机 图片切换  展示突突的效果
    switch_image = True
    
    # 切换延迟  整个一个while循环就是一帧
    delay = 100
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN: #响应 MOUSEBUTTONDOWN 的事件可以知道用户是否点下鼠标
                if event.button == 1 and paused_rect.collidepoint(event.pos):#如果按下了，且在图片矩形内按下（检测鼠标的pos）
                    paused = not paused#paused=false---->paused=True了
                    if paused:
                        pygame.time.set_timer(SUPPLY_TIME, 0)#设置为0，就是取消这个自定义事件，暂停的时候停止发放补给
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pygame.time.set_timer(SUPPLY_TIME, 10 * 1000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()
            
            elif event.type == MOUSEMOTION:# MOUSEMOTION当玩家的鼠标在这个界面上有任何的移动的时候，检测他是否在这个范围之内
                if paused_rect.collidepoint(event.pos):#如果在暂停图片矩形范围内的话  深色图片
                    if paused:#如果是暂停的情况下
                        paused_image = resume_pressed_image
                    else:
                        paused_image = pause_pressed_image
                else:                               #如果鼠标箭头没有在矩形范围内的话  浅色图片
                    if paused:
                        paused_image = resume_nor_image
                    else:
                        paused_image = pause_nor_image
            
            elif event.type == KEYDOWN:#检测是不是按下 事件
                "事件为按下键盘空格"
                if event.key == K_SPACE:
                    if bomb_num:
                        bomb_num -= 1
                        bomb_sound.play()
                        for each in enemies:
                            if each.rect.bottom > 0:#遍历矩形属性大于0的，（在屏幕里的，存活状态全部为false）
                                each.active = False

            elif event.type == SUPPLY_TIME:#检测上面的自定义事件--补给
                supply_sound.play()
                supply_list=[1,2,3]
                if choice(supply_list)==1:#随机选择括号里一个，
                    bomb_supply.reset()#调用reset（）方法，，active变为True，即将准备发送补给
                elif  choice(supply_list)==2:
                    bullet_supply.reset()
                else:
                    life_supply.reset()
            
            elif event.type == DOUBLE_BULLET_TIME:
                is_double_bullet = False
                pygame.time.set_timer(DOUBLE_BULLET_TIME, 0)#设置为0，就是取消这个定时器  自定义事件
            
            elif event.type == INVINCIBLE_TIME:
                me.invincible = False
                pygame.time.set_timer(INVINCIBLE_TIME, 0)#设置为0，就是取消这个自定义事件
        
        # 根据用户的得分增加难度
        if level == 1 and score > 50000:
            level = 2
            upgrade_sound.play()
            # 增加3架小型敌机、2架中型敌机和1架大型敌机
            add_small_enemies(small_enemies, enemies, 3)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 1)
            # 提升小型敌机的速度
            inc_speed(small_enemies, 1)
        elif level == 2 and score > 300000:
            level = 3
            upgrade_sound.play()
            # 增加5架小型敌机、3架中型敌机和2架大型敌机
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            # 提升小型敌机的速度
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        elif level == 3 and score > 600000:
            level = 4
            upgrade_sound.play()
            # 增加5架小型敌机、3架中型敌机和2架大型敌机
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            # 提升小型敌机的速度
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        elif level == 4 and score > 1000000:
            level = 5
            upgrade_sound.play()
            # 增加5架小型敌机、3架中型敌机和2架大型敌机
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            # 提升小型敌机的速度
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        
        screen.blit(background, (0, 0))

        #如果还有命，也没有按暂停，进行正常游戏环节
        if life_num and not paused:
            # 检测用户的键盘操作
            key_pressed = pygame.key.get_pressed()#pygame.key.get_pressed()  —  获取键盘上所有按键的状态 返回一个序列
            
            if key_pressed[K_w] or key_pressed[K_UP]:#key_pressed[K_w] key_pressed变量就是一个序列，
                        # 而这里K_w 事实上就是一个索引值，他事实上都是定义的，他背后都有一个数字，那这里就是他的一个索引值，就是表示当W这个键被按下
                me.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()
            if key_pressed[K_F10]:
                me.autoMove()

            # 发放全屏炸弹补给并检测是否获得
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)#绘出下落的补给包
                if pygame.sprite.collide_mask(bomb_supply, me):#完美的碰撞检测，捡到了就返回True
                    get_bomb_sound.play()
                    if bomb_num < 15:
                        bomb_num += 1
                    bomb_supply.active = False
                    # 接着玩家捡到之后就不用再绘制他让他出现在屏幕上了，就bomb_supply.active = False ，设置他的active属性为False

            # 发放超级子弹补给并检测是否获得
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply, me):
                    get_bullet_sound.play()
                    is_double_bullet = True
                    pygame.time.set_timer(DOUBLE_BULLET_TIME, 100 * 1000)
                    ##定时器，每100秒触发DOUBLE_BULLET_TIME这个事件，在后面当我们检测到这个事件时，就发放补给
                    bullet_supply.active = False
            '''当子弹包掉下来后，玩家捡到了，双倍子弹使用属性变为True，is_double_bullet = True，‘当它为True后，下面的语句就发射了’。
            然后设置一个定时器，每100秒触发DOUBLE_BULLET_TIME这个事件，用语句去检测这个触发，检测到了后，is_double_bullet = False，就不满足
            发射双倍子弹了'''
            # 发放生命补给并检测是否获得
            if life_supply.active:
                life_supply.move()
                screen.blit(life_supply.image, life_supply.rect)  # 绘出下落的补给包
                if pygame.sprite.collide_mask(life_supply, me):  # 完美的碰撞检测，捡到了就返回True
                    get_bomb_sound.play()
                    life_num+=1
                    life_supply.active = False
            # 准备子弹的射出 以及 检测子弹是否击中敌机'''
            if not (delay % 10):#那么就是if not(delay % 10): 每十帧，就调用一次，这里意思就是说只又delay 的值是能够被10整除的，那么才会执行这里边的内容
                bullet_sound.play()
                if is_double_bullet:#捡到了超级子弹，is_double_bullet为True
                    bullets = bullet2#使用超级子弹库，把bullet2里边的子弹对象都放到，bullets 里边去，
                    bullets[bullet2_index].reset((me.rect.centerx - 33, me.rect.centery))#左
                    bullets[bullet2_index + 1].reset((me.rect.centerx + 30, me.rect.centery))#索引bullet2_index+1 表示他的第二颗子弹应该在中间炮筒发射出去
                    bullets[bullet2_index + 2].reset((me.rect.midtop))                      #右
                    bullet2_index = (bullet2_index + 3) % BULLET2_NUM  #bullets中的第0 1 2 颗子弹分别送左中右射出，索引一次加3 【0 3 6 9 9+3=12 12%12=0，又从0开始索引】
                                                                        #0+3 第3颗又从左边射出。总共为0-11个，% 12 能始终保证值在0-11循环，不会累加超出子弹列表边界
                else:# 将生成的子弹（是存在列表里的） 为false，调用子弹的reset方法后，弄为存活状态 为true，并 放置到飞机相应位置
                    bullets = bullet1   #同样发射普通子弹时也是bullet1里边的对象都放到bullets里边，然后下面都是对bullets 进行处理就可以了。
                    bullet1_index = (bullet1_index + 1) % BULLET1_NUM
                    bullets[bullet1_index].reset(me.rect.midtop)

            '''做碰撞检测,pygame.sprite.spritecollide(sprite,sprite_group,bool):一个组中的所有精灵都会逐个地对另外一个单个精灵进行冲突检测，发生冲突的精灵会作为一个列表返回。
            第一个参数就是单个精灵，第二个参数是精灵组，第三个参数是一个bool值，最后这个参数起了很大的作用。当为True的时候，会删除组中所有冲突的精灵，False的时候不会删除冲突的精灵
             第四个参数是：两个精灵之间的像素遮罩检测"'''
            #遍历子弹是否射中
            for b in bullets:
                if b.active:#调用子弹的reset方法，active为true，就移动子弹，将子弹射出去
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            if e in mid_enemies or e in big_enemies:
                                e.hit = True #中型飞机或者大型飞机被打到了，改变值为True
                                e.energy -= 1
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False
                                '''那么就是在敌机被击中时，就来for e in mid_enemies or big_enemies: 来判断是否是中大型敌机，是的话就e.energy -= 1 减1生命值，
                                然后if e.energy == 0 来判断他们的生命值是否等于0，是的话e.active = False 就把他们的active属性设置为False，
                                另一种情况就是小型敌机了，直接设置他的active属性为False就可以了.关于上面的mid_enemies 和 big_enemies 这两个列表，
                                因为前面在创建敌机的时候，他都会把新创建的敌机加入到两个group中，一个是加入到他自己的group，就是这个mid_enemies ，
                                另一个就是加入一个存着所有敌机的enemies列表'''
            
            # 绘制大型敌机 先画大型敌机， 先画大型敌机，后边画的小型敌机就会飞行在大型敌机上面
            for each in big_enemies:
                if each.active:
                    each.move()
                    if each.hit:#如果被子弹打到了，绘制一下特效图片
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        if switch_image:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)
                    
                    # 绘制血槽
                    ''' 先画一条黑色的线，再在上面画一条绿色的线
                    调用pygame的draw模块的line，画直线的方法，第一个参数就是指定画在screen 对象上，第二个参数就指定画的颜色，
                    第三个参数就是画的直线的开始位置，那么就是这个飞机矩形对象左上角往上大概5个像素的距离，第四个参数就是画的直线的结束位置，
                    就是飞机矩形对象右上角往上大概5个像素的点 ，连起来就是一条直线啦，然后第五个参数再来设置一下直线的宽度为2'''
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), \
                                     2)
                    # 当生命大于20%显示绿色，否则显示红色
                    energy_remain = each.energy / enemy.BigEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                        #在黑色的线上覆盖绘制 👿
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, \
                                      each.rect.top - 5), 2)
                    '''首先第三个参数是一样的，起点都是一样，然后血条的右边的终点我们就要算算比例了，
                     那就是起点开始each.rect.left ，然后再加上还有多少血，each.rect.width *energy_remain，
                      因为each.rect.width 飞机矩形的宽度刚好就是整个血条的长度，拿来乘上边计算得到还剩的比例，
                      就可以得到绿色或者红色还要话多长了， 然后这只是x坐标的，还有y坐标的each.rect.top - 5，不变，
                      还剩飞机矩形往上5个像素，宽度也还是2个像素'''


                    # 即将出现在画面中，播放音效
                    '''这里-50就是，也就是说-50，-49，-48他都要播放一次，那还得了，那么就是他从上到下走了多少像素，
                    就播放了多少次，然后一次还要几秒钟，那这样子相当于卡住了八个通道，全部卡住了，全部播放这个声音了，
                    所以这样是不对的，如下修改，就是当他移动到-50的位置，就给个参数-1，
                    就是表示循环播放这个音效，然后就是当他挂掉的时候就不播放了，'''
                    if each.rect.bottom == -50:
                        enemy3_fly_sound.play(-1)
                else:
                    # 毁灭
                    if not (delay % 3):
                        '''那么screen.blit(each.destroy_images[e3_destroy_index], each.rect) 就是每一个飞机对象调用他的当前索引值索引得到的毁灭图片，
                        接下来就应该将这个e3_destroy_index是索引值向下一个。
                        那么就是 e3_destroy_index = (e3_destroy_index + 1) % 6 ，因为大型敌机毁灭图片一共有6张图片，
                        所以这里%6,那么这个表达式得到的值就永远是0-5之间，当e3_destroy_index=5，在加1等于6,6再%6就等于0.刚好切换会第一张毁灭的图片。
                        接着if e3_destroy_index == 0: 来判断索引值是不是等于0，是的话就each.reset() ，这里是这样的，比如该开始进来的时候 e3_destroy_index的值是0，
                        ，那么就把第一张毁灭的图片画出来，画出来之后呢，索引值就加1,1%6这个值就变成1了，不等于0，接着继续播放第二张，以此类推，播放第三张，第四张，第五张，
                        第六张，到第六张的时候，也就是索引值变成了5，在+1变成6,6%6等于0，就满足这个条件，说明他一轮过去了，就去执行reset方法复活，重新回到界面的上方
                                第一帧刚进来的时候，e3_destroy_index是0，然后就播放一次音效，
                        然后第一张毁灭图片画出来，e3_destroy_index +1 再次进来 不符合，那他就不播放了，
                        直接到下面画第二张毁灭图，到最后他再次等于0 的时候，他就reset()'''
                        if e3_destroy_index == 0:
                            enemy3_down_sound.play()
                        screen.blit(each.destroy_images[e3_destroy_index], each.rect)
                        e3_destroy_index = (e3_destroy_index + 1) % 6
                        if e3_destroy_index == 0:
                            enemy3_fly_sound.stop()#boss挂了就不播放声音了
                            score += 10000
                            each.reset()
            
            # 绘制中型敌机：
            for each in mid_enemies:
                if each.active:
                    each.move()
                    
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)
                    
                    # 绘制血槽
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), \
                                     2)
                    # 当生命大于20%显示绿色，否则显示红色
                    energy_remain = each.energy / enemy.MidEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, \
                                      each.rect.top - 5), 2)
                else:
                    # 毁灭
                    if not (delay % 3):
                        if e2_destroy_index == 0:
                            enemy2_down_sound.play()
                        screen.blit(each.destroy_images[e2_destroy_index], each.rect)
                        e2_destroy_index = (e2_destroy_index + 1) % 4
                        if e2_destroy_index == 0:
                            score += 6000
                            each.reset()
            
            # 绘制小型敌机：
            for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    # 毁灭
                    if not (delay % 3):
                        if e1_destroy_index == 0:
                            enemy1_down_sound.play()
                        screen.blit(each.destroy_images[e1_destroy_index], each.rect)
                        e1_destroy_index = (e1_destroy_index + 1) % 4
                        if e1_destroy_index == 0:
                            score += 1000
                            each.reset()
            
            # 检测我方飞机是否被撞
            enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
            if enemies_down and not me.invincible:#无敌状态不能撞敌机，无敌时me.invincible为True
                me.active = False
                for e in enemies_down:
                    e.active = False
            

            # 切换图片
            '''加一个switch_image = True布尔类型的变量，接着在绘制玩家飞机的时候，那么我们就通过判断和变换这个变量，
            不断切换地绘制两张图片，if switch_image: 如果是True的话就绘制me1，如果是False就画m2，然后就是switch_image = not switch_image 
            每次循环取反一次，那么这样就实现了这两种图片不断的切换'''
            if not (delay % 5):#只有是5的倍数时才切换  余数只能为1 2 3 4，加上0，相当于每5帧切换一次
                switch_image = not switch_image
            delay -= 1
            if not delay:  # 当delay不为真时， if delay==0
                delay = 100
                # 通过时钟对象指定循环频率，每秒循环60次，这里设置为最大60帧
                # 帧速率是指程序每秒在屏幕山绘制图
            clock.tick(60)
            # 绘制我方飞机
            if me.active:
                if switch_image:
                    screen.blit(me.image1, me.rect)
                else:
                    screen.blit(me.image2, me.rect)
            else:
                # 毁灭
                if not (delay % 3):
                    #播放死亡音效和绘制死亡消逝图片
                    if me_destroy_index == 0:
                        me_down_sound.play()
                    screen.blit(me.destroy_images[me_destroy_index], me.rect)
                    me_destroy_index = (me_destroy_index + 1) % 4
                    if me_destroy_index == 0:#4%4取余为0，相当于死亡图片一圈显示完了，飞机完完全全死了
                        life_num -= 1
                        me.reset()
                        #飞机重生后，invincible = True，有10秒无敌时间，10秒后，用定时器触发INVINCIBLE_TIME事件，
                        # 当后面检测到这个事件后，invincible = True取消无敌
                        pygame.time.set_timer(INVINCIBLE_TIME, 10 * 1000)
            
            # 绘制全屏炸弹图标，数量
            bomb_text = bomb_font.render("× %d" % bomb_num, True, WHITE)#用render渲染成一个surface对象，才能画到屏幕上，显示样式就是   X 炸弹数量
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_image, (10, height - 10 - bomb_rect.height))#炸弹图标
            screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - text_rect.height))#炸弹数量

            # 绘制剩余生命数量
            if life_num:
                for i in range(life_num):
                    screen.blit(life_image, \
                                (width - 10 - (i + 1) * life_rect.width, \
                                 height - 10 - life_rect.height))
            
            # 绘制得分
            score_text = score_font.render("Score : %s" % str(score), True, WHITE)
            screen.blit(score_text, (10, 5))
        
        # 绘制游戏结束画面
        elif life_num == 0:
            # 背景音乐停止
            pygame.mixer.music.stop()
            
            # 停止全部音效
            pygame.mixer.stop()
            
            # 停止发放补给
            pygame.time.set_timer(SUPPLY_TIME, 0)
            
            if not recorded:
                "那么就是recorded 刚开始的默认值是Fasle，那么就是if not recorded: " \
                "玩家只要一运行，此条件满足，进入到里面，进到后就把recorded = True，设置为True，" \
                "那以后的循环他都不会进来了，就只执行一次，接着读取里面的最高分"
                recorded = True
                # 读取历史最高得分
                with open("record.txt", "r") as f:
                    record_score = int(f.read())
                
                # 如果玩家得分高于历史最高得分，则存档
                if score > record_score:
                    with open("record.txt", "w") as f:
                        f.write(str(score))
            
            # 绘制结束画面
            record_score_text = score_font.render("Best : %d" % record_score, True, (255, 255, 255))
            screen.blit(record_score_text, (50, 50))

            #绘制 Your Score这几个字
            gameover_text1 = gameover_font.render("Your Score", True, (255, 255, 255))
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = \
                (width - gameover_text1_rect.width) // 2, height // 3
            screen.blit(gameover_text1, gameover_text1_rect)

            #绘制你的分数
            gameover_text2 = gameover_font.render(str(score), True, (255, 255, 255))
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = \
                (width - gameover_text2_rect.width) // 2, \
                gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, gameover_text2_rect)

            #绘制 重新开始按钮
            again_rect.left, again_rect.top = \
                (width - again_rect.width) // 2, \
                gameover_text2_rect.bottom + 50
            screen.blit(again_image, again_rect)

            #绘制 结束游戏按钮
            gameover_rect.left, gameover_rect.top = \
                (width - again_rect.width) // 2, \
                again_rect.bottom + 10
            screen.blit(gameover_image, gameover_rect)


            # 检测用户的鼠标操作
            # 如果用户按下鼠标左键
            if pygame.mouse.get_pressed()[0]:
                # 获取鼠标坐标
                pos = pygame.mouse.get_pos()
                # 如果用户点击“重新开始”
                if again_rect.left < pos[0] < again_rect.right and \
                        again_rect.top < pos[1] < again_rect.bottom:
                    # 调用main函数，重新开始游戏
                    main()
                # 如果用户点击“结束游戏”
                elif gameover_rect.left < pos[0] < gameover_rect.right and \
                        gameover_rect.top < pos[1] < gameover_rect.bottom:
                    # 退出游戏
                    pygame.quit()
                    sys.exit()
                    
        # 绘制暂停按钮
        screen.blit(paused_image, paused_rect)
        

        # 更新整个待显示的  Surface 对象到屏幕上，将内存中的内容显示到屏幕上
        pygame.display.flip()



if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
'''except SystemExit: 如果是正常的退出，他就抛出**SystemExit:**的异常，直接不管他pass就可以了，
如果说是其他异常的话，就报告一下，traceback.print_exc() 这主要就是让我们在双击这个python源代码文件执行的时候，
不会说如果出错了，就一闪而过，我们要让他停留，打印出相关的错误，input() 就是起到一个停留的作用，接受用户的输入，然后才可以走
'''