import argparse
from pathlib import Path

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--model', default='yolov8n.pt', help='Base model to fine-tune')
    p.add_argument('--data', default='datasets/triple_riding/data.yaml', help='Path to data.yaml')
    p.add_argument('--epochs', type=int, default=50)
    p.add_argument('--imgsz', type=int, default=640)
    p.add_argument('--batch', type=int, default=8)
    p.add_argument('--project', default='runs/train')
    p.add_argument('--name', default='triple_riding_yolov8n')
    p.add_argument('--device', default=None, help="Device for training (e.g. 'cpu' or '0')")
    args = p.parse_args()

    try:
        from ultralytics import YOLO
    except Exception as e:
        raise SystemExit("Please install ultralytics (pip install ultralytics)") from e

    model = YOLO(str(args.model))
    print(f"Starting training: model={args.model}, data={args.data}, epochs={args.epochs}")
    model.train(data=str(args.data), epochs=args.epochs, imgsz=args.imgsz, batch=args.batch,
                project=args.project, name=args.name, device=args.device)
    print("Training finished. Check runs/train/<name>/weights/best.pt")

if __name__ == '__main__':
    main()
