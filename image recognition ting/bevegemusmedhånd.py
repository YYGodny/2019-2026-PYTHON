import cv2
import numpy as np
import pyautogui


rightp_cascade = cv2.CascadeClassifier('rpalm.xml')
fist_cascade = cv2.CascadeClassifier('fist.xml')
leftp_cascade = cv2.CascadeClassifier('lpalm.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img = cv2.resize(img, (1920, 1080))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rhand = rightp_cascade.detectMultiScale(gray)
    lhand = leftp_cascade.detectMultiScale(gray)
    fist = fist_cascade.detectMultiScale(gray) #1.3, 5
    cx,cy = pyautogui.position()
    for (x,y,w,h) in rhand:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = img[y:y+h, x:x+w]
        ###finger = fingercascadeosv...
        pyautogui.click()
        
    for (x, y, w, h) in fist:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
        if x < pyautogui.size()[0] and y < pyautogui.size()[1]:
            pyautogui.moveTo(pyautogui.size()[0]-x, y)

    for (x, y, w, h) in lhand:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
##    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
