import cv2

img = cv2.imread("meme4.jpg")

if img is not None:
    h,w,c = img.shape
    print(f"Image loaded!!!! \nheight: {h} \nwidth: {w} \nchannels: {c}")
else:
    print("could not load.")