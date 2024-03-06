import torch
import numpy as np
from torchvision import transforms
from matplotlib import pyplot as plt


size = (256, 256)
trans = transforms.Compose([
    transforms.Resize(size=size),
])


path = r'G:/datasets/Pelvis/Gold-Atlas/data/npy_dst/2_04_P/2_04_P_18.npy'
data = np.load(path)
h, w = data.shape
print(data.shape)

im1 = data[:, :w // 2]
im2 = data[:, w // 2:]

ims = np.stack([im1, im2])
ims = torch.from_numpy(ims)
ims = trans(ims)

print(ims.shape)
plt.subplot(1, 2, 1)
plt.imshow(ims[0], cmap='gray')
plt.subplot(1, 2, 2)
plt.imshow(ims[1], cmap='gray')
plt.show()
