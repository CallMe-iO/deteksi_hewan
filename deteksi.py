import torch
import cv2

# Load model YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)

# Buka webcam
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Deteksi objek
    results = model(frame)

    # Plot hasil deteksi
    annotated_frame = results.render()[0]

    # Tampilkan frame
    cv2.imshow('YOLOv5 Webcam Detection', annotated_frame)

    # Tekan q untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
