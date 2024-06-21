from manim import *

class FancySquareAnimation(Scene):
    def construct(self):
        # 创建一个正方形
        square = Square()

        # 设置正方形的初始颜色和位置
        square.set_fill(BLUE, opacity=0.5)
        square.set_stroke(WHITE, width=2)
        square.move_to(LEFT * 3)

        # 创建一个平移动画
        move_right = square.animate.move_to(RIGHT * 3)

        # 创建一个旋转动画
        rotate = Rotate(square, angle=PI * 2)

        # 创建颜色渐变动画
        color_change = square.animate.set_fill(YELLOW, opacity=1)

        # 组合动画：移动 -> 旋转 -> 颜色变化
        self.play(move_right, run_time=2)
        self.play(rotate, run_time=2)
        self.play(color_change, run_time=2)

        # 添加渐隐效果
        self.play(FadeOut(square))

        # 保持动画最后一帧1秒
        self.wait(1)

# 渲染场景
# 在命令行中运行以下命令来渲染动画：
# manim -pql fancy_square_animation.py FancySquareAnimation
