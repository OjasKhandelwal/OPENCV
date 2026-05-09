import cv2
img = cv2.imread("meme4.jpg")


blurred = cv2.GaussianBlur(img, (9, 9), 10) #GaussianBlur(image, (kernel_size_x, kernel_size_y), sigma)    kernelsize humesha odd number hota hai
                                                                                                      #sigma - kitna strong blur hona chahiye

cv2.imshow("original", img)
cv2.imshow("gb", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()