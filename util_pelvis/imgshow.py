import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

path = r'G:/datasets/Pelvis/Gold-Atlas/data/npy_dst/train/2_04_P/2_04_P_18.npy'
# path = r'G:/datasets/Pelvis/Gold-Atlas/data/npy_dst/train/2_09_P/2_09_P_29.npy'

s = np.load(path)
print(s.shape)

h, w = s.shape
mr = s[:, :w // 2]
ct = s[:, w // 2:]

# plt.subplot(1, 2, 1)
# plt.imshow(mr, cmap='gray')
# plt.title('MR')

# plt.subplot(1, 2, 2)
# plt.imshow(ct, cmap='gray')
# plt.title('CT')

# plt.show()
Image.fromarray((mr * 255).astype(np.uint8)).save('pelvis-MR.png')
Image.fromarray((ct * 255).astype(np.uint8)).save('pelvis-CT.png')
