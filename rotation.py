import cv2
img = cv2.imread("meme4.jpg")

(height,width) = img.shape[:2]
center = (width//2 ,height//2)
M = cv2.getRotationMatrix2D(center, 90,1.0)            #cv2.getRotationMatrix2D(center, angle, scale)  
rotated = cv2.warpAffine(img, M, (width, height))         #cv2.warpAffine(image, M, (width, height))

cv2.imshow("original", img)
cv2.imshow("rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()