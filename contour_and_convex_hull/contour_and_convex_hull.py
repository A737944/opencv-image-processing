import cv2
import numpy as np

# 讀取影像
src = cv2.imread("HW5(2).jpg")
cv2.imshow('src', src)  # 顯示原始影像

# 將彩色影像轉換為灰度影像
src_gary = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 二值化處理影像，將灰度影像轉換為黑白影像
ret, dst_binary = cv2.threshold(src_gary, 50, 255, cv2.THRESH_BINARY)

# 找出影像內的輪廓
# cv2.findContours 返回輪廓和層次結構
contours, hierarchy = cv2.findContours(dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 在原影像上繪製輪廓
# -1 表示繪製所有輪廓，(0, 0, 255) 為紅色，5 為線條寬度
dst1 = cv2.drawContours(src, contours, -1, (0, 0, 255), 5)
cv2.imshow("dst1", dst1)  # 顯示繪製了輪廓的影像
cv2.waitKey(0)
cv2.destroyAllWindows()

# 創建白色遮罩影像，與原影像大小相同
mask = np.ones(src.shape, np.uint8)
mask.fill(255)  # 填充為白色

# 在遮罩上繪製輪廓，填充內部為黑色
dst2 = cv2.drawContours(mask, contours, -1, (0, 0, 0), -1)
cv2.imshow('dst2', dst2)  # 顯示遮罩影像

# 使用 bitwise_or 將原影像與遮罩影像進行邏輯或操作
# 這裡會顯示遮罩應用的效果
dst3 = cv2.bitwise_or(src, mask)
cv2.imshow('dst3', dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 計算每個輪廓的中心點，並在影像上標記
for c in contours:
    M = cv2.moments(c)  # 計算輪廓的矩
    Cx = int(M['m10'] / M['m00'])  # 計算 x 坐標中心
    Cy = int(M['m01'] / M['m00'])  # 計算 y 坐標中心
    cv2.circle(dst1, (Cx, Cy), 5, (255, 0, 0), -1)  # 在中心點畫藍色圓點
cv2.imshow('dst1 with center', dst1)  # 顯示包含中心點的影像

# 計算輪廓的最小包圍矩形
box = cv2.minAreaRect(contours[0])  # 取得最小包圍矩形
print(f'轉換前的矩形頂角 = \n {box}')

# 將矩形轉換為頂點座標
points = cv2.boxPoints(box)
points = np.int_(points)
print(f'轉換後矩形頂角 = \n {points}')

# 在影像上繪製最小包圍矩形
dst = cv2.drawContours(dst1, [points], 0, (0, 255, 0), 2)
cv2.imshow('dst', dst)  # 顯示包含最小包圍矩形的影像
cv2.waitKey(0)
cv2.destroyAllWindows()

# 再次讀取影像用於凸包處理
src = cv2.imread('HW5(2).jpg')

# 計算凸包
hull = cv2.convexHull(contours[0])  # 計算指定輪廓的凸包

# 在影像上繪製凸包
dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)
cv2.imshow('dst', dst)  # 顯示包含凸包的影像

# 計算凸包面積
convex_area = cv2.contourArea(hull)
print(f'凸包面積 = {convex_area}')

cv2.waitKey(0)
cv2.destroyAllWindows()
