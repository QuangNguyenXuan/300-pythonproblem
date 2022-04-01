from PIL import Image
img = Image.open("image.png")
angle = int(input("Enter a angle"))
rotated_img = img.rotate(angle)
rotated_img.show()