import cv2

import numpy as np

# black squares

img = np.zeros((10,10), np .uint8)

img = cv2.resize(img ,(1000,1000), interpolation =cv2.INTER_AREA)

cv2.imshow("IMAGE", img)

cv2.waitKey(0)