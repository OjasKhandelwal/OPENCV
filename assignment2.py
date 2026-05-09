import cv2

img = cv2.imread(input("enter file location: "))
if img is None:
    print("Image not found")
    exit()
option = input("what you want to annotate on the image: ")
color1 = (255,0,0)
color2 = (0,255,0)
color3 = (0,0,255)
color4 = (255,255,0)
thickness = 4
radius = 50
center = (150,150)
text = "20 20 20 20 vision"
org = (50,300)

if option=="line":
    line = cv2.line(img,(20,100),(157,250),color1,thickness)
    cv2.imshow("line", line)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif option=="rectangle":
    rect = cv2.rectangle(img,(75,200),(120,250),color2,thickness)
    cv2.imshow("rectangle", rect)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif option=="circle":
    circ = cv2.circle(img,center,radius,color3,thickness)
    cv2.imshow("circle", circ)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif option=="text":
    txt = cv2.putText(img, text, org, cv2.FONT_HERSHEY_SIMPLEX, 1.2, color4, 4)
    cv2.imshow("text", txt)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else: 
    print("invalid operation")
