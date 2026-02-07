# Fruits Detection Using YOLOv8
This project trains a custom model on YOLOv8 to recognize and label apple, banana and orange.

## Dataset
- Dataset consists of fruit images annotated with bounding boxes
- Converted raw dataset in Pascal VOC(XML) form to YOLO compatible form
- Corrupted annotations where removed correctly from the dataset
Class Labels:
- Apple
- Banana
- Orange

## Project Structure

fruit-detection/<br>
├── dataset/<br>
│   ├── images/<br>
│   │   ├── train/<br>
│   │   └── test/<br>
│   └── labels/<br>
│       ├── train/<br>
│       └── test/<br>
├── runs/<br>
│   └── detect/<br>
│       ├── train/<br>
│       └── predict_test/<br>
|           └── results/<br>
|           └── videocapture/<br>
├── .gitignore<br>
├── food_detection_model.py<br>
├── data.yaml<br>
└── README.md

## Teck Stack
- Python 3.13.1
- OpenCv
- Ultralytics YOLOv8

## Model Training

YOLOv8 was trained using the Ultralytics framework.

Command used:
```
yolo detect train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640
```
Trained Model is saved in:
```
runs/detect/train/weights/best.pt
```
To predict labels for test image run this line in command line:

```
yolo detect predict model=runs/detect/train/weights/best.pt source=path/to/your_test_image.jpg
```
Result will be saved at:
```
runs/detect/predict/
 ├── image.jpg
 └── labels/
```

## Live video annotation
To run the model on live video to detect labels and annotate bounding boxes run:
```
food_detection_model.py
```

## Author
Gayathri E
