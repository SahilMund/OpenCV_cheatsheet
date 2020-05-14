#using compter cam to capture a videoe and process it

import cv2,time

video=cv2.VideoCapture(0)
a=1

while True:
    a=a+1
    check,frame= video.read()
    print(check)
    print(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("capturing",frame)
    
    key=cv2.waitKey(1) #we are generating a new frame in every 1 milliseconds
    
    if key == ord('z'):
        break

print(a)  #total number of frames


video.release()
cv2.destroyAllWindows()
