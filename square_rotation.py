from manim import *

class SquareRotation(Scene):
    def construct(self):
        # 创建一个正方形
        square = Square()

        # 设置正方形的初始位置
        square.move_to(ORIGIN)

        # 创建一个旋转动画，持续2秒
        rotation = Rotate(square, angle=PI, run_time=2)

        # 播放旋转动画
        self.play(rotation)

        # 保持动画最后一帧1秒
        self.wait(1)

