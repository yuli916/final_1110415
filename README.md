# final_1110415
1110415期末專題程式碼
# 車牌偵測器 (Haar Cascade)

本專案使用 OpenCV 的 Haar Cascade 訓練自製車牌偵測器。

## 使用方式

1. 安裝套件：
pip install -r requirements.txt

2. 執行車牌偵測程式：
python detect_plate.py

3. 結果會顯示在畫面上並自動儲存為 `result.jpg`

## 檔案說明

- `classifier/`：訓練完成的 cascade.xml
- `test/`：測試圖片，請放置為 `test.jpg`
- `detect_plate.py`：主程式
