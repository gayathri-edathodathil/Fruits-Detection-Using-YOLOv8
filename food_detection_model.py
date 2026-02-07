from ultralytics import YOLO
import os
import cv2
from ultralytics.utils.plotting import Annotator

MODEL_PATH = "runs/detect/train/weights/best.pt"
TEST_IMAGE_DIR = "dataset/images/test"
OUTPUT_DIR = "predict_test"
CONFIDENCE = 0.25

video=cv2.VideoCapture(0)
model = YOLO(MODEL_PATH)

while True:
    _,frame=video.read()

    results = model.predict(source=frame)
    for r in results:
        annotator=Annotator(frame)
        boxes=r.boxes
        for box in boxes:
            b=box.xyxy[0]
            c=box.cls
            annotator.box_label(b,model.names[int(c)])
    frame=annotator.result()
    cv2.imshow("Fruit detection, Press space to Exit",frame)
    key=cv2.waitKey(1)
    if key==ord(' '):
        break
video.release()
cv2.destroyAllWindows()

print("Prediction complete")

