import os
import glob

from hd_bet.run import run_hd_bet


if __name__ == "__main__":
    """
    mri_fnames
        Can be either a single file name or an input folder. If file: must be
        nifti (.nii.gz) and can only be 3D. No support for 4d images, use fslsplit to
        split 4d sequences into 3d images. If folder: all files ending with .nii.gz
        within that folder will be brain extracted.

    output_fnames
        Can be either a filename or a folder. If it does not exist, the folder
        will be created

    mode
        can be either 'fast' or 'accurate'. Fast will
        use only one set of parameters whereas accurate will
        use the five sets of parameters that resulted from
        our cross-validation as an ensemble. Default: accurate

    device
        used to set on which device the prediction will run.
        Must be either int or str. Use int for GPU id or
        'cpu' to run on CPU. When using CPU you should
        consider disabling tta. Default for device is: 0
    tta
        whether to use test time data augmentation
        (mirroring). 1= True, 0=False. Disable this
        if you are using CPU to speed things up! Default: 1
    pp
        set to 0 to disabe postprocessing (remove all
        but the largest connected component in
        the prediction. Default: 1

    save_mask
        if set to 0 the segmentation " "mask will not be " "saved"

    overwrite_existing
        set this to 0 if you don't " "want to overwrite existing " "predictions

    bet
        set this to 0 if you don't want to save skull-stripped brain
    """

    dataset_root = "/public/home/hb/datasets/i2i/IXI"

    data_root = os.path.join(dataset_root, 'raw')
    save_root = os.path.join(dataset_root, 'outputs', 'bet_outputs2')
    modalities = ['T1', 'T2', 'PD']

    mode = "accurate"
    save_mask = True
    save_bet_img = True
    device = 3

    for m in modalities:
        save_dir = os.path.join(save_root, "IXI-" + m)
        os.makedirs(save_dir, exist_ok=True)
        for input_path in glob.glob(os.path.join(data_root, 'IXI-' + m, '*')):
            output_path = os.path.join(save_dir, os.path.basename(input_path))
            run_hd_bet(
                mri_fnames=input_path,
                output_fnames=output_path,
                mode=mode,
                device=device,
                postprocess=1,
                do_tta=1,
                keep_mask=save_mask,
                overwrite=False,
                bet=save_bet_img,
            )
