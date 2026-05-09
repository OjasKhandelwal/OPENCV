import cv2

img = cv2.imread(input("enter file location: "))
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

ask = input("you want to show or save: ")
if ask == "show": 
    cv2.imshow("title",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif ask == "save":
    cv2.imwrite(input("enter file name: "),gray)
    print("file saved successfully")
else:
    print("invalid operation")
