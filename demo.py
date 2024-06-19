import numpy as np
import matplotlib.pyplot as plt

# 生成模拟数据
np.random.seed(0)  # 为了保证每次生成的数据相同
x = np.linspace(0, 10, 20)  # 生成0到10之间的20个点
y = 2.5 * x + 1.0 + np.random.normal(0, 2, x.size)  # 模拟一个线性关系并加入噪声

# 绘制原始数据点
plt.scatter(x, y, label='Data Points')

# 线性拟合
coeffs_linear = np.polyfit(x, y, 1)  # 1表示线性拟合
linear_fit = np.poly1d(coeffs_linear)
plt.plot(x, linear_fit(x), label='Linear Fit', color='red')

# 二次曲线拟合
coeffs_quadratic = np.polyfit(x, y, 2)  # 2表示二次拟合
quadratic_fit = np.poly1d(coeffs_quadratic)
plt.plot(x, quadratic_fit(x), label='Quadratic Fit', color='green')

# 显示图例和图像
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Curve Fitting Example')
plt.show()
