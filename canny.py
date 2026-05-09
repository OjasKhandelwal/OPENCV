import cv2
import numpy as np
img = cv2.imread("meme4.jpg", cv2.IMREAD_GRAYSCALE)
#canny edge detection - used for -> 1) detect borders    2)seperate objects    3)feature extraction
edges = cv2.Canny(img,50,150)               #Canny(image,threshold1,threshold2)
cv2.imshow("original", img)
cv2.imshow("edged", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

''' 
Canny checks intensity changes in the image.
Large intensity change → likely edge
Small intensity change → probably noise

The two thresholds classify edges.

| Threshold    | Purpose         |
| ------------ | --------------- |
| `threshold1` | Lower threshold |
| `threshold2` | Upper threshold |



In canny thresholding -> Brightness difference between nearby pixels is checked 
eg- sudden change → edge       smooth region → no edge
'''