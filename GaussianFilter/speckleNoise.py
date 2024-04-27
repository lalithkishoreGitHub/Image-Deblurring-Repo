import numpy as np
import cv2 as cv
import os


def speckleNoise(img):
    row = img.shape[0]
    col = img.shape[1]
    ch = img.shape[2]
    # Generate speckle noise with mean 1 and standard deviation 0.1
    speckle = np.random.normal(1, 0.1, (row, col, ch))
    noisy = img * speckle
    return noisy


# image path
image_path = '../photo.jpg'

if not os.path.exists(image_path):
    print("Image not found")
    exit()

image = cv.imread(image_path)
if image is None:
    print("No image")
    exit()

noisy_image = speckleNoise(image)
cv.imwrite('speckled_image.jpg',noisy_image)

