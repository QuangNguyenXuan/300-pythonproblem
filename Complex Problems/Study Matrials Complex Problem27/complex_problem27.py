import cv2
img = cv2.imread("image.png")
blur_Image = cv2.blur(img,(100,10))
cv2.imshow("Title of real image", img)
cv2.imshow("Title image", blur_Image)
cv2.waitKey(0)
