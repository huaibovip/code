import os
import glob
import nibabel as nib
import numpy as np
# os.environ.setdefault('NEURITE_BACKEND', 'pytorch')
# from neurite import plot
# from matplotlib import pyplot as plt


if __name__ == '__main__':
    dataset_root = "/public/home/hb/datasets/i2i/IXI/outputs"
    data_root = os.path.join(dataset_root, "reg_outputs")
    dst_root = os.path.join(dataset_root, "crop_outputs")
    modalities = ["T1", "T2", "PD"]

    for m in modalities:
        save_dir = os.path.join(dst_root, "IXI-" + m)
        save_mask_dir = os.path.join(dst_root, "maskes", "IXI-" + m)
        os.makedirs(save_dir, exist_ok=True)
        os.makedirs(save_mask_dir, exist_ok=True)
        for input_path in glob.glob(os.path.join(data_root, "IXI-" + m, "*")):
            print(input_path)
            img = nib.load(input_path)
            data = img.get_fdata().astype('float32')
            data = np.pad(data, ((0,0), (0,0), (15,0)))
            print(data.shape)
            data = data[17:-20, 4:-5, :-12]
            print(data.shape)
            ##########################
            # plot.slices([data[i] for i in range(data.shape[0])], grid=True, show=False)
            # plt.savefig('data1.png')
            # plot.slices([data[:, i] for i in range(data.shape[1])], grid=True, show=False)
            # plt.savefig('data2.png')
            # plot.slices([data[:, :, i] for i in range(data.shape[2])], grid=True, show=False)
            # plt.savefig('data3.png')  
            ##########################
            mask = data.copy()
            mask[mask > 0.] = 1
            mask[mask <= 0.] = 0
            mask = mask.astype('uint8')
            # save
            affine = np.eye(4)
            new_img = nib.Nifti1Image(data, affine)
            mask_img = nib.Nifti1Image(mask, affine)
            input_name = os.path.basename(input_path)
            img_path = os.path.join(save_dir, input_name)
            mask_path = os.path.join(save_mask_dir, input_name[:-7] + '_mask.nii.gz')
            nib.save(new_img, img_path)
            nib.save(mask_img, mask_path)
