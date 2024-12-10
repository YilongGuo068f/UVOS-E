
# README: 使用 Python 生成图像的相位谱

## 依赖库

- OpenCV
- NumPy
- Matplotlib

安装依赖库：

```bash
pip install opencv-python numpy matplotlib
```

## 使用方法

### 1. 读取图像

首先，代码会读取输入的图像文件，并将其转换为灰度图像

```python
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
```

### 2. 傅里叶变换

通过 `np.fft.fft2()` 执行二维傅里叶变换，计算图像的频域表示。之后，使用 `np.fft.fftshift()` 将低频成分移到图像的中心

```python
f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)
```

### 3. 计算相位谱

相位谱是通过 `np.angle()` 函数计算傅里叶变换结果中的相位信息

```python
phase_spectrum = np.angle(fshift)
```

### 4. 归一化相位谱

由于相位谱的值通常在 `[-π, π]` 范围内，为了便于可视化，我们将其归一化到 `[0, 1]` 的范围

```python
phase_spectrum_normalized = (phase_spectrum + np.pi) / (2 * np.pi)
```

### 5. 可视化

最后，我们使用 `matplotlib` 的 `imshow()` 函数来显示原图和归一化后的相位谱。 `HSV` 是伪彩色映射

```python
plt.imshow(phase_spectrum_normalized, cmap='hsv')
```

## 输出

代码将生成两张图：
1. **原始图像**：显示输入的图像
2. **彩色相位谱**：显示图像频率成分的相位信息。因为用了 `HSV` 色图，将展示不同相位值对应的颜色。



## 学习资源

- [论文：Pseudo-Labeling and Self-training](https://arxiv.org/abs/1905.13736)
- [PyTorch官方教程](https://pytorch.org/tutorials/)

--- 

欢迎反馈问题或建议！ 😊
