import cv2
img = cv2.imread("meme4.jpg")
pt1 = (5,100)
pt2 = (200,500)
color1 = (255,0,0) #(b,g,r)
color2 = (0,255,0)
color3 = (0,0,255)
color4 = (0,255,255)
radius = 50
center = (150,150)
text = "20 20 20 20 vision"
org = (50,300)

ln = cv2.line(img, pt1,pt2,color1,4)    #line(img, point1, point2, color, thickness)
rect = cv2.rectangle(img, pt1,pt2,color2,4) 
circ = cv2.circle(img, center, radius, color3, 4)   #circle(img, center, radius, color, thickness)

txt = cv2.putText(img, text, org, cv2.FONT_HERSHEY_SIMPLEX, 1.2, color4, 4)

cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()