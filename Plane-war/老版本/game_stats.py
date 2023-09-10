# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/9/2 8:56
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : game_stats.py
# @Software: PyCharm
class GameStats():
    "跟踪游戏的统计信息"

    def __init__(self,ai_settings):
        self.ai_settings=ai_settings
        #调用下面初始化方法
        self.reset_stats()
        self.game_active=False
        self.high_score=self.a11()
        # self.high_score=0#最高得分

    def a11(self):
        with open('high_score.txt','r') as f:
            high_s=f.read()
        return high_s
    def reset_stats(self):
        "初始化在游戏运行期间可能变化的统计信息"
        self.ships_left=self.ai_settings.ship_limit#初始3条命
        self.score=0#初始得分


