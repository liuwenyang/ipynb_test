from manim import *

class GaussianBlurExample(Scene):
    def construct(self):
        # 定义一个简单的5x5图像矩阵
        image_matrix = np.array([
            [10, 10, 10, 10, 10],
            [10, 50, 50, 50, 10],
            [10, 50, 100, 50, 10],
            [10, 50, 50, 50, 10],
            [10, 10, 10, 10, 10]
        ])
        
        # 定义一个3x3的高斯核
        gaussian_kernel = np.array([
            [1, 2, 1],
            [2, 4, 2],
            [1, 2, 1]
        ])
        gaussian_kernel = gaussian_kernel / gaussian_kernel.sum()

        # 将图像矩阵和高斯核转换为Manim矩阵对象
        image_matrix_manim = Matrix(image_matrix).scale(0.5)
        kernel_matrix_manim = Matrix(gaussian_kernel).scale(0.5)

        # 创建标签
        image_label = Text("Image Matrix", font_size=24).next_to(image_matrix_manim, UP)
        kernel_label = Text("Gaussian Kernel", font_size=24).next_to(kernel_matrix_manim, UP)

        # 显示图像矩阵和高斯核
        self.play(Write(image_label), Create(image_matrix_manim))
        self.play(Write(kernel_label), Create(kernel_matrix_manim))
        self.wait(2)

        # 定义卷积过程
        conv_matrix = self.convolve(image_matrix, gaussian_kernel)

        # 显示卷积结果
        conv_matrix_manim = Matrix(conv_matrix).scale(0.5)
        conv_label = Text("Convolution Result", font_size=24).next_to(conv_matrix_manim, UP)
        self.play(Write(conv_label), Create(conv_matrix_manim))
        self.wait(2)

    def convolve(self, image, kernel):
        """对图像矩阵进行卷积"""
        output = np.zeros_like(image)
        pad = kernel.shape[0] // 2

        # 对图像进行零填充
        padded_image = np.pad(image, pad, mode='constant')

        # 进行卷积操作
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                region = padded_image[i:i+kernel.shape[0], j:j+kernel.shape[1]]
                output[i, j] = np.sum(region * kernel)

        return output
