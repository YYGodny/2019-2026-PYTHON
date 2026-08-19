import cv2
from engine.object_detection import ObjectDetection

od = ObjectDetection()

cap = cv2.VideoCapture('handvideo.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
