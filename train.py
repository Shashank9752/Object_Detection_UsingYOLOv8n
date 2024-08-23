
from google.colab import drive
drive.mount('/content/drive')

# %cd /content/drive/MyDrive/yolo
#train the model
!yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=20 imgsz=640 plots=True