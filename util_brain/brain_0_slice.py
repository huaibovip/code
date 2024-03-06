import os
import multiprocessing as mp

import cv2
import numpy as np
import nibabel as nib

from brain_config import (
    T1, T2, T1GD, FLAIR, MP,
    IMG_CLIP,
    SAVE_IMG_PNG,
    SRC_ROOT,
    SLICE_ROOT,
)


def random_scale_factor(n_dim=3, mean=1, std=0.25):
    return np.random.normal(mean, std, n_dim)

 
def scale_image(image, scale_factor):
    """ scale NIFTI image with a scale factor
        https://blog.csdn.net/gefeng1209/article/details/90406454
    """
    from nilearn.image import new_img_like, resample_to_img
    
    scale_factor = np.asarray(scale_factor)
    new_affine = np.copy(image.affine)
    #修改原image的affine, 乘以放缩系数
    new_affine[:3, :3] = image.affine[:3, :3] * scale_factor
    #修改第４列的前３个值，保证放缩后的图像居中
    #1-scale_factor：缩小时，右移;放大时，左移
    new_affine[:, 3][:3] = image.affine[:, 3][:3] + (image.shape * np.diag(image.affine)[:3] * (1 - scale_factor)) / 2
    
    #返回创建新的nii image，data与原image相同，affine更新
    new_img = new_img_like(image, data=image.get_fdata(), affine=new_affine)
    return resample_to_img(new_img, image, interpolation="continuous")


def save_slice(path, im_slice, test=False):
    """ if test = False: save img to png;
        else save img to npy
    """
    if test:
        cv2.imwrite(path + '.png', im_slice * 255.0)
    else:
        np.save(path + '.npy', im_slice)


def slice_nib(name, modality, src_root, dst_root, clip=True, test=False, roi=[224, 224]):
    src_path = os.path.join(src_root, name, name + '_' + modality + '.nii.gz')
    dst_path = os.path.join(dst_root, name, modality)
    os.makedirs(dst_path, exist_ok=True)
    img = nib.load(src_path)  # (256, 256, 150)
    # scale = 1.1
    # img = scale_image(img, scale_factor=(scale, scale, scale))
    img_fdata = img.get_fdata(dtype=np.float32)
    img_fdata = np.rot90(m=img_fdata, k=-1, axes=(0, 1))
    img_fdata = np.flip(m=img_fdata, axis=1)
    
    print(img_fdata.dtype, end=' ')
    print(img_fdata.shape, end=' ')
    # print(img_fdata.min(), img_fdata.max(), end=' ')
    print(src_path, end=' ')
    
    if clip:
        print('clip', end=' ')
        maxv = np.percentile(img_fdata, 99.99)
        img_fdata = np.clip(img_fdata, a_min=0, a_max=maxv)
    else:
        print('no_clip', end=' ')
        maxv = np.max(img_fdata)
    
    img_fdata = img_fdata / maxv

    count_num = 0
    for i in range(img_fdata.shape[-1]):
        img_slice = img_fdata[:, :, i]
        if np.all(img_slice == 0):
            continue
        if np.count_nonzero(img_slice) < img_slice.size * 0.05:
            continue
        save_slice(os.path.join(dst_path, name + '_' + modality + '_{}'.format(i + 1)), img_slice, test=test)
        count_num += 1
    print(count_num)


def main(src_root, dst_root, modality, func, clip=True, test=False):
    fnames = os.listdir(src_root)
    print(f'subject count: {len(fnames)}')
    if MP:
        print(f'[cpu count] {mp.cpu_count()}')
        pool = mp.Pool(mp.cpu_count())
    for name in fnames:
        if MP:
            pool.apply_async(func, args=(name, modality, src_root, dst_root, clip, test))        
        else:
            func(name, modality, src_root, dst_root, clip, test)
    if MP:
        pool.close()
        pool.join()


if __name__ == '__main__':
    flag = 'png' if SAVE_IMG_PNG else 'npy'
    dir = flag + '_clip_slice' if IMG_CLIP else flag + '_noclip_slice'
    dst = os.path.join(SLICE_ROOT, dir)

    if SAVE_IMG_PNG:
        main(SRC_ROOT, dst, modality=T1GD, func=slice_nib, clip=IMG_CLIP, test=SAVE_IMG_PNG)
    else:
        for m in [T1, T1GD, T2, FLAIR]:
            main(SRC_ROOT, dst, modality=m, func=slice_nib, clip=IMG_CLIP, test=SAVE_IMG_PNG)
    