from ultralytics import YOLO
import cv2
model = YOLO('../Yolo-Weights/yolov8l.pt')
results = model("img-5.jpg",show=True)
cv2.waitKey(0)
# ../  that mean go back
# here yolov8l mean it detect all think in detail which in background
# and yolov8n is scan only limited think (n = nano and l = large) , this 8l and 8n very usefully for constant image or fix camera not perfect for video scan
