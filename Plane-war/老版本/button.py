# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/9/2 15:00
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : button.py
# @Software: PyCharm
import pygame.font
class Button():
    def __init__(self,ai_settings,screen,msg):
        "初始化按钮的属性"
        self.screen=screen
        self.screen_rect=screen.get_rect()
        #设置按钮的尺寸和其他属性
        self.width,self.height=200,50
        self.button_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)
        #创建按钮的rect对象，居中
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        #按钮的标签只创建一次
        self.prep_msg(msg)
    def prep_msg(self,msg):
        "将文本渲染成图像，并在按钮中居中显示"
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)#创建图像的render（）
        self.msg_image_rect=self.msg_image.get_rect()#得到这个文本的rect
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        "绘制一个用颜色填充的按钮，再绘制文本"
        self.screen.fill(self.button_color,self.rect)#绘制表示按钮的矩形
        self.screen.blit(self.msg_image,self.msg_image_rect)#

