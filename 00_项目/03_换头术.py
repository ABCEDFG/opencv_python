import cv2
import numpy as np

cap=cv2.VideoCapture(0)

face=cv2.CascadeClassifier("E:/000/xml/haarcascade_frontalface_alt2.xml")
img = cv2.imread('E:/000/12.png')

g = img.shape

while(cap.isOpened()):
    ret,lend=cap.read()
    
    gray=cv2.cvtColor(lend,cv2.COLOR_BGR2GRAY)
    
    faces=face.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(5,5))
    
    for(x,y,w,h) in faces:
        #dstImage = np.zeros((w+15,h+20,3),np.uint8)
        
        for i in range(0,h+20):
            for j in range(0,w+15):
                iNew = int(i*g[0]*1.0/(h+20))
                jNew = int(j*g[1]*1.0/(w+15))
                
                lend[i+y-25,j+x-15] = img[iNew,jNew]
        
        cv2.imshow("img",lend)
        #cv2.rectangle(img,(x,y),(x+w,y+w),(0,255,0),2)
        # for i in range(0,h):
            # for j in range(0,w):
                # img[x+i,y+j]=dstImage[i,j]
    
    
    
    c=cv2.waitKey(1)
    if c==27:
        break

cap.release()
cv2.destroyAllWindows()




















