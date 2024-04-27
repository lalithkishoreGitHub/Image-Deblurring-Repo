import cv2
import random
import os

# Read the image file
image_path = '../photo.jpg'
if not os.path.exists(image_path):
    print(f"Error: Image file '{image_path}' not found.")
    exit()

# Read the image in grayscale
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Error: Failed to load image.")
    exit()


# Add salt-and-pepper noise
def add_noise(img):
    row, col = img.shape
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        img[y_coord][x_coord] = 255
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        img[y_coord][x_coord] = 0
    return img


# Add salt-and-pepper noise to the image
noisy_img = add_noise(img)

# Apply median filter to remove noise
denoised_img = cv2.medianBlur(noisy_img, 5)  # 5x5 median filter kernel size

# Save the denoised image
cv2.imwrite('denoised_lal.jpeg', denoised_img)

print("Denoising complete. Output saved as 'denoised_lal.jpeg'.")
