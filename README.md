# Face and Hand Tracker 🎥🖐️

This project is a real-time face and hand detection system using OpenCV. It captures video from your webcam and detects:

- Faces using Haar Cascade classifiers
- Head direction (left / center / right) based on face position
- Hands based on skin color detection in the HSV color space

## 📦 Features

- ✅ Real-time webcam capture
- ✅ Face detection with bounding box
- ✅ Head direction estimation (left, center, right)
- ✅ Hand detection using color segmentation and contour area filtering

## ▶️ How to Run

1. Make sure you have Python and OpenCV installed:
   ```bash
   pip install opencv-python numpy
Run the script:

bash
Копировать
Редактировать
python face_hand_tracker.py
Press q to quit the app.

💻 Dependencies
Python 3.x

OpenCV (opencv-python)

NumPy

🧠 Notes
Hand detection is based on color range in HSV, so results may vary in different lighting conditions.

Haar Cascade files are included in OpenCV by default (via cv2.data.haarcascades).
