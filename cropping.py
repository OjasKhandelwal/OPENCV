import cv2
img = cv2.imread("meme4.jpg")


cropped = img[100:200 , 50:150]

cv2.imshow("original", img)
cv2.imshow("cropped", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()