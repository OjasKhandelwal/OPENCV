import cv2
import numpy as np
img = cv2.imread("meme4.jpg")

sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharped = cv2.filter2D(img, -1, sharpen_kernel)   #cv2.filter2D(src, ddepth, kernel)
cv2.imshow("original", img)
cv2.imshow("sharped", sharped)
cv2.waitKey(0)
cv2.destroyAllWindows()