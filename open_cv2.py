# reshape the image

##  Read n show the image

import cv2
# read colored image
img=cv2.imread("C:\\Users\\qwertyuiop\\Desktop\\n3.jpeg",1)
#print(img)

# resizing
resize=cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))


cv2.imshow("babe",img)
cv2.waitKey(0)
cv2.destroyAllWindows()