import cv2 as cv
import os
from scipy.signal import wiener
image_path = '../WeinerFilter/white_noised_image.jpeg'
if not os.path.exists(image_path):
    print("Image doesn't exist")
    exit()

image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
denoised_image = wiener(image,(255,255))

cv.imwrite('denoised_image.jpeg', denoised_image)
