import cv2

# 載入訓練好的分類器
cascade = cv2.CascadeClassifier('classifier/cascade.xml')

# 讀入測試影像
img = cv2.imread('test5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 偵測物件
objects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=17)

# 繪製方框
for (x, y, w, h) in objects:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 顯示結果
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
