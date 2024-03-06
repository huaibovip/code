import os
import glob
import nibabel as nib
import numpy as np
os.environ.setdefault('NEURITE_BACKEND', 'pytorch')
from neurite import plot
from matplotlib import pyplot as plt


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


affine = np.eye(4)
data_root = '/public/home/hb/softwares/tool/data_preprocessing/atlases/mni_icbm152_nlin_asym_09a'
dst_root = '/public/home/hb/softwares/tool/data_preprocessing/atlases/mni_icbm152_nlin_asym_09a/new'

os.makedirs(dst_root, exist_ok=True)
for input_path in glob.glob(os.path.join(data_root, "*.nii*")):
    print(input_path)
    img: nib.Nifti1Image = nib.load(input_path)
    print(img.header['datatype'])
    data = img.get_fdata().astype('int32')
    data = np.pad(data, ((0,0), (0,0), (15,0)))
    print(data.shape)
    data = data[18:-19, 4:-5, :-12]
    print(data.shape)
    plot.slices([data[i] for i in range(data.shape[0])], grid=True, show=False)
    plt.savefig('data1.png')
    plot.slices([data[:, i] for i in range(data.shape[1])], grid=True, show=False)
    plt.savefig('data2.png')
    plot.slices([data[:, :, i] for i in range(data.shape[2])], grid=True, show=False)
    plt.savefig('data3.png')
    # save
    input_name = os.path.basename(input_path)
    img_path = os.path.join(dst_root, input_name)
    new_img = nib.Nifti1Image(data, affine, img.header)
    nib.save(new_img, img_path)
    # save_volfile(data, img_path, affine, img.header)
