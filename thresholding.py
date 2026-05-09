import cv2
import numpy as np
img = cv2.imread("meme4.jpg", cv2.IMREAD_GRAYSCALE)
ret, thresholded_image = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)         #threshold(image, thresh_value, max_value, method)
cv2.imshow("original", img)
cv2.imshow("thresh", thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''Thresholding usually works on grayscale images, 
and choosing a suitable threshold value is important because very high or very low thresholds can lose important image details.'''

'''
Normal/Binary Thresholding -> Pixel brightness itself is checked

Example:
bright → white
dark → black
'''