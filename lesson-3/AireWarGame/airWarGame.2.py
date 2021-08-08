import pygame

''' 游戏场景设计'''

'''
    <首先我们强调一个事情，编程要走的更高更远，最最重要的是数学！--- 数学之美>

            笛卡尔坐标系 ==> 直角坐标系

    我们引入一个概念 
                >> 类 <<

    这个类用来做什么呢，设计游戏的主场景

    那么什么是类呢？

    举个最简单的例子： 人 = > 人类

    class Human(object):
        def __init__(self):
            self.gender = male
            self.age = 18
            self.weight = 55kg
            self.height = 170cm
            self.health = healthy
            self.status = sleeping
            self.nationality = China
        # 上面这些的就是用来定义人的<<属性>>的
        def set_gender():
            ...
        def set_age():
            ...
        def set_weight():
            ...
        def set_height():
            self.height(172)
        def set_health_status():
            ...
        def move_left(steps):
            ...
        def eat():
            ...
        def walk():
            ...
        def run():
            ...
        def sleep():
            ...
        # 上面这些的就是用来定义人的<<行为>>的

    那我拿到了这个类 应该怎么用呢
    首先定义一个对象
        Human jerry;
        jerry.set_height(172);
        ...
        # 往左走10步
        jerry.move_left(10);

    =========>> 主场景 <<===========

    我们创建GameScene类，用于显示窗口，并负责游戏的核心逻辑及场景中
    各个游戏元素的管理

'''
class MainScene(object):
    '''
        =========>> 初始化主场景 <<===========
    '''
    def __init__(self):
        # 设置场景尺寸
        self.mSize = (512, 768)
        # 场景对象                                   x 轴    |    y 轴
        self.mScene = pygame.display.set_mode([self.mSize[0], self.mSize[1]])
        # 设置标题
        pygame.display.set_caption("Air War - v1.0")

    '''
        绘制

        计算出了游戏中的元素，飞机或者子弹的坐标，那么就需要将飞
        机和子弹的图片绘制到这个坐标的位置;
    '''
    def draw_elements(self):
        pass
 
    '''
        动作

        计算游戏中元素的坐标。也就是游戏每刷新一次，游戏中的元素，
        例如子弹坐标就会+1, 比如飞机的坐标计算等等；
    '''
    def action_elements(self):
        pass
 
    '''
        处理事件

        游戏进行过程中，玩家会通过键盘或者鼠标点击、拖动、
        甚至关闭窗口等都属于事件，当玩家有这些操作的时候，我们要对
        玩家的操作做出响应。比如，如果玩家点击了窗口右上角的X按钮，
        我们就要停止游戏并且关闭窗口结束程序，如果玩家按下w键，我们
        就让飞机向上移动等等。
    '''
    def handle_event(self):
        pass
 
    '''
        碰撞检测

        这个游戏核心逻辑，我们发出子弹，就要判断子弹是否
        和敌人飞机碰到一起，如果碰到一起我们就要消失子弹，并且消失
        飞机，在碰撞坐标处播放动画。如果敌人子弹击中我们，也是类似
        思路。碰撞检测我们主要通过判断两张图片的矩形是否相交。
    '''
    def detect_conllision(self):
        pass

    '''
        刷新窗口。

        这个最为简单，直接调用pygame.display.update()即可。
    '''
    def display_update(self):
        pygame.display.update()
        pass

    # 主循环,主要处理各种事件
    def run_scene(self):
 
        while True:
            # 计算并确定下一步所有元素坐标
            self.action_elements()
            # 绘制所有元素图片
            self.draw_elements()
            # 处理事件
            self.handle_event()
            # 碰撞检测
            self.detect_conllision()
            # 刷新显示
            self.display_update()

# 入口函数
if __name__ == "__main__":
    # 创建主场景
    mainScene = MainScene()
    # 开始游戏
    mainScene.run_scene()