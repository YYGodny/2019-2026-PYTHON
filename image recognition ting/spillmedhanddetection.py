import cv2
import numpy as np
import pygame
import threading



def handdetection():
    cap = cv2.VideoCapture(0)
    
    rightp_cascade = cv2.CascadeClassifier('rpalm.xml')
    fist_cascade = cv2.CascadeClassifier('fist.xml')
    
    while True:
        ret, img = cap.read()
        img = cv2.resize(img, (1920, 1080))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        rhand = rightp_cascade.detectMultiScale(gray)
        fist = fist_cascade.detectMultiScale(gray)

        for (x, y, w, h) in rhand:
            print()
        for (x, y, w, h) in fist:
            print()
        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()


##handdetection()
hb = threading.Thread(target=handdetection)
hb.daemon = True
##hb.start()
pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('handgame')

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

pygame.quit()
