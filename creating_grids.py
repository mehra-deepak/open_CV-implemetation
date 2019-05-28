import cv2

import numpy as np

# black squares

img = np.zeros((10,10), np .uint8)

img[0,0]=255

img[0,1]=200

img[0,2]=100

img[0,2]=25


img = cv2.resize(img ,(1000,1000), interpolation =cv2.INTER_AREA)

cv2.imshow("IMAGE", img)

cv2.waitKey(0)