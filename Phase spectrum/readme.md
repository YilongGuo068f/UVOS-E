
# README: 使用 Python 生成图像的相位谱

这个项目展示了如何使用 Python 和 OpenCV 库来进行图像的傅里叶变换，并计算其 **相位谱**。通过应用伪彩色映射，我们可以将相位谱可视化，以帮助理解图像频域中的相位信息。

## 目的

本代码旨在帮助大家了解傅里叶变换和相位谱的概念，并展示如何将其以彩色图的形式进行可视化

## 环境要求

- Python 3.x
- OpenCV
- NumPy
- Matplotlib

可以使用以下命令安装所需的库：

```bash
pip install opencv-python numpy matplotlib
```

## 代码说明

### 1. 读取图像

首先，代码会读取输入的图像文件，并将其转换为灰度图像，因为傅里叶变换通常应用于灰度图像进行频域分析。

```python
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
```

### 2. 傅里叶变换

通过 `np.fft.fft2()` 执行二维傅里叶变换，计算图像的频域表示。之后，使用 `np.fft.fftshift()` 将低频成分移到图像的中心。

```python
f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)
```

### 3. 计算相位谱

相位谱是通过 `np.angle()` 函数计算傅里叶变换结果中的相位信息。它提供了图像中频率成分的相位角度。

```python
phase_spectrum = np.angle(fshift)
```

### 4. 归一化相位谱

由于相位谱的值通常在 `[-π, π]` 范围内，为了便于可视化，我们将其归一化到 `[0, 1]` 的范围。这样，我们可以将其应用于伪彩色映射。

```python
phase_spectrum_normalized = (phase_spectrum + np.pi) / (2 * np.pi)
```

### 5. 可视化

最后，我们使用 `matplotlib` 的 `imshow()` 函数来显示原图和归一化后的相位谱。为了使相位谱的表现更为直观，使用了 `HSV` 伪彩色映射。

```python
plt.imshow(phase_spectrum_normalized, cmap='hsv')
```

## 结果

代码将生成两张图：
1. **原始图像**：显示输入的图像。
2. **彩色相位谱**：显示图像频率成分的相位信息。相位谱被映射到 `HSV` 色图，展示不同相位值对应的颜色。


## 适用场景

- **傅里叶变换和频域分析**：帮助理解图像中的频率成分。
- **图像处理**：应用于图像压缩、去噪等领域，了解相位对图像重建的影响。
- **计算机视觉**：有助于在频域中分析图像的结构和模式。

## 学习资源

- [论文：Pseudo-Labeling and Self-training](https://arxiv.org/abs/1905.13736)
- [PyTorch官方教程](https://pytorch.org/tutorials/)

--- 

欢迎反馈问题或建议！ 😊
