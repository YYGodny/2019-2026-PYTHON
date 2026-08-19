import cv2
import numpy as np

rightp_cascade = cv2.CascadeClassifier('rpalm.xml')
fist_cascade = cv2.CascadeClassifier('fist.xml')
leftp_cascade = cv2.CascadeClassifier('lpalm.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rhand = rightp_cascade.detectMultiScale(gray)
    lhand = leftp_cascade.detectMultiScale(gray)
    fist = fist_cascade.detectMultiScale(gray) #1.3, 5
    for (x,y,w,h) in rhand:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = img[y:y+h, x:x+w]
        ###finger = fingercascadeosv...

    for (x, y, w, h) in fist:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

    for (x, y, w, h) in lhand:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
