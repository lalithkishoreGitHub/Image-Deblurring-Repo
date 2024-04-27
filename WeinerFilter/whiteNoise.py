import cv2 as cv
import os
import random

image_path = '../lenna.jpeg'
if not os.path.exists(image_path):
    print("Image doesn't exist")
    exit()

image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)


def addWhiteNoise(img):
    row, col = img.shape
    # add white noise
    number_of_pixels = random.randint(1, (row * col))
    for i in range(number_of_pixels):
        x_cord = random.randint(0, row - 1)
        y_cord = random.randint(0, col - 1)
        img[x_cord][y_cord] = 255

    return img


noised_image = addWhiteNoise(image)
cv.imwrite('white_noised_image.jpeg', noised_image)
