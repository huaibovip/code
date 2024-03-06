import os
import nibabel as nib
os.environ.setdefault('NEURITE_BACKEND', 'pytorch')
from neurite import plot


def plot_slices(vols):
    slices = []
    for vol in vols:
        h, w, d = vol.shape
        slices.append(vol[h//2, :, :])
        slices.append(vol[:, w//2, :])
        slices.append(vol[:, :, d//2])
    return plot.slices(slices, cmaps=None, grid=True, width=9, show=False)
