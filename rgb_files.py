import cv2

import numpy as np 

img = np.zeros((10,10,3),np.uint8)


img[0,0]=(255 ,0,0) #for blue square 

img[0,1]=(0,255,0) #for green square
 
img[0,2]=(0,0,255) #for red square

img[0,3]=(255) #for white square

img [1,0] = (0,150,150) #dark yellow

# a total of 256 * 256 * 256 =16,777,216 color formation can be made


img = cv2.resize(img ,(1000,1000), interpolation =cv2.INTER_AREA)

cv2.imshow("IMAGE", img)

cv2.waitKey(0)