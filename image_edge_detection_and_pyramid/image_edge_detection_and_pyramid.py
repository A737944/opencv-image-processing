import cv2

src = cv2.imread('hand(2).jpg', cv2.IMREAD_GRAYSCALE)
src = cv2.GaussianBlur(src, (3,3), 0)

#Sobel()函數
dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dsty = cv2.Sobel(src, cv2.CV_32F, 0 ,1)
dstx = cv2.convertScaleAbs(dstx)
dsty = cv2.convertScaleAbs(dsty)
dst_sobel = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)

#Scharr()函數
dstx = cv2.Scharr(src, cv2.CV_32F, 1, 0)
dsty = cv2.Scharr(src, cv2.CV_32F, 0, 1)
dstx = cv2.convertScaleAbs(dstx)
dsty = cv2.convertScaleAbs(dsty)
dst_scharr = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)

#Laplacian()函數
dst_tmp = cv2.Laplacian(src, cv2.CV_32F, ksize=3)
dst_lap = cv2.convertScaleAbs(dst_tmp)

#Canny()函數
dst_canny = cv2.Canny(src, 50, 100)

#輸出影像梯度
cv2.imshow('src', src)
cv2.imshow('Canny', dst_canny)
cv2.imshow('Sobel', dst_sobel)
cv2.imshow('Scharr', dst_scharr)
cv2.imshow('Lap;acian', dst_lap)
cv2.waitKey(0)
cv2.destroyAllWindows()

src = cv2.imread('hand(2).jpg')
dst1 = cv2.pyrDown(src) 
dst2 = cv2.pyrDown(dst1)
dst3 = cv2.pyrDown(dst2)
cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()

dst2 = cv2.pyrUp(dst3)
dst1 = cv2.pyrUp(dst2)
src = cv2.pyrUp(dst1)
cv2.imshow('dst3', dst3)
cv2.imshow('dst2', dst2)
cv2.imshow('dst1', dst1)
cv2.imshow('src', src)
cv2.waitKey(0)
cv2.destroyAllWindows()