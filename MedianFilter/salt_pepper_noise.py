import random
import cv2
import os


def add_noise(img):
    # Getting the dimensions of the image
    row, col = img.shape

    # Randomly pick some pixels in the
    # image for coloring them white
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # Color that pixel to white
        img[y_coord][x_coord] = 255

    # Randomly pick some pixels in
    # the image for coloring them black
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # Color that pixel to black
        img[y_coord][x_coord] = 0

    return img


# Check if the image file exists
image_path = '../photo.jpg'
if not os.path.exists(image_path):
    print(f"Error: Image file '{image_path}' not found.")
    exit()

# Reading the color image in grayscale image
img1 = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img1 is None:
    print("Error: Failed to load image.")
    exit()

# adding more noise to the image and storing it
for i in range(0, 400):
    result_img = add_noise(img1)
cv2.imwrite('salt_and_pepper_lal.jpg', result_img)

print("Salt-and-pepper noise added successfully.")
