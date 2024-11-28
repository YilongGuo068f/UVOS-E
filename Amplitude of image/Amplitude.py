import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_color_amplitude_spectrum(image_path):
    #读取图像并转换为灰度图
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"图像加载失败，请检查路径：{image_path}")
        return

    #应用傅里叶变换
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)  #将低频部分移到图像中心

    #计算幅度谱
    magnitude_spectrum = np.abs(fshift)
    magnitude_spectrum_log = 20 * np.log(magnitude_spectrum + 1)  #对数缩放

    #使用伪彩色映射显示幅度谱
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(magnitude_spectrum_log, cmap='jet')  #使用伪彩色映射
    plt.title('Magnitude Spectrum (Color)')
    plt.axis('off')

    plt.show()

#输入图像路径
image_path = "D:\\Tz\\2023-09-08T21-37-05-983.jpg"
show_color_amplitude_spectrum(image_path)
