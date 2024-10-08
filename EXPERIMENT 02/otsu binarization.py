import cv2
import numpy as np
from scipy.ndimage import gaussian_filter

image_path = 'EXPERIMENT 02/bellingam.jpg'
image = cv2.imread(image_path)


if len(image.shape) == 3:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
else:
    gray_image = image

hist, bin_edges = np.histogram(gray_image.flatten(), bins=256, range=[0, 256])


smoothed_hist = gaussian_filter(hist, sigma=1.0)

total_pixels = smoothed_hist.sum()
sum_total = np.dot(np.arange(256), smoothed_hist)
cumulative_sum = np.cumsum(smoothed_hist)

# Prevent division by zero by replacing zero values in cumulative_sum with a small number
cumulative_sum_nonzero = np.where(cumulative_sum == 0, 1, cumulative_sum)
cumulative_mean = np.cumsum(np.arange(256) * smoothed_hist) / cumulative_sum_nonzero

# Compute the global mean
global_mean = sum_total / total_pixels


max_variance = 0
best_threshold = 0


for t in range(256):
    if cumulative_sum[t] == 0 or cumulative_sum[-1] == cumulative_sum[t]:
        continue
    
    weight1 = cumulative_sum[t] / total_pixels
    weight2 = 1 - weight1

    mean1 = cumulative_mean[t]
    mean2 = (global_mean - weight1 * mean1) / weight2

    between_class_variance = weight1 * weight2 * (mean1 - mean2) ** 2
    if between_class_variance > max_variance:
        max_variance = between_class_variance
        best_threshold = t


binary_image = (gray_image > best_threshold).astype(np.uint8) * 255


cv2.imwrite('binary_image.png', binary_image)
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


print(f"Optimal Threshold Value: {best_threshold}")
print(f"Maximum Between-Class Variance: {max_variance}")


import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
plt.title("Original Histogram")
plt.bar(bin_edges[:-1], hist, width=1.0, color='gray')


plt.subplot(1, 2, 2)
plt.title("Smoothed Histogram")
plt.bar(bin_edges[:-1], smoothed_hist, width=1.0, color='gray')

plt.tight_layout()
plt.show()
