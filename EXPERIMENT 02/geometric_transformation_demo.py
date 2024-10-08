import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('EXPERIMENT 02/bellingam.jpg',1)

rows, cols, ch = image.shape

pts1_affine = np.float32([[50, 50], [200, 50], [50, 200]])
pts2_affine = np.float32([[10, 100], [200, 50], [100, 250]])
M_affine = cv2.getAffineTransform(pts1_affine, pts2_affine)
affine_transformed = cv2.warpAffine(image, M_affine, (cols, rows))

pts1_perspective = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2_perspective = np.float32([[10, 100], [200, 50], [100, 250], [220, 220]])
M_perspective = cv2.getPerspectiveTransform(pts1_perspective, pts2_perspective)
perspective_transformed = cv2.warpPerspective(image, M_perspective, (cols, rows))

scale_x = 1.5
scale_y = 1.5
scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)

M_translation = np.float32([[1, 0, 100], [0, 1, 50]])
translated_image = cv2.warpAffine(image, M_translation, (cols, rows))

center = (cols // 2, rows // 2)
angle = 45
scale = 1.0
M = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, M, (cols, rows))


plt.subplot(321)
plt.imshow(image)
plt.title('ORIGINAL')

plt.subplot(322)
plt.imshow(affine_transformed)
plt.title('Affine Transformation')

plt.subplot(323)
plt.plot(perspective_transformed)
plt.title('Perspective Transformation')

plt.subplot(324)
plt.plot(scaled_image)
plt.title('Scaling')

plt.subplot(2325)
plt.plot(translated_image)
plt.title('Translation')

plt.subplot(326)
plt.plot(rotated_image)
plt.title('Rotation')

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
