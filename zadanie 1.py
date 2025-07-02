import cv2
import numpy as np
import sys


face_cascade= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Rozpocznij przechwytywanie wideo z domyślnej kamery
video_capture = cv2.VideoCapture(0)

# Funkcja do wykrywania ruchu głowy
def head_direction(face_x, face_w, frame_width):
    center_x = face_x + face_w // 2  # Środek wykrytej twarzy
    if center_x < frame_width // 3:  # Lewa część ekranu
        return "lewo"
    elif center_x > 2 * frame_width // 3:  # Prawa część ekranu
        return "prawo"
    else:
        return "środek"

while True:
    # Przechwyć klatkę po klatce
    ret, frame = video_capture.read()
    if not ret:
        break

    # Detekcja twarzy
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Rysowanie prostokątów wokół wykrytych twarzy
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Wyświetlenie informacji o kierunku głowy
        direction = head_direction(x, w, frame.shape[1])
        cv2.putText(frame, direction, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Detekcja dłoni (koloru skóry)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Znajdź kontury w masce
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Rysowanie prostokątów wokół wykrytych dłoni
    for contour in contours:
        if cv2.contourArea(contour) > 1000:  # Filtrowanie małych konturów
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Wyświetl wynikową klatkę
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Po zakończeniu, zwolnij przechwytywanie
video_capture.release()
cv2.destroyAllWindows()
