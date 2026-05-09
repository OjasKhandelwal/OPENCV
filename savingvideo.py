import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')    #codec- compression format,  fps-frames per second  


recorder = cv2.VideoWriter("my_video.avi",codec,20,(frame_width, frame_height))  #VideoWriter(filename, codec, fps, frame_size)

while True:

    success, image = camera.read()

    if not success:
        break

    recorder.write(image)

    cv2.imshow("Recording live", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
recorder.release()

cv2.destroyAllWindows()
 