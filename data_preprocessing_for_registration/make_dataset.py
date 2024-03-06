import os
import glob
import nibabel as nib
import numpy as np
from utils.reorientation import do_reorientation
from utils.io import pkload, pkdump


def normalize_intensity(image, normalization_type='01'):
    if normalization_type == '01':
        return (image - image.min()) / (image.max() - image.min())

    elif normalization_type == '0mean':
        return (image - image.mean()) / image.std()

    else:
        raise ValueError("Unrecognized Intensity Normalization type.")


if __name__ == '__main__':
    src_affine = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])
    src_axcodes = tuple(nib.aff2axcodes(src_affine))

    dst_affine = np.array([
        [-1,  0, 0, 0],
        [ 0,  0, 1, 0],
        [ 0, -1, 0, 0],
        [ 0,  0, 0, 1],
    ])
    dst_axcodes = tuple(nib.aff2axcodes(dst_affine))

    data_root = '/public/home/hb/datasets/i2i/IXI/outputs'
    src_img_root = os.path.join(data_root, 'n4_outputs')
    src_seg_root = os.path.join(data_root, 'seg_outputs')
    dst_root = os.path.join(data_root, 'final_outputs')
    modalities = ["T1", "T2", "PD"]

    for m in modalities:
        save_dir = os.path.join(dst_root, "IXI-" + m)
        os.makedirs(save_dir, exist_ok=True)
        for img_path in glob.glob(os.path.join(src_img_root, "IXI-" + m, "*")):
            seg_path = img_path.replace('n4_outputs', 'seg_outputs')
            seg_path = os.path.join(os.path.dirname(seg_path), os.path.basename(seg_path)[:-7] + '_seg.nii.gz')
            dst_path = os.path.join(save_dir, os.path.basename(img_path)[:-7] + '.pkl')
            img = nib.load(img_path).get_fdata().astype('float32')
            seg = nib.load(seg_path).get_fdata().astype('int16')
            img = do_reorientation(img, src_axcodes, dst_axcodes)
            seg = do_reorientation(seg, src_axcodes, dst_axcodes)
            img = normalize_intensity(img)
            pkdump(data=(img, seg), path=dst_path)

    path = os.path.join(dst_root, "IXI-T1", "IXI002-Guys-0828-T1.pkl")
    ret = pkload(path)
    print(ret[0].shape, ret[0].dtype)
    print(ret[1].shape, ret[1].dtype)
