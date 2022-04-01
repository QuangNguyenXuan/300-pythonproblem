import cv2
img = cv2.imread("image.png")
h = img.shape[0] # height
w = img.shape[1] # width 
print(h)
print(w)
print(str(w) +" x "+str(h))