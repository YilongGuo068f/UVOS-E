import numpy as np
import matplotlib.pyplot as plt

#设置参数
mean = 0 #均值
std_dev = 1 #标准差
num_samples = 1000 #生成样本的数量

#进行高斯采样
samples = np.random.normal(mean, std_dev, num_samples)

#绘制直方图
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')

#绘制高斯分布的概率密度函数
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)
plt.plot(x, p, 'k', linewidth=2)

plt.title('Gaussian Sampling')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()
