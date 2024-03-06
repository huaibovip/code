
import argparse
import os
from os.path import join as op_join
import cv2

import numpy as np
import nibabel as nib

WIN_CENTER = 0
WIN_WIDTH = 550


def winclip(img, wincenter, winwidth):
    """ dim (x y z)
    """
    min = (2 * wincenter - winwidth) / 2.0 + 0.5
    max = (2 * wincenter + winwidth) / 2.0 + 0.5
    dFactor = 255.0 / (max - min)

    rows, cols, depths = img.shape
    for z in range(depths):
        for i in np.arange(rows):
            for j in np.arange(cols):
                img[i, j, z] = (img[i, j, z] - min) * dFactor
    return img


def norm(img, minv=None, maxv=None):
    if minv is None or maxv is None:
        minv = img.min()
        maxv = img.max()
    img = (img - minv) / (maxv - minv)
    return img


def slice_nib(name, src_root):
    img_path = op_join(src_root, name + '.nii.gz')
    mask_path = op_join(src_root, 'mask.nii.gz')

    img = nib.load(img_path)  # (512, 512, 84)
    mask = nib.load(mask_path)
    img_arr = img.get_fdata(dtype=np.float32)
    mask_arr = mask.get_fdata(dtype=np.float32)

    if name.find('CT') != -1:
        # CT
        img_arr[mask_arr <= 0] = -1000
        # img_arr = winclip(img_arr, WIN_CENTER, WIN_WIDTH)
        # HU (-1000, 1400)
        img_arr = np.clip(img_arr, a_min=-1000, a_max=1400)
    else:
        # MR
        img_arr[mask_arr <= 0] = 0
        maxv = np.percentile(img_arr, 99.99)
        img_arr = np.clip(img_arr, a_min=0, a_max=maxv)
        # img_arr = img_arr / maxv

    img_arr = np.rot90(m=img_arr, k=3, axes=(0, 1))
    img_arr = np.flip(m=img_arr, axis=1)

    print(img_arr.dtype, end=' ')
    print(img_arr.shape, end=' ')
    # print(img_arr.min(), img_arr.max(), end=' ')
    print(img_path)
    return norm(img_arr)


def save_slice(path, im_slice, test=False):
    """ if test = False: save img to png;
        else save img to npy
    """
    if test:
        cv2.imwrite(path + '.png', im_slice * 255.0)
    else:
        # data range (0., 1.)
        np.save(path + '.npy', im_slice)


def main(root, test=False):
    sdir = 'png_dst' if test else 'npy_dst'
    for dir_name in os.listdir(op_join(root, 'src')):
        src_root = op_join(root, 'src', dir_name)
        dst_root = op_join(root, sdir, dir_name)
        t2_arr = slice_nib('MR_T2', src_root)
        ct_arr = slice_nib('CTtoMR', src_root)
        os.makedirs(dst_root, exist_ok=True)

        assert ct_arr.shape == t2_arr.shape
        for i in range(ct_arr.shape[-1]):
            t2_slice = t2_arr[:, :, i]
            ct_slice = ct_arr[:, :, i]
            im_slice = np.concatenate([t2_slice, ct_slice], 1)
            save_slice(op_join(dst_root, dir_name + f'_{i + 1}'), im_slice, test)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--test', action='store_true', help='')
    args = parser.parse_args()

    # root = r'/public/home/hb/datasets/'
    root = r'G:/datasets/Pelvis/Gold-Atlas/data'
    main(root, test=args.test)
