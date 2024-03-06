import os
import nibabel as nib
import pickle
import numpy as np


root = "/public/home/hb/datasets/i2i/IXI_data"

val_root = os.path.join(root, "Train")
niftit_root = os.path.join(root, "Niftit", "Train")
os.makedirs(niftit_root, exist_ok=True)
affine = np.eye(4)


def pkload(fname):
    with open(fname, "rb") as f:
        return pickle.load(f)


def save_volfile(array, filename, affine=None):
    """
    Saves an array to nii, nii.gz, or npz format.

    Parameters:
        array: The array to save.
        filename: Filename to save to.
        affine: Affine vox-to-ras matrix. Saves LIA matrix if None (default).
    """
    if filename.endswith(('.nii', '.nii.gz')):
        import nibabel as nib
        if affine is None and array.ndim >= 3:
            # use LIA transform as default affine
            affine = np.array([[-1, 0, 0, 0],  # nopep8
                               [0, 0, 1, 0],  # nopep8
                               [0, -1, 0, 0],  # nopep8
                               [0, 0, 0, 1]], dtype=float)  # nopep8
            pcrs = np.append(np.array(array.shape[:3]) / 2, 1)
            affine[:3, 3] = -np.matmul(affine, pcrs)[:3]
        nib.save(nib.Nifti1Image(array, affine), filename)
    elif filename.endswith('.npz'):
        np.savez_compressed(filename, vol=array)
    else:
        raise ValueError('unknown filetype for %s' % filename)


affine = np.array([
    [-1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, -1, 0, 0],
    [0, 0, 0, 1]],
    dtype=np.int32
)

# for fname in os.listdir(val_root):
#     img, seg = pkload(os.path.join(val_root, fname))
#     print(img.dtype, img.shape)
#     new_img = nib.Nifti1Image(img, affine)
#     new_img_path = os.path.join(niftit_root, fname[:-4] + ".nii.gz")
#     print(new_img_path)
#     nib.save(new_img, new_img_path)


path = '/public/home/hb/datasets/i2i/IXI/outputs/reg_outputs/IXI-T1/IXI019-Guys-0702-T1.pkl'
img, seg = pkload(path)
new_img = nib.Nifti1Image(img, affine)
new_img_path = os.path.join(root, "Niftit", "t1.nii.gz")
# nib.save(new_img, new_img_path)
save_volfile(img, filename=new_img_path)

# img, seg = pkload(os.path.join(root, 'atlas.pkl'))
# new_img_path = os.path.join(root, "Niftit", "atlas.nii.gz")
# save_volfile(img, filename=new_img_path)
