# YOLOv5 Webcam Detection

Program ini digunakan untuk mendeteksi objek secara real-time lewat webcam menggunakan model YOLOv5 yang sudah dilatih (`best.pt`).

## Isi Folder

- `model/best.pt` → Model Terbaik Dari hasil training YOLOv5.
- `model/last.pt` → Model Terakhir Dari hasil training YOLOv5.
- `main.py` → Script utama untuk menjalankan deteksi dari webcam.
- `.gitignore`, `.gitattributes`, `README.md` → File tambahan untuk keperluan git dan dokumentasi.

## Cara Pakai

1. **Install dulu library yang dibutuhkan:**

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install opencv-python
```

2. **Jalankan program:**

```bash
python main.py
```

3. **Tekan `q` untuk keluar dari jendela webcam.**

## Catatan

- Kalau webcam nggak nyala, ubah angka di `cv2.VideoCapture(1)` jadi `0` atau angka lain tergantung kamera yang aktif di laptop/PC kamu.
- Model `best.pt` ini adalah model hasil training sendiri, jadi hasil deteksinya tergantung data yang dipakai waktu training.

## Sumber
datasets : https://www.kaggle.com/datasets/ankanghosh651/object-detection-wildlife-dataset-yolo-formathttps://www.kaggle.com/datasets/ankanghosh651/object-detection-wildlife-dataset-yolo-format
Model menggunakan YOLOv5 dari Ultralytics: https://github.com/ultralytics/yolov5
