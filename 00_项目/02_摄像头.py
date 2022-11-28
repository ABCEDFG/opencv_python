import cv2
import numpy as np
import time

cap=cv2.VideoCapture(0)

font=cv2.FONT_HERSHEY_SIMPLEX   # 正常大小

i=0
while(cap.isOpened()):
    t1=time.time()
    
    if i==0:
        ret,img1=cap.read()
        img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        img1=cv2.GaussianBlur(img1,(5,5),0,0)
    i=1
    ret,img=cap.read()
    #img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    #img2=cv2.GaussianBlur(img2,(5,5),0,0)
    
    #img = img2 - img1
    #img1=img2
    
    #gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    
    
    c=cv2.waitKey(1)
    if c==27:
        break
   
    t2=time.time()
    fps=1//(t2-t1)
    
    cv2.putText(img,str(fps),(0,50),font,2,(0,255,0),5)        
    cv2.imshow("img",img)
    

cap.release()
cv2.destroyAllWindows()