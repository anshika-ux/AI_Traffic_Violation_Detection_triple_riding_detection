from ultralytics import YOLO

model = YOLO("best.pt")
results = model.val(
    data="triple_riding.v1-triple_riding.yolov8/data.yaml",
    split="val",
    imgsz=640,
    conf=0.001,
    plots=True,
)