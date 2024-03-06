import os
import numpy as np
from matplotlib import pyplot as plt
from brain_config import T1, T1GD, T2, FLAIR


path = r'G:\datasets\Brain\dataset\dst\verio\npy_clip_dst\brain_t1_t1gd_t2_flair\train\UPENN-GBM-00285_11\55.npy'

imgs = np.load(path)
print(imgs.shape, imgs.dtype)

modalities = [T1, T1GD, T2, FLAIR]
for i in range(imgs.shape[0]):
    plt.subplot(1, imgs.shape[0], i + 1)
    plt.title(modalities[i])
    plt.xticks([])
    plt.yticks([])
    plt.imshow(imgs[i], cmap='gray')
plt.show()
