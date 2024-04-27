import cv2 as cv
import os

image_path = '../GaussianFilter/speckled_image.jpg'

if not os.path.exists(image_path):
    print("Image not found")
    exit()

noised_image = cv.imread(image_path)
if noised_image is None:
    print("No image")
    exit()

denoised_image = cv.GaussianBlur(noised_image, (5, 5), 0)
cv.imwrite('speckle_removed.jpg', denoised_image)

