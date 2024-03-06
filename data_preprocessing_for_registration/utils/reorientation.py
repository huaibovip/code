import numpy as np
import nibabel as nib


def _compute_orientation(init_axcodes, final_axcodes):
    """
    A thin wrapper around ``nib.orientations.ornt_transform``

    :param init_axcodes: Initial orientation codes
    :param final_axcodes: Target orientation codes
    :return: orientations array, start_ornt, end_ornt
    """
    ornt_init = nib.orientations.axcodes2ornt(init_axcodes)
    ornt_fin = nib.orientations.axcodes2ornt(final_axcodes)

    ornt_transf = nib.orientations.ornt_transform(ornt_init, ornt_fin)
    
    return ornt_transf, ornt_init, ornt_fin


def do_reorientation(data_array, init_axcodes, final_axcodes):
    """
    source: https://niftynet.readthedocs.io/en/dev/_modules/niftynet/io/misc_io.html#do_reorientation
    Performs the reorientation (changing order of axes)

    :param data_array: 3D Array to reorient
    :param init_axcodes: Initial orientation
    :param final_axcodes: Target orientation
    :return data_reoriented: New data array in its reoriented form
    """
    ornt_transf, ornt_init, ornt_fin = _compute_orientation(init_axcodes, final_axcodes)
    if np.array_equal(ornt_init, ornt_fin):
        return data_array

    return nib.orientations.apply_orientation(data_array, ornt_transf)


if __name__ == '__main__':
    # I test the code by the following simple demo, and it works.

    # src_path = r'/public/home/hb/softwares/tool/data_preprocessing/atlases/mni_icbm152_nlin_asym_09a/mni_icbm152_t1_tal_nlin_asym_09a.nii'
    # dst_path = r'/public/home/hb/softwares/tool/data_preprocessing/atlases/rsp/mni_icbm152_nlin_asym_09a/mni_icbm152_t1_tal_nlin_asym_09a.nii'
    src_path = r'/public/home/hb/softwares/tool/data_preprocessing/atlases/mni_icbm152_lpi/t1.nii.gz'
    dst_path = r'/public/home/hb/softwares/tool/data_preprocessing/atlases/mni_icbm152_lpi/t1_lpi.nii.gz'

    src_nii = nib.load(src_path)
    src_data = src_nii.get_fdata() # shape = (512, 512, 123)
    src_axcodes = tuple(nib.aff2axcodes(src_nii.affine)) # ('R', 'A', 'S')
    affine = src_nii.affine

    dst_affine = np.array([
        [-1,  0, 0, affine[0,3]],
        [ 0,  0, 1, affine[1,3]],
        [ 0, -1, 0, affine[2,3]],
        [ 0,  0, 0, 1],
    ])
    dst_axcodes = tuple(nib.aff2axcodes(dst_affine))
    print(f'{src_path} -> {dst_axcodes}')

    new_data = do_reorientation(src_data, src_axcodes, dst_axcodes)
    new_img = nib.Nifti1Image(new_data, dst_affine)
    nib.save(new_img, dst_path)
