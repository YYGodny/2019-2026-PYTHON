import cv2
import numpy as np

###### ep 1 ##############
##img = cv2.imread('hand.jpg', cv2.IMREAD_GRAYSCALE)
##
##cv2.imshow('image', img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()


######## ep 2 ###########
##cap = cv2.VideoCapture(0)
##
##while True:
##    ret, frame = cap.read()
##    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
##    
##    cv2.imshow('frame', frame)
##    cv2.imshow('gray', gray)
##    
##
##    if cv2.waitKey(1) & 0xFF == ord('q'):
##        break
##
##cap.release()
##cv2.destroyAllWindows()


###### ep 3 ###########
##img = cv2.imread('hand.jpg', cv2.IMREAD_COLOR)
##
##cv2.line(img, (0,0), (150, 150), (255, 0, 0), 15)
##cv2.rectangle(img, (100,100), (500, 500), (0, 255, 0), 10)
##cv2.circle(img, (300, 300), 200, (0, 0, 255), -1)
##
##pts = np.array([[150, 100],[400, 500], [200, 100], [400, 500],[250, 100],[400, 500], [300, 100],[400, 500], [350, 100]], np.int32)
####pts = pts.reshape((-1, 1, 2))
##cv2.polylines(img, [pts], False, (0, 255, 0), 3)
##
##font = cv2.FONT_HERSHEY_SIMPLEX
##cv2.putText(img, 'hei', (400, 500), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
##
##cv2.imshow('image', img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()


###### ep 4 ########
##img = cv2.imread('hand.jpg', cv2.IMREAD_COLOR)
##img[64, 72] = [0, 0, 0]
##px = img[64, 72]
##print(px)
###img[90: 600, 100: 550] = [0, 0 ,0]
##hand = img[90: 600, 100: 550]
##img[0:510, 0:450] = hand
##cv2.imshow('image', img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

######## ep 5 #########
img1 = cv2.imread('hand.jpg')
img2 = cv2.resize(cv2.imread('hand2.jpg'), (637, 720), interpolation=cv2.INTER_AREA)
img3 = cv2.imread('banana joe.jpg')

#add = img1 + img2
#add = cv2.add(img1, img2)

##weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
##cv2.imshow('weighted', weighted)

rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]

img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img3gray, 220, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()


