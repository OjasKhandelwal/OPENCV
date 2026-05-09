import cv2
img = cv2.imread("meme4.jpg")
resized = cv2.resize(img, (300,300))    # dimesion = (width , height)

cv2.imshow("original", img)
cv2.imshow("resized", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()