import os
import shutil
import cv2
import numpy as np

os.environ['MPLCONFIGDIR'] = r'C:\Users\LENOVO\.gemini\antigravity\brain\b768dafa-3595-483f-97f3-a6502a8b1ef6\scratch'
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

repo_dir = r'C:\Users\LENOVO\.gemini\antigravity\scratch\image-enhancement-filters-opencv1'
assets_dir = os.path.join(repo_dir, 'assets')
os.makedirs(assets_dir, exist_ok=True)

src_img = r'C:\Users\LENOVO\.gemini\antigravity\brain\b768dafa-3595-483f-97f3-a6502a8b1ef6\.user_uploaded\media_1795491029890_1a2e6c3b.png'
dest_img = os.path.join(repo_dir, 'birds.jpeg')

shutil.copyfile(src_img, dest_img)
shutil.copyfile(src_img, os.path.join(assets_dir, 'birds.jpeg'))

# Step 1: Read and convert to RGB
image1 = cv2.imread(dest_img)
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

# 1. Averaging filter
kernel = np.ones((11, 11), np.float32) / 169
image3 = cv2.filter2D(image2, -1, kernel)

plt.figure(figsize=(9, 6))
plt.subplot(1, 2, 1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(image3)
plt.title("Average Filter Image")
plt.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_1_average.png'), bbox_inches='tight', dpi=150)
plt.close()

# 2. Weighted averaging
kernel1 = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
image_weighted = cv2.filter2D(image2, -1, kernel1)

fig, ax = plt.subplots(figsize=(5, 7.5))
ax.imshow(image_weighted)
ax.set_title("Weighted Average Filter Image")
ax.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_2_weighted.png'), bbox_inches='tight', dpi=150)
plt.close()

# 3. Gaussian filter
gaussian_blur = cv2.GaussianBlur(image2, (33, 33), 0, 0)

fig, ax = plt.subplots(figsize=(5, 7.5))
ax.imshow(gaussian_blur)
ax.set_title("Gaussian Blur")
ax.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_3_gaussian.png'), bbox_inches='tight', dpi=150)
plt.close()

# 4. Median filter
median = cv2.medianBlur(image2, 13)

fig, ax = plt.subplots(figsize=(5, 7.5))
ax.imshow(median)
ax.set_title("Median Blur")
ax.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_4_median.png'), bbox_inches='tight', dpi=150)
plt.close()

# 5. Laplacian kernel
kernel2 = np.array([[-1, -1, -1], [2, -2, 1], [2, 1, -1]])
image_lap_kernel = cv2.filter2D(image2, -1, kernel2)

fig, ax = plt.subplots(figsize=(5, 7.5))
ax.imshow(image_lap_kernel)
ax.set_title("Laplacian Kernel")
ax.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_5_laplacian_kernel.png'), bbox_inches='tight', dpi=150)
plt.close()

# 6. Laplacian operator
laplacian = cv2.Laplacian(image2, cv2.CV_64F)

fig, ax = plt.subplots(figsize=(5, 7.5))
ax.imshow(laplacian)
ax.set_title("Laplacian Operator")
ax.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_6_laplacian_operator.png'), bbox_inches='tight', dpi=150)
plt.close()

print('All filter outputs generated successfully!')
