import cv2
img = cv2.imread("meme4.jpg")


blurred = cv2.medianBlur(img, 7)                    #medianBlur(image, kernel_size)
cv2.imshow("original", img)
cv2.imshow("mb", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()