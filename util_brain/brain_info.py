import os
import numpy as np
import nibabel as nib
from brain_config import T1, T1GD, T2, FLAIR, SRC_ROOT


def statistics(src_root, name, modality):
    src_path = os.path.join(src_root, name, name + '_' + modality + '.nii.gz')
    img = nib.load(src_path)  # (256, 256, 150)
    # print(img.header)

    datatype = img.get_data_dtype()
    bitpix = img.header['bitpix']
    # pixdim = img.header['pixdim'][1:4]
    
    data = img.get_fdata(dtype=np.float32)

    max_val = np.max(data)
    min_val = np.min(data)
    max_val_99 = np.percentile(data, 99.99)
    mean_val = np.mean(data)
    shape = data.shape
    print(f'{name}\t{modality}\t{shape}\t{datatype}\t{bitpix}\t{min_val}\t{max_val}\t{max_val_99}\t{mean_val}')


def main(src_root, modality):
    fnames = os.listdir(src_root)
    for name in fnames:
        statistics(src_root, name, modality)


if __name__ == '__main__':
    ROOT = r'G:/datasets/IXI/dataset/trilinear/Guys'
    print('name\tmodality\tshape\tdatatype\tbitpix\tmin_val\tmax_val\tmax_val_99\tmean')
    for m in [T1, T1GD, T2, FLAIR]:
        main(SRC_ROOT, m)
