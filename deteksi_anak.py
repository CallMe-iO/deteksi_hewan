import cv2
import torch
import pyttsx3
import time

# Load model YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')  # pastikan ini model YOLOv5

# Inisialisasi text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Fungsi bicara
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Untuk menghindari bicara berulang
last_detected = ""
last_spoken_time = 0

# Mulai webcam
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Deteksi
    results = model(frame)

    # Konversi hasil ke pandas
    df = results.pandas().xyxy[0]

    for index, row in df.iterrows():
        label = row['name']
        conf = row['confidence']
        x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])

        # Label dengan emoji
        if label == 'zebra':
            display_text = "😺 Ini kucing lucu!"
            speech_text = "Ini kucing, meow meow!"
        elif label == 'rhino':
            display_text = "🐶 Anjing pintar!"
            speech_text = "Ini anjing, gug gug!"
        else:
            display_text = f"📦 {label}"
            speech_text = f"Ini adalah {label}"

        # Gambar kotak & teks
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)
        cv2.putText(frame, display_text, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

        # Bicarakan jika beda deteksi dan jeda cukup
        current_time = time.time()
        if label != last_detected or current_time - last_spoken_time > 5:
            speak(speech_text)
            last_detected = label
            last_spoken_time = current_time

    cv2.imshow("Deteksi Hewan untuk Anak-Anak", frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bersihkan
cap.release()
cv2.destroyAllWindows()
