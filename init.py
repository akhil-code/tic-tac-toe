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

def getPositionFromXY(x,y):
    global e
    x_pos,y_pos = (-1,-1)

    if x>0 and x<e/3:
        x_pos = 1
    elif x>e/3 and x<(2*e/3):
        x_pos = 2
    elif x>(2*e/3) and x<e:
        x_pos = 3

    if y>0 and y<e/3:
        y_pos = 0
    elif y>e/3 and y<(2*e/3):
        y_pos = 1
    elif y>(2*e/3) and y<e:
        y_pos = 2

    return x_pos+y_pos*3

def checkGame(marked):
    for x in range(0,7,3):
        if marked[x]==marked[x+1] and marked[x+1]==marked[x+2] and marked[x] != -1:
            return True
    for y in range(3):
        if marked[y]==marked[y+3] and marked[y+3]==marked[y+6] and marked[y] != -1:
            return True

    if marked[0]==marked[4] and marked[4]==marked[8] and marked[0] != -1:
        return True
    if marked[2]==marked[4] and marked[4]==marked[6] and marked[2] != -1:
        return True
    return False

# mouse callback function
def clicked(event,x,y,flags,param):
    global counter,img,marked
    if event == cv2.EVENT_LBUTTONUP:
        img = markPosition(img,getPositionFromXY(x,y),counter%2)
        marked[getPositionFromXY(x,y)-1] = counter%2
        cv2.imshow("tic tac toe",img)
        cv2.waitKey(10)
        if checkGame(marked):
            cv2.waitKey(1000)
            if(counter%2)==0:
                print 'O won the game'
            else:
                print 'X won the game'
            counter = 0
            marked = [-1 for i in range(9)]
            img = cv2.imread('img.jpg')
            img = drawLines(img)
            return
        elif counter>=8:
            cv2.waitKey(1000)
            print 'match draw'
            counter = 0
            marked = [-1 for i in range(9)]
            img = cv2.imread('img.jpg')
            img = drawLines(img)
            return
        counter += 1


img = cv2.imread('img.jpg')
e,_,_ = img.shape
marked = [-1 for i in range(9)]
counter = 0
img = drawLines(img)
cv2.namedWindow("tic tac toe")
cv2.setMouseCallback("tic tac toe",clicked)

while True:
    cv2.imshow("tic tac toe",img)
    if cv2.waitKey(5) & 0xFF == 27:
        break
