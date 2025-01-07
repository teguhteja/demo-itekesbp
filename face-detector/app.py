import numpy as np
import cv2
from playsound import playsound
# import winsound 

cap = cv2.VideoCapture(4)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

r = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame from webcam. Check device index and connection.")
        break
    
    frame = cv2.resize(frame, (800, 700))
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        ff_gray = gray[y : y + w, x : x + w]
        ff_color = frame[y : y + w, x : x + w]

        eyes = eye_cascade.detectMultiScale(ff_gray, 1.3, 5)

        for ex, ey, ew, eh in eyes:
            cv2.rectangle(ff_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    if type(faces) == tuple:
        r += 1
    else:
        r = 0

    print("r =", r)

    if r > 30:
        r = 0
        print("Candidate maybe cheating...")
        # winsound.Beep(500,200)
        playsound("mixkit-emergency-alert-alarm-1007.wav")
        break

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
