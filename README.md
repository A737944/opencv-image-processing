# OpenCV Image Processing

本專案包含了使用 OpenCV 進行圖像處理的各種操作，包含圖像縮放、翻轉、濾波、邊緣檢測、輪廓檢測等功能。

## 目錄結構

```bash
.
├── image_transformation.py
├── edge_detection.py
├── contour_detection.py
├── README.md
└── images
    ├── HW3(2).jpg
    ├── hand(2).jpg
    └── HW5(2).jpg
說明
image_transformation.py
本程式碼展示了常見的影像處理操作：
圖像縮放：根據設定的比例縮放圖像。
水平翻轉：將圖像進行水平翻轉。
高斯模糊：使用高斯濾波器模糊圖像。
形態學操作：開運算、閉運算、形態學梯度、頂帽運算和黑帽運算等。
edge_detection.py
本程式碼實現了不同的邊緣檢測：
Sobel: 進行水平和垂直方向的 Sobel 邊緣檢測，並將結果合併。
Scharr: 使用 Scharr 算子進行邊緣檢測，結果與 Sobel 相似。
Laplacian: 進行拉普拉斯邊緣檢測。
Canny: 使用 Canny 邊緣檢測算子。
此外，還包含了影像金字塔的上採樣和下採樣，通過多層次的金字塔視覺效果來顯示圖像。
contour_detection.py
本程式碼展示了影像中的輪廓檢測：
二值化：將圖像轉換為黑白影像，便於進行輪廓檢測。
輪廓檢測：使用 cv2.findContours() 函數來檢測圖像中的輪廓。
繪製輪廓：將輪廓繪製到原圖像上。
機能：計算每個輪廓的中心並標註，找到每個輪廓的最小包圍矩形，繪製凸包等。
安裝依賴
請安裝必要的 Python 套件以運行本專案：

bash
複製程式碼
pip install opencv-python numpy
使用說明
將影像放入 images 資料夾中，或修改程式中的檔案路徑。
使用 Python 執行程式碼，例如：
bash
複製程式碼
python image_transformation.py
根據需求修改程式碼中的影像處理步驟，並觀察處理後的結果。
範例影像
HW3(2).jpg：用於測試圖像處理操作的原始影像。
hand(2).jpg：用於測試邊緣檢測的原始影像。
HW5(2).jpg：用於測試輪廓檢測的原始影像。
