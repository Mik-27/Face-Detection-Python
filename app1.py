import cv2
import time

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
a = 1
face_cascade = cv2.CascadeClassifier(r"venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

while True:
    a = a + 1
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5)
    for x, y, w, h in faces:
        gray = cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Video", gray)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

print(a)
video.release()
cv2.destroyAllWindows()
