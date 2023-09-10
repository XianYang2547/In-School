# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/8/31 14:37
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : game_functions.py
# @Software: PyCharm
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from scoreboard import Scoreboard
def check_keydown_event(event,ai_settings,screen,ship,bullets):
    "响应按键"
    if event.key == pygame.K_RIGHT:  # 判断按下的键是不是右箭头
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # 左
        ship.moving_left = True
    elif event.key == pygame.K_DOWN:  # 下
        ship.moving_down = True
    elif event.key == pygame.K_UP:  # 上
        ship.moving_up = True
    elif event.key==pygame.K_SPACE:#检测空格键 开火
        # 创建一颗子弹加入到编组bullets中 主程序里的bullets=Group()
        # new_bullet=Bullet(ai_settings,screen,ship)
        # bullets.add(new_bullet)
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key==pygame.K_q:#按Q退出
        sys.exit()

def fire_bullet(ai_settings, screen, ship,bullets):
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)

def check_keyup_event(event,ship):
    "松开按键"
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False

def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets,sb):
    "监视键盘和鼠标事件"
    for event in pygame.event.get():  #
        if event.type == pygame.QUIT:  # 如果点了窗口关闭按钮，则退出游戏
            sys.exit()  #
            #下面几行与控制飞机移动有关
        elif event.type==pygame.KEYDOWN:#   每次按键都是一个keydown事件 调用上面按键函数，控制移动
            check_keydown_event(event,ai_settings,screen,ship,bullets)

        elif event.type==pygame.KEYUP:#     检测松开按键，
            check_keyup_event(event, ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:#检测鼠标按下
            mouse_x,mouse_y=pygame.mouse.get_pos()#返回鼠标单击的一个坐标
            check_play_button(ai_settings, screen,stats,play_button,ship,aliens,mouse_x,mouse_y,sb)#调用下面这个函数

def check_play_button(ai_settings, screen,stats,play_button,ship,aliens,mouse_x,mouse_y,sb):
    "单击play改变game——active的值，开始游戏"
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)#检查坐标是否在按钮的rect范围内
    if button_clicked and not stats.game_active:#将play按钮切换到非活动状态。游戏开始前能点，游戏中不能点击
        #重置游戏统计信息                           点击到play区域时，且stats.game_active为false，一开始就为false，命没了也为false
        pygame.mouse.set_visible(False)#游戏开始后 隐藏鼠标
        ai_settings.initialize_dynamic_settings()#重置速度
        stats.reset_stats()#重置命条数
        #再次点击play时，更新分数和最高纪录？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # sb.prep_high_score() #1 当超过最高记录时，命用完了，点击play 要报错，2 重新运行才会刷新最高记录

        sb.prep_score()
        sb.prep_ships()#显示命条数,刷新的感觉

        stats.game_active=True#改为true后才能开始游戏   命没了就为false
        aliens.empty()#清空屏幕上的敌机
        #创建一群敌机，飞机居中
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
def create_fleet(ai_settings, screen,ship,aliens):
    "创建敌机群"
    alien = Alien(ai_settings, screen)#先创建一个敌机
    number_alien_x=get_number_aliens_X(ai_settings,alien.rect.width)#调用下面的函数，传入的参数alien.rect.width=alien_width
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    for row_number in range(number_rows-6):
        for alien_number in range(number_alien_x-4):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def get_number_aliens_X(ai_settings,alien_width):
    "计算每行可容纳多少敌机"
    available_space_x=ai_settings.screen_width-2*alien_width#得到屏幕的宽度，并留出两个敌机的宽度
    number_alien_x=int(available_space_x/(2*alien_width))#得到可以放置敌机的个数
    return number_alien_x

def get_number_rows(ai_settings,ship_height,alien_height):
    "计算可容纳多少行敌机"
    available_space_y=ai_settings.screen_height-(3*alien_height)-ship_height#屏幕高度-第一行敌机上边距-第一行敌机高度-留的空白为敌机高度-飞机高度
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    "创建一个敌机 加入到编组中"
    alien = Alien(ai_settings, screen)#先创建一个敌机
    alien_width=alien.rect.width#获取敌机的宽度
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien_height=alien.rect.height#获取敌机的高度
    alien.y=alien_height+2*alien_height*row_number
    alien.rect.y=alien.y
    aliens.add(alien)  # 加到编组中

def update_screen(ai_settings, screen,stats,sb, ship,aliens,bullets,play_button):
    "更新屏幕代码。传3个参数：setting实例，要用到颜色  ship实例要接受screen参数"
    screen.fill(ai_settings.bg_color)  # 用这个颜色填充屏幕  bg_color=(230,230,230)  调用类中参数 颜色
    #显示发射的每一颗子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 把飞机画在屏幕上
    ship.blitme()
    #把敌机画在屏幕上
    aliens.draw(screen)
    #显示分数
    sb.show_score()
    #如果游戏处于非活动状态，就绘制play按钮
    if not stats.game_active:
        play_button.draw_button()
    # 显示绘制的屏幕
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats,sb,ship, aliens,bullets):
    # 发射子弹 ‘bullets.update()为编组bullets中的每颗子弹调用bullet.update（）’
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats,sb,ship, aliens,bullets)
    
def check_bullet_alien_collisions(ai_settings, screen,stats,sb, ship, aliens,bullets):
    #检测碰撞，第一个true改为false后，子弹不会消失，敌机则坠毁
    collisions=pygame.sprite.groupcollide(bullets,aliens,False,True)
    if collisions:
        for i in collisions.values():
            stats.score+=ai_settings.alien_points*len(i)#如果检测碰撞了，就加上分数 i是一个列表，存放了消灭的敌机数量
            sb.prep_score()#更新分数，显示在屏幕上
        check_high_score(stats,sb)
    #如果剩下一个飞机，就新建一群
    if len(aliens)==0:
        # ai_settings.increase_speed()#上一波消灭后，提高速度
        create_fleet(ai_settings, screen, ship, aliens)
def check_high_score(stats,sb):
    "检查是否产生了最高分"
    if stats.score>int(stats.high_score):
        stats.high_score=int(stats.score)
        with open('high_score.txt','w') as f:
            f.write(str(stats.high_score))
        sb.show_score()#调用显示最高分函数

def check_fleet_edges(ai_settings,aliens):
    "有敌机到达边缘时采取措施"
    for alien in aliens.sprites():
        if alien.check_edges():#如果碰到屏幕边缘了
            change_fleet_direction(ai_settings,aliens)#"就将敌机下移，并改变横向移动的方向"
            break

def change_fleet_direction(ai_settings,aliens):
    "将敌机下移，并改变横向移动的方向"
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1#改变方向


def ship_hit(ai_settings, stats, screen, sb,ship, aliens, bullets):
    "响应被敌机碰到的飞机，接下来会做什么"
    if stats.ships_left>1:#大于0则有4条命
        stats.ships_left -= 1  # stats是GameStats（）的实例，调用里面的ships_left   命减一
        sb.prep_ships()#命的图标减一
        aliens.empty()  # 清空敌机组
        create_fleet(ai_settings, screen, ship, aliens)  # 新创建一群敌机
        ship.center_ship()  # 调用ship中的center——ship，将飞机居中
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)#命没了后显示鼠标
def check_aliens_bottom(ai_settings,stats,screen,sb,ship,aliens,bullets):
    "检测是否有敌机到达了屏幕底部"
    screen_rect=screen.get_rect()#得到屏幕rect
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets)
            break

def update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets):
    "更新敌机的位置 检查敌机是否到达屏幕左右边缘"
    check_fleet_edges(ai_settings,aliens)
    aliens.update()    #对编组（敌机群）调用方法update（移动）
    "检测敌机和飞机的碰撞"
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings, stats, screen, sb,ship, aliens, bullets)
    "检测是否有敌机到达了屏幕底部"
    check_aliens_bottom(ai_settings,stats,screen,sb,ship,aliens,bullets)




