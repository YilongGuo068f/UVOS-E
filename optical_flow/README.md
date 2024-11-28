# README: 使用 Python 生成光流图

---

## 目的

本项目旨在帮助大家了解并学会如何使用Python和OpenCV生成光流图。

1. **光流的基本概念**：理解光流图如何表示物体运动的方向和速度
2. **从视频中提取帧**：通过指定帧序号从视频中提取帧数据
3. **生成光流图**：使用OpenCV的 `cv2.calcOpticalFlowFarneback` 方法计算光流并生成伪彩色光流图
4. **图像可视化**：使用Matplotlib展示光流图和原始帧

---

## 光流图简介

光流是图像序列中像素的运动信息，广泛用于视频分析、目标跟踪和运动检测等领域。通过光流图，我们可以直观地观察到视频帧之间的运动变化：

- **颜色**表示运动的方向
- **亮度**表示运动的幅度（速度）

---

## 功能

该项目实现以下主要功能：

1. 从视频中提取指定的一帧
2. 计算该帧与下一帧之间的光流
3. 使用伪彩色显示光流图，其中：
   - 色调（H）表示运动方向
   - 亮度（V）表示运动幅度

---

## 配置

### 1. 安装依赖

运行代码前，请确保安装以下 Python 库：

```bash
pip install opencv-python matplotlib
```

### 2. 准备视频文件

将目标视频文件保存到指定路径。支持常见格式如 `.mp4`, `.avi`

### 3. 修改代码路径

打开 `optical_flow.py` 文件，修改以下代码中的 `video_path` 为自己的视频文件路径：

```python
video_path = "XXX.mp4"  #需要替换的视频路径
frame_index = 0  #需要替换成要分析的帧号
```

### 4. 运行代码

运行代码：

```bash
python optical_flow.py
```

---

## 输出说明

运行代码后，将看到两张图像：

1. **原始帧**：选定帧的图像，用于直观对比
2. **光流图**：对应帧的伪彩色光流图，包含运动方向和速度的信息

---

## 主要流程

### 1. 加载视频和指定帧

通过 `cv2.VideoCapture` 打开视频并提取指定帧及其下一帧

```python
cap = cv2.VideoCapture(video_path)
ret, frame1 = cap.read()
```

### 2. 计算光流

使用 OpenCV 的 `cv2.calcOpticalFlowFarneback` 方法，计算两帧之间的光流信息：

```python
flow = cv2.calcOpticalFlowFarneback(prev_gray, next_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
```

### 3. 转换为伪彩色光流图

将光流信息转换为 HSV 色彩空间表示，并映射为伪彩色图：

```python
hsv[..., 0] = angle * 180 / np.pi / 2  #方向映射到色相
hsv[..., 2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)  #速度映射到亮度
```

### 4. 图像可视化

使用 Matplotlib 显示原始帧和光流图：

```python
plt.imshow(cv2.cvtColor(flow_rgb, cv2.COLOR_BGR2RGB))
```

---

## 输出

运行代码后，将看到如下输出：

1. 左侧显示视频的原始帧
2. 右侧显示伪彩色光流图，颜色和亮度分别表示方向和速度

---

## 遇到的问题

1. **性能问题**：

   - 光流计算对帧分辨率较敏感。若运行速度较慢，可对视频帧进行下采样：

     ```python
     prev_gray = cv2.resize(prev_gray, (width // 2, height // 2))
     ```

## 学习资源

- [CSDN：optical flow 光流的常见可视化方法，光流图像生成](https://blog.csdn.net/tywwwww/article/details/126125681?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522841b0fa17ced6a12c7e648c6117d2f80%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=841b0fa17ced6a12c7e648c6117d2f80&biz_id=0&spm=1018.2226.3001.4187)
- [PyTorch官方教程](https://pytorch.org/tutorials/)
---

欢迎反馈问题或建议！ 😊
