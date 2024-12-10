# README：用Python实现EMA

## 依赖库

- Numpy
- Matplotlib

安装依赖库
  ```bash
  pip install numpy matplotlib
  ```
## 使用方法
### 1. 实现EMA计算函数
```python
    #计算平滑常数alpha
    alpha = 2 / (window_size + 1)
    ema_values = []
    
    #使用数据的第一个值作为EMA的起始值
    ema_values.append(data[0])
    
    #从第二个数据点开始计算EMA
    for t in range(1, len(data)):
        ema = alpha * data[t] + (1 - alpha) * ema_values[t-1]
        ema_values.append(ema)
    
```
`alpha`：计算平滑常数，通常公式为 `α = 2 / (window_size + 1)`，其中 `window_size` 是窗口大小。
初始EMA值使用数据集的第一个值。然后，通过迭代计算剩余数据点的EMA值

### 2. 生成示例数据
```python
data = np.random.randn(100)  # 生成100个随机数据点
```
`np.random.randn(100)` 生成100个来自标准正态分布的随机数，作为模拟数据

### 3. 计算EMA
```python
ema_values = calculate_ema(data, window_size)
```
调用 `calculate_ema` 函数计算给定数据的EMA值

### 4. 绘制图表
```python
plt.plot(data, label='Data')
plt.plot(ema_values, label=f'EMA (window={window_size})', linewidth=2)
plt.legend()
plt.title('Exponential Moving Average (EMA)')
plt.show()
```
使用 `matplotlib` 绘制原始数据 (`data`) 和计算得到的EMA值 (`ema_values`)。
设置图表的标题和图例以便区分原始数据与EMA


## 学习资源

- [知乎：Ema的原理及代码实现](https://zhuanlan.zhihu.com/p/657869421)
- [PyTorch官方教程](https://pytorch.org/tutorials/)

---
欢迎反馈问题或建议！ 😊
