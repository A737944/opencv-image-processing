import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 定義顏色
white = (255, 255, 255)
red = (0, 0, 255)

# 定義添加中文文字
def cv2_Chinese_Text(img, text, left, top, textColor, fontSize):
    # 檢查圖像是否為 NumPy 陣列格式，如果是則轉換為 PIL 格式
    if isinstance(img, np.ndarray):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 轉換為 RGB 格式
    draw = ImageDraw.Draw(img)  # 建立 PIL 繪圖物件
    # 使用指定的字體和大小
    fontText = ImageFont.truetype("C:\\Windows\\Fonts\\mingliu.ttc", fontSize, encoding='utf-8')
    # 在圖像上繪製中文文本
    draw.text((left, top), text, textColor, font=fontText)
    # 轉換回 OpenCV 圖像格式 (BGR)
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

# 1. 讀取 lena(3).jpg 圖片
img = cv2.imread('lena(3).jpg')
cv2.imshow('lena', img)  # 顯示原始圖片

# 2. 繪製矩形
cv2.rectangle(img, (100, 100), (250, 260), red)  # 左上角(100,100)，右下角(250,260)，顏色為紅色

# 3. 添加中文文字
img = cv2_Chinese_Text(img, '徐浩芳', 220, 280, white, 30)  # 添加文字“徐浩芳”，白色，大小 30

# 4. 繪製橢圓
cv2.ellipse(img, (260, 295), (55, 25), 0, 0, 360, white, 3)  # 中心點(260,295)，半徑(55,25)，顏色為白色

# 顯示修改後的圖像
cv2.imshow('lenal', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5. 讀取 back(2).jpg 圖片
img2 = cv2.imread('back(2).jpg')
cv2.imshow('back', img2)  # 顯示背景圖像

# 6. 圖像加權混合 (透明疊加)
alpha = 1    # lena 圖像的權重
beta = 1     # back 圖像的權重
gamma = 1    # 亮度增量
dst = cv2.addWeighted(img, alpha, img2, beta, gamma)  # 合併圖像
cv2.imshow('lena+back', dst)  # 顯示疊加圖像
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7. 轉換為灰階圖像
img_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
cv2.imshow('GRAY_Color_Space', img_gray)  # 顯示灰階圖

# 8. 應用自適應閾值分割
thresh = 127
maxval = 255

# 自適應閾值（平均值法）
dst_mean = cv2.adaptiveThreshold(img_gray, maxval, cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY, 3, 5)  # 核大小為 3，減去常數 C=5
cv2.imshow('ADAPTIVE_THRESH_MEAN_C', dst_mean)

# 自適應閾值（高斯法）
dst_gauss = cv2.adaptiveThreshold(img_gray, maxval, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY, 3, 5)  # 核大小為 3，減去常數 C=5
cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_C', dst_gauss)

# 等待按鍵並關閉所有窗口
cv2.waitKey(0)
cv2.destroyAllWindows()