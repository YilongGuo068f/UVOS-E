# README: 使用 Python 生成光流图




## 依赖库

- OpenCV
- Numpy
- Matplotlib

安装依赖库：

```bash
pip install opencv-python matplotlib
```
需要修改代码为自己的内容

```python
video_path = "XXX.mp4" #需要替换的视频路径
frame_index = 0 #需要替换成要分析的帧号
```



## 使用方法

#### 输出：

1. **原始帧**：选定帧的图像，用于直观对比
2. **光流图**：对应帧的伪彩色光流图，包含运动方向和速度的信息


### 1. 加载视频和指定帧

通过 `cv2.VideoCapture` 打开视频并提取指定帧及其下一帧

```python
cap = cv2.VideoCapture(video_path)
ret, frame1 = cap.read()
```

### 2. 计算光流

使用 OpenCV 的 `cv2.calcOpticalFlowFarneback` 方法，计算两帧之间的光流信息

```python
flow = cv2.calcOpticalFlowFarneback(prev_gray, next_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
```

### 3. 转换为伪彩色光流图

将光流信息转换为 HSV 色彩空间表示，并映射为伪彩色图

```python
hsv[..., 0] = angle * 180 / np.pi / 2  #方向映射到色相
hsv[..., 2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)  #速度映射到亮度
```

### 4. 图像可视化

使用 Matplotlib 显示原始帧和光流图

```python
plt.imshow(cv2.cvtColor(flow_rgb, cv2.COLOR_BGR2RGB))
```


## 学习资源

- [CSDN：optical flow 光流的常见可视化方法，光流图像生成](https://blog.csdn.net/tywwwww/article/details/126125681?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522841b0fa17ced6a12c7e648c6117d2f80%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=841b0fa17ced6a12c7e648c6117d2f80&biz_id=0&spm=1018.2226.3001.4187)
- [PyTorch官方教程](https://pytorch.org/tutorials/)
---

欢迎反馈问题或建议！ 😊
