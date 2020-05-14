##  Read n show the image

import cv2
# read colored image
img=cv2.imread("C:\\Users\\qwertyuiop\\Desktop\\p.jpg",1)
print(img)

cv2.imshow("babe",img)
cv2.waitKey(0)
cv2.destroyAllWindows()