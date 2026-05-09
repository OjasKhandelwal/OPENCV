import cv2


img = cv2.imread("meme4.jpg")   #loads image

if img is None:
    print("error!!! img not found")

else:
    print("img loaded!!!!")

cv2.imshow("title", img)   #displays image
cv2.imwrite("output.jpg",img)   #saves image
cv2.waitKey(0)            #Without this line, the image window closes immediately because the program finishes execution.
cv2.destroyAllWindows()      #Close all OpenCV windows properly



