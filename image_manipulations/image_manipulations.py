import cv2
import numpy as np
# 讀取圖像檔案
src = cv2.imread('HW3(2).jpg')  # 載入名為 HW3(2).jpg 的圖片
cv2.imshow('Src', src)  # 顯示原圖
# 調整圖片大小
# fx = 0.8 表示寬度縮放為 80%，fy = 1.5 表示高度放大為 150%
dst = cv2.resize(src, None, fx=0.8, fy=1.5)
cv2.imshow('Dst', dst)  # 顯示調整大小後的圖片
# 水平翻轉圖片 (1 表示水平翻轉，0 表示垂直翻轉，-1 表示同時翻轉)
dst1 = cv2.flip(dst, 1)
cv2.imshow('Dst1', dst1)  # 顯示翻轉後的圖片
# 使用高斯模糊處理圖片
# (5,5) 表示高斯模糊的內核大小，0 表示自動計算標準差
dst = cv2.GaussianBlur(dst1, (5, 5), 0, 0)
cv2.imshow('Dst2', dst)  # 顯示模糊處理後的圖片
cv2.waitKey(0)  # 等待按鍵
cv2.destroyAllWindows()  # 關閉所有視窗
# 顯示翻轉後的圖片 (重新打開視窗)
cv2.imshow('Dst1', dst1)
# 定義一個 5x5 的內核，內核值全為 1
kernel = np.ones((5, 5), np.uint8)
# 進行形態學操作：開運算 (先腐蝕再膨脹，用於去除噪點)
dst = cv2.morphologyEx(dst1, cv2.MORPH_OPEN, kernel)
cv2.imshow('after OPEN', dst)  # 顯示開運算結果
# 進行形態學操作：閉運算 (先膨脹再腐蝕，用於填補小孔洞)
dst = cv2.morphologyEx(dst1, cv2.MORPH_CLOSE, kernel)
cv2.imshow('after CLOSE', dst)  # 顯示閉運算結果
# 進行形態學操作：形態學梯度 (膨脹結果減去腐蝕結果，提取邊緣)
dst = cv2.morphologyEx(dst1, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('after morpological gradient', dst)  # 顯示形態學梯度結果
# 進行形態學操作：頂帽運算 (原圖減去開運算結果，提取亮區細節)
dst = cv2.morphologyEx(dst1, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('after tophat', dst)  # 顯示頂帽運算結果
# 進行形態學操作：黑帽運算 (閉運算結果減去原圖，提取暗區細節)
dst = cv2.morphologyEx(dst1, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('after blackhat', dst)  # 顯示黑帽運算結果
cv2.waitKey(0)  # 等待按鍵
cv2.destroyAllWindows()  # 關閉所有視窗
