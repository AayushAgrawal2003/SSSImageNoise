import cv2
import numpy as np

image = cv2.imread('test.jpeg' , cv2.IMREAD_GRAYSCALE)

# Create a noise mask with varying standard deviation
noise_mask = np.random.uniform(0, 1, image.shape[:2])  # Adjust the range as needed

# Scale the noise mask to control the level of noise
max_std_dev =  0.04

# Add Gaussian noise with varying standard deviation to the image
noisy_image = image * ( 1 + np.random.normal(0, max_std_dev, image.shape))

noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)


# Display the noisy image
cv2.imshow("Noisy Image", noisy_image)
cv2.imshow("Orignal",image)
cv2.waitKey(0)

# Save the noisy image
# cv2.imwrite('noisy_image.jpg', noisy_image)
