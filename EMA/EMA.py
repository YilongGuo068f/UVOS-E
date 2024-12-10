import numpy as np
import matplotlib.pyplot as plt

def calculate_ema(data, window_size):
    #计算平滑常数alpha
    alpha = 2 / (window_size + 1)
    ema_values = []
    
    #使用数据的第一个值作为EMA的起始值
    ema_values.append(data[0])
    
    #从第二个数据点开始计算EMA
    for t in range(1, len(data)):
        ema = alpha * data[t] + (1 - alpha) * ema_values[t-1]
        ema_values.append(ema)
    
    return np.array(ema_values)

#数据
data = np.random.randn(100) #生成100个随机数据点

#设置窗口大小
window_size = 10

#计算EMA
ema_values = calculate_ema(data, window_size)

#绘制数据和EMA
plt.plot(data, label='Data')
plt.plot(ema_values, label=f'EMA (window={window_size})', linewidth=2)
plt.legend()
plt.title('Exponential Moving Average (EMA)')
plt.show()
