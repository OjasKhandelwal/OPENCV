import cv2

cap = cv2.VideoCapture(0)     #VideoCapture(source)   #source=0 -> humare computer ka webcam     source=1-> external webcam

while True:
    ret,frame= cap.read()   #ret-true/false   frame=image
    if not ret:
        print("could not read frame")
        break

    cv2.imshow("webcam" , frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting....")
        break


cap.release() #stop the capturing
cv2.destroyAllWindows()