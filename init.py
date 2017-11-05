import cv2,random
import numpy as np

def getCalibratedxy(x,y,e):
    x = int(x - 0.1*e)
    y = int(y + 0.1*e)
    return (x,y)

def markPosition(img,pos,mark):
    e,_,_ = img.shape
    font = cv2.FONT_HERSHEY_SIMPLEX
    if pos%3 != 0:
        x = (e/3)*(pos%3-0.5)
    else:
        x = 5*e/6

    if pos%3 !=0:
        y = (e/3)*(0.5+int(pos/3))
    else:
        y = (e/6)+(pos/3-1)*(e/3)
    if mark is 0:
        cv2.putText(img,'o',getCalibratedxy(x,y,e), font, 4,(255,255,255),2)
    elif mark is 1:
        cv2.putText(img,'x',getCalibratedxy(x,y,e), font, 4,(255,255,255),2)
    return img

def drawLines(img):
    e,_,_ = img.shape
    cv2.line(img,(e/3,0),(e/3,e),(255,0,0),5)
    cv2.line(img,(2*e/3,0),(2*e/3,e),(255,0,0),5)
    cv2.line(img,(0,e/3),(e,e/3),(255,0,0),5)
    cv2.line(img,(0,2*e/3),(e,2*e/3),(255,0,0),5)
    return img



e = 300
img = cv2.imread('img.jpg')
img = drawLines(img)
for x in range(1,10):
    img = markPosition(img,x,x%2)

cv2.imshow("tic tac toe",img)
cv2.waitKey(0)
