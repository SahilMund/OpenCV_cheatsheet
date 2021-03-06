# face  n eye detection  in video taken b y webcam


import cv2,time

#create a CascadeClassifier object
face_cascade=cv2.CascadeClassifier('C:\\Users\\qwertyuiop\\Desktop\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\qwertyuiop\\Desktop\\haarcascade_eye.xml')

video=cv2.VideoCapture(0)
while True:
    
    check,frame= video.read()
    # read colored image
    #img=cv2.imread(frame,1)
    
    #reading the image as gray scale image  or converting the colored image to gray scale image
    gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #search the coordinates of the face rectangle coordinates in image
    # 1.  scaleFactor:---  decreses the shape value by 5%,untill the face is found.[smaller this vale gretaer the accuracy]  
    faces=face_cascade.detectMultiScale(gray_image,scaleFactor=1.05,minNeighbors=5)
   
    #giving rectangular box to the image
    for x,y,w,h in faces:
        img=cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),3)
        roi_gray = gray_image[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        image_item="my_image.png"
        cv2.imwrite(image_item,roi_gray)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    cv2.imshow("capturing",frame)
    
    key=cv2.waitKey(1) #we are generating a new frame in every 1 milliseconds
    
    if key == ord('z'):
        break
 
time.sleep(3)
video.release()

cv2.destroyAllWindows()


