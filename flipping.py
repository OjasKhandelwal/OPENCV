import cv2
img = cv2.imread("meme4.jpg")

f_hori = cv2.flip(img,1)
f_verti = cv2.flip(img,0)
f_both = cv2.flip(img,-1)

cv2.imshow("original", img)
cv2.imshow("horizontally", f_hori)
cv2.imshow("vertically", f_verti)
cv2.imshow("both", f_both)
cv2.waitKey(0)
cv2.destroyAllWindows()