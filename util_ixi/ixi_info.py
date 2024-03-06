import os
import numpy as np
import nibabel as nib
from ixi_config import T1, T2, PD, SRC_ROOT


def statistics(name, src_root):
    src_path = os.path.join(src_root, name)
    # mask_path = os.path.join(src_root, '..', 'mask', name[:6] + '_mask.nii.gz')
    modal = os.path.split(src_root)[-1]
    mask_path = os.path.join(src_root, '..', 'mask', modal, name[:-7] + '_mask.nii.gz')
    img = nib.load(src_path)  # (256, 256, 150)
    mask = nib.load(mask_path)
    # print(img.header)

    datatype = img.get_data_dtype()
    bitpix = img.header['bitpix']
    # pixdim = img.header['pixdim'][1:4]
    
    data = img.get_fdata(dtype=np.float32)
    mask = mask.get_fdata(dtype=np.float32)
    data[mask < 0.5] = 0

    max_val = np.max(data)
    min_val = np.min(data)
    max_val_99 = np.percentile(data, 99.99)
    mean_val = np.mean(data)
    shape = data.shape
    # data = np.rot90(m=data, k=1, axes=(0, 1))
    print(f'{name[:-7]}, ({shape[0]} {shape[1]} {shape[2]}), {datatype}, {bitpix}, {min_val}, {max_val}, {max_val_99}, {mean_val}')


def main(src_root):
    fnames = os.listdir(src_root)
    print('name, shape, datatype, bitpix, min_val, max_val, max_val_99, mean')
    for name in fnames:
        statistics(name, src_root)


if __name__ == '__main__':
    ROOT = r'G:\datasets\IXI\raw'
    for m in [T1, T2, PD]:
        # src_root = os.path.join(ROOT, 'src_80', m)
        src_root = os.path.join(ROOT, m)
        main(src_root)

    # import glob
    # ROOT = r'G:\datasets\IXI\raw\IXI-T2'
    # paths = glob.glob(os.path.join(ROOT, '*'))
    # print(paths[:5])
    # print(len(paths))
    