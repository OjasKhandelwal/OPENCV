import cv2
import numpy as np
img = cv2.imread("circle.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)


contours, heirarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)    #findContours(image, mode, method)
cv2.drawContours(img, contours, -1, (0,0,255), 3) #drawContours(image, contours, contour_index, color, thickness)


'''
#Contours are boundaries/outlines of objects in an image.
Contours detect the shape/boundary of objects.


#hierarchy - Stores relationship between contours.

#mode - Controls which contours should be retrieved. 
examples:cv2.RETR_EXTERNAL, cv2.RETR_TREE

#method- Controls how contour points are stored.
eg- cv2.CHAIN_APPROX_SIMPLE, cv2.CHAIN_APPROX_NONE

'''

#SHAPE DETECTION
for contour in contours:

    approx = cv2.approxPolyDP(contour,0.01 * cv2.arcLength(contour, True),True)   #approxPolyDP(contour, epsilon, True)

    corners = len(approx)

    if corners == 3:
        shape_name = "Triangle"

    elif corners == 4:
        shape_name = "Rectangle"

    elif corners == 5:
        shape_name = "Pentagon"

    elif corners > 5:
        shape_name = "Circle"
    else: 
        shape_name = "unknown"

cv2.drawContours(img, [approx], 0, (0,255,0), 2)
x = approx.ravel()[0]
y = approx.ravel()[1] - 10

cv2.putText(img,shape_name,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,255))

'''
epsilon controls: how accurately the contour should be approximated/simplified
epsilon decides: how much detail to keep
Large object → larger epsilon.
Small object → smaller epsilon.
'''

cv2.imshow("contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

