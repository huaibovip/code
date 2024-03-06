import pickle
import numpy as np


def pkload(path):
    with open(path, "rb") as f:
        return pickle.load(f)


def pkdump(data, path):
    with open(path, "wb") as f:
        pickle.dump(data, f)


def save_volfile(array, filename, affine=None, header=None):
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
        nib.save(nib.Nifti1Image(array, affine, header), filename)
    elif filename.endswith('.npz'):
        np.savez_compressed(filename, vol=array)
    else:
        raise ValueError('unknown filetype for %s' % filename)
