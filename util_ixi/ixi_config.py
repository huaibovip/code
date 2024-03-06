import os


T1 = 'IXI-T1'
T2 = 'IXI-T2'
PD = 'IXI-PD'

MP = True
ROOT = r'G:/datasets/IXI'

# untar
TAR_ROOT = os.path.join(ROOT, 'raw')
SRC_ROOT = os.path.join(ROOT, 'src')
SRC_TMP_ROOT = os.path.join(SRC_ROOT, 'tmps')

# flirt
REF_MODALITY = T2
MASK_ROOT = os.path.join(SRC_ROOT, 'mask')
INTERPOLATION = 'trilinear' # 'spline'

# slice
IMG_CLIP = True
SAVE_IMG_PNG = False
SLICE_ROOT = os.path.join(ROOT, 'dataset_tmp', 'slice')

# dataset
DST_ROOT = os.path.join(ROOT, 'dataset_tmp', 'dst')
DATASET_TYPE = 'npy' # hdf5, png
