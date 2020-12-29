### Use cv to open webcam

import cv2

videoCapture = cv2.VideoCapture(0)

while True:
    ret, img = videoCapture.read()
    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break