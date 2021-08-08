import pygame

''' 地图类'''
class GameBackground(object):
    '''初始化地图'''
    def __init__(self, scene):
        '''
        加载相同张图片资源,做交替实现地图滚动，
        注意看这张图片的特性....
        '''
        self.image1 = pygame.image.load("res/img_bg_level_3.jpg")
        self.image2 = pygame.image.load("res/img_bg_level_3.jpg")
        '''
        保存场景对象: 这里赋值等号右侧的是MainScene，大家可以具体看为什么
        '''
        self.main_scene = scene
        '''
        辅助移动地图, y1指的是第一张图片的起始位置，y2指的是第二张图片的结尾位置
        '''
        self.y1 = 0
        '''记住下面一行中的size[1]指的是电脑屏幕的y轴，是竖向的'''
        self.y2 = -self.main_scene.size[1]  
 
    '''
    计算地图图片绘制坐标
    '''
    def action(self):
        self.y1 = self.y1 + 1
        self.y2 = self.y2 + 1
        if self.y1 >= self.main_scene.size[1]:
            self.y1 = 0
        if self.y2 >= 0:
            self.y2 = -self.main_scene.size[1]
 
    '''
    大家可以注意到x轴并没有变化，因为我们在这个游戏中我们不需要背景左右飘动，
    同时绘制地图的两张图片，形成无缝衔接
    '''
    def draw(self):
        self.main_scene.scene.blit(self.image1, (0, self.y1))
        self.main_scene.scene.blit(self.image2, (0, self.y2))

# 主场景
class MainScene(object):
    # 初始化主场景
    def __init__(self):
        # 场景尺寸
        self.size = (512, 768)
        # 场景对象
        self.scene = pygame.display.set_mode([self.size[0], self.size[1]])
        # 设置标题
        pygame.display.set_caption("Air War - v1.0")
        # 创建地图对象
        self.map = GameBackground(self)

    # 绘制
    def draw_elements(self):
        self.map.draw()
 
    # 动作
    def action_elements(self):
        self.map.action()
 
    # 处理事件
    def handle_event(self):
        pass
 
    # 碰撞检测
    def detect_conllision(self):
        pass
 
    # 主循环,主要处理各种事件
    def run_scene(self):
 
        while True:
            # 计算元素坐标
            self.action_elements()
            # 绘制元素图片
            self.draw_elements()
            # 处理事件
            self.handle_event()
            # 碰撞检测
            self.detect_conllision()
            # 刷新显示
            pygame.display.update()
 
# 入口函数
if __name__ == "__main__":
    # 创建主场景
    mainScene = MainScene()
    # 开始游戏
    mainScene.run_scene()