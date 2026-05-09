import cv2
import numpy as np

img1 = np.zeros((300,300), dtype="uint8")
img2 = np.zeros((300,300), dtype="uint8")

cv2.circle(img1, (150, 150), 100, 255, -1)
cv2.rectangle(img2, (100,100), (250,250), 255, -1)

bt1 = cv2.bitwise_and(img1, img2)       #bitwise_and(img1, img2)
bt2 = cv2.bitwise_or(img1, img2)       #bitwise_or(img1, img2)
bt3 = cv2.bitwise_not(img1)        #bitwise_not(img1)  

cv2.imshow("Circle", img1)
cv2.imshow("Rectangle", img2)

cv2.imshow("AND", bt1)
cv2.imshow("OR", bt2)
cv2.imshow("NOT", bt3)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
1) and - Keeps only pixels that are present in BOTH images.  Only overlapping bright regions survive.
Useful for: masking objects , extracting ROI (region of interest)


2) or - Combines both images.     If a pixel is white in ANY image → white in result.
Useful for:merging masks , combining shapes

3) not - Inverts image.  black becomes white, white becomes black, colors invert
'''