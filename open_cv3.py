# face detection from an image by rectangular box


import cv2

#create a CascadeClassifier object
face_cascade=cv2.CascadeClassifier("C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml'")
# read colored image
img=cv2.imread("C:\\Users\\qwertyuiop\\Desktop\\openCV\\p.jpg",1)

#reading the image as gray scale image  or converting the colored image to gray scale image
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#search the coordinates of the face rectangle coordinates in image
# 1.  scaleFactor:---  decreses the shape value by 5%,untill the face is found.[smaller this vale gretaer the accuracy]  
faces=face_cascade.detectMultiScale(gray_image,scaleFactor=1.05,minNeighbors=5)

#giving rectangular box to the image
for x,y,w,h in faces:
    img=cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)
    
cv2.imshow("babe",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

