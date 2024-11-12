import cv2
import numpy as np
import matplotlib.pyplot as plt

def generate_optical_flow(video_path, frame_index=0):
    #打开视频文件
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("无法打开视频，请检查路径")
        return

    #读取第一帧和第二帧
    ret, frame1 = cap.read()
    current_frame = 0
    while ret and current_frame < frame_index:  #跳到指定帧
        ret, frame1 = cap.read()
        current_frame += 1

    if not ret:
        print(f"无法读取帧 {frame_index}")
        return

    #转换为灰度图
    prev_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    #读取下一帧（用于计算光流）
    ret, frame2 = cap.read()
    if not ret:
        print("无法读取下一帧，光流无法计算")
        return

    next_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    #计算稠密光流
    flow = cv2.calcOpticalFlowFarneback(prev_gray, next_gray, None,
                                        0.5, 3, 15, 3, 5, 1.2, 0)

    #计算光流的方向和幅度
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])

    #根据角度生成伪彩色光流图
    hsv = np.zeros_like(frame1)
    hsv[..., 1] = 255  #设置饱和度
    hsv[..., 0] = angle * 180 / np.pi / 2  #将角度转换为色相值
    hsv[..., 2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)  #按幅度归一化亮度
    flow_rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)  #转换为 RGB 格式

    #显示结果
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
    plt.title(f'Frame {frame_index}')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(flow_rgb, cv2.COLOR_BGR2RGB))
    plt.title('Optical Flow')
    plt.axis('off')

    plt.show()

    #释放视频资源
    cap.release()

#输入视频路径和帧索引
video_path = "D:\\Tz\\190144-887464241_medium.mp4"  #请替换视频文件路径
frame_index = 0  #指定帧索引
generate_optical_flow(video_path, frame_index)
