# 使用Python进行高斯采样

## 依赖库

- Numpy
- Matplotlib

安装依赖库
  ```bash
  pip install numpy matplotlib
  ```
## 使用方法

### 1. 生成高斯分布样本
```python
samples = np.random.normal(mean, std_dev, num_samples)
```
使用 `np.random.normal` 函数生成符合指定均值和标准差的随机样本

### 2. 绘制直方图
```python
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')
```
- `plt.hist` 用于绘制样本数据的直方图
- `bins=30`：将样本数据分为30个区间
- `density=True`：将直方图的高度标准化为概率密度
- `alpha=0.6`：设置直方图的透明度
- `color='g'`：设置直方图的颜色为绿色

### 3. 绘制理论高斯分布的概率密度函数
```python
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)
plt.plot(x, p, 'k', linewidth=2)
```
- 生成高斯分布的概率密度函数并绘制在直方图上
- `np.linspace(xmin, xmax, 100)` 生成100个x值，这些值用于绘制概率密度函数
- `p` 计算每个x值对应的概率密度

### 6. 设置图表标题和标签
```python
plt.title('Gaussian Sampling')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()
```
- 设置图表的标题以及x轴和y轴的标签
- `plt.show()` 显示最终绘制的图表


## 学习资源

- [知乎：第八章：采样 | 04 高斯分布的采样](https://zhuanlan.zhihu.com/p/118494301)
- [PyTorch官方教程](https://pytorch.org/tutorials/)

---
欢迎反馈问题或建议！ 😊
