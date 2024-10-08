import cv2
import matplotlib.pyplot as plt

# Read two images as grayscale images
img1 = cv2.imread('EXPERIMENT 03//shape1.png', 0)
img2 = cv2.imread('EXPERIMENT 03//shape2.jpg', 0)

# Apply thresholding on the images to convert to binary images
ret, thresh1 = cv2.threshold(img1, 127, 255, 0)
ret, thresh2 = cv2.threshold(img2, 127, 255, 0)

# Find the contours in the binary images
contours1, hierarchy1 = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours2, hierarchy2 = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Print the number of shapes detected
print("Number of Shapes detected in Image 1:", len(contours1))
print("Number of Shapes detected in Image 2:", len(contours2))

# Create a figure to display the results
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Display the original images
axs[0, 0].imshow(img1, cmap='gray')
axs[0, 0].set_title('Image 1')
axs[0, 0].axis('off')
axs[0, 1].imshow(img2, cmap='gray')
axs[0, 1].set_title('Image 2')
axs[0, 1].axis('off')

# Draw contours on the images
contour_img1 = cv2.drawContours(img1.copy(), contours1, -1, (0, 255, 0), 1)
contour_img2 = cv2.drawContours(img2.copy(), contours2, -1, (0, 255, 0), 1)

axs[1, 0].imshow(contour_img1, cmap='gray')
axs[1, 0].set_title('Contours on Image 1')
axs[1, 0].axis('off')
axs[1, 1].imshow(contour_img2, cmap='gray')
axs[1, 1].set_title('Contours on Image 2')
axs[1, 1].axis('off')

plt.tight_layout()
plt.show()

# Check if contours are available and then compute match scores
if len(contours1) > 0 and len(contours2) > 0:
    cnt1 = contours1[0]
    cnt2 = contours2[0]
    
    # Compute the match scores
    ret11 = cv2.matchShapes(cnt1, cnt1, 1, 0.0)
    ret22 = cv2.matchShapes(cnt2, cnt2, 1, 0.0)
    ret12 = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
    
    # Print the matching scores
    print("Matching Image 1 with itself:", ret11)
    print("Matching Image 2 with itself:", ret22)
    print("Matching Image 1 with Image 2:", ret12)
else:
    print("No contours found in one or both images.")
