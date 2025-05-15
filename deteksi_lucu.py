import cv2
import torch

# Load model YOLOv5 hasil training sendiri
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')  # model YOLOv5

# Buka webcam
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Deteksi objek
    results = model(frame)
    detections = results.pandas().xyxy[0]

    for index, row in detections.iterrows():
        label = row['name']
        conf = row['confidence']
        x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])

        # Label lucu untuk anak-anak
        if label == 'zebra':
            display_text = "Hai Aku Zebra!"
        elif label == 'rhino':
            display_text = "HIDUP JOKOWI"
        elif label == 'bird':
            display_text = "🐦 Burung ceria!"
        elif label == 'cow':
            display_text = "🐮 Sapi besar!"
        else:
            display_text = f"📦 {label}"

        # Gambar kotak & teks
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, display_text, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

    # Tampilkan hasil
    cv2.imshow("Deteksi Hewan untuk Anak-Anak 🐾", frame)

    # Tekan Q untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bersihkan
cap.release()
cv2.destroyAllWindows()
