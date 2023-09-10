#1 当超过最高记录时，命用完了，点击play 要报错，2 重新运行才会刷新最高记录  game_functions 3 消灭一波后，生成的一波移动加速有问题，太快了
import pygame#导入pygame
import game_functions as gf#导入模块并命名为gf
from settings import Settings#导入Settings这个类
from  ship import Ship# 导入飞船
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():#主程序
    pygame.init()#初始化pygame
    #使用设置类
    ai_settings=Settings()#创建setting实例
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))#用类名来调用 类里面的参数  创建一块屏幕
    pygame.display.set_caption('--------打飞机--------')#设置窗口的标题
    #创建一个用于储存游戏统计信息的实例
    stats=GameStats(ai_settings)
    #创建计分
    sb=Scoreboard(ai_settings,screen,stats)
    #创建一个飞船
    ship =Ship(ai_settings,screen)  #调用模块Ship
    #创建一个储存子弹的数组，‘导入了pygame.sprite中的group类，创建它的实例’
    bullets=Group()#子弹库
    #创建敌机裤
    aliens=Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    play_button=Button(ai_settings,screen,'QQ.play')
    #游戏循环
    while 1:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets,sb)
        if stats.game_active:
            #飞机左右移动
            ship.update()
            #发射子弹并删除消失的子弹并删除打掉的飞机
            gf.update_bullets(ai_settings, screen, stats,sb,ship, aliens,bullets)
            #移动敌机
            gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
        #每次循环时都绘屏幕
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()



