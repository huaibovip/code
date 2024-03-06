import os
import time
import shutil
import multiprocessing as mp

import ants

from ixi_config import (
    T1, T2, PD, MP,
    REF_MODALITY,
    INTERPOLATION,
    SRC_TMP_ROOT,
    SRC_ROOT
)


ignore_names = [
    'IXI116-Guys-0739',
    'IXI182-Guys-0792',
    'IXI309-IOP-0897',
    'IXI500-Guys-1017',
    'IXI014-HH-1236',
    'IXI630-Guys-1108',
    'IXI593-Guys-1109',
    'IXI533-Guys-1066',
    'IXI580-IOP-1157',
]

def move_files(modalities):
    for m in modalities:
        src = os.path.join(SRC_TMP_ROOT, m)
        dst = os.path.join(SRC_ROOT, m)
        # shutil.mv(src, dst)
        shutil.copytree(src, dst)


def ants_func(idx, in_path, ref_path, out_path, mat_path=None, interpolation='linear', method='Affine'):
    """
    interpolation: linear, nearestNeighbor
    """
    start = time.time()
    # ants图片的读取
    m_img = ants.image_read(in_path)
    f_img = ants.image_read(ref_path)
    # f_label = ants.image_read("./data/f_label.nii.gz")
    # m_label = ants.image_read("./data/m_label.nii.gz")

    '''
    ants.registration()函数的返回值是一个字典：
        warpedmovout: 配准到fixed图像后的moving图像 
        warpedfixout: 配准到moving图像后的fixed图像 
        fwdtransforms: 从moving到fixed的形变场 
        invtransforms: 从fixed到moving的形变场

    type_of_transform参数的取值可以为:
        Rigid: 刚体
        Affine: 仿射配准，即刚体+缩放
        ElasticSyN: 仿射配准+可变形配准, 以MI为优化准则, 以elastic为正则项
        SyN: 仿射配准+可变形配准, 以MI为优化准则
        SyNCC: 仿射配准+可变形配准, 以CC为优化准则

    以下为其他不常用的函数：
        ANTsTransform.apply_to_image(image, reference=None, interpolation='linear')
        ants.read_transform(filename, dimension=2, precision='float')
        # transform的格式是".mat"
        ants.write_transform(transform, filename)
        # field是ANTsImage类型
        ants.transform_from_displacement_field(field)
    '''
    
    interpolations = {
        'linear': 'linear',
        'spline': 'bSpline',
        'nearest': 'nearestNeighbor',
    }
    
    # 图像配准
    mytx = ants.registration(fixed=f_img, moving=m_img, type_of_transform=method)
    # 将形变场作用于moving图像，得到配准后的图像，interpolator也可以选择"nearestNeighbor"等
    warped_img = ants.apply_transforms(fixed=f_img, moving=m_img, transformlist=mytx['fwdtransforms'], interpolator=interpolations[interpolation])
    # 对moving图像对应的label图进行配准
    # warped_label = ants.apply_transforms(fixed=f_img, moving=m_label, transformlist=mytx['fwdtransforms'], interpolator=interpolation)
    # 将配准后图像的direction/origin/spacing和原图保持一致
    warped_img.set_direction(f_img.direction)
    warped_img.set_origin(f_img.origin)
    warped_img.set_spacing(f_img.spacing)
    # warped_label.set_direction(f_img.direction)
    # warped_label.set_origin(f_img.origin)
    # warped_label.set_spacing(f_img.spacing)
    # 图像的保存
    ants.image_write(warped_img, out_path)
    if mat_path is not None:
        shutil.copy(mytx['fwdtransforms'][0], mat_path)
    # ants.image_write(warped_label, label_name)
    print(f'{idx + 1} time: {time.time() - start}  {in_path}  ->  {out_path}')


def main(root, out_root, in_modal, ref_modal, interpolation):
    in_names = os.listdir(os.path.join(root, in_modal))
    ref_names = os.listdir(os.path.join(root, ref_modal))
    fnames = in_names if len(in_names) < len(ref_names) else ref_names    
    print(f'subject count: {len(fnames)}')

    mat_root = os.path.join(out_root, 'mats')
    os.makedirs(os.path.join(out_root, in_modal), exist_ok=True)
    os.makedirs(os.path.join(mat_root, in_modal), exist_ok=True)

    if MP:
        print(f'[cpu count] {mp.cpu_count()}')
        pool = mp.Pool(mp.cpu_count())

    start = time.time()
    for i in range(len(fnames)):
        if fnames[i][:15] in ignore_names:
            continue
        in_name = fnames[i][:-16] + in_modal[-2:]
        ref_name = fnames[i][:-16] + ref_modal[-2:]
        in_path = os.path.join(root, in_modal, in_name + '_output.nii.gz')
        ref_path = os.path.join(root, ref_modal, ref_name + '_output.nii.gz')

        if os.path.isfile(in_path) and os.path.isfile(ref_path):
            out_path = os.path.join(out_root, in_modal, in_name + '.nii.gz')
            mat_path = os.path.join(mat_root, in_modal, in_name + '.mat')
            if MP:
                pool.apply_async(func=ants_func, args=(i, in_path, ref_path, out_path, mat_path, interpolation))
            else:
                ants_func(i, in_path, ref_path, out_path, mat_path, interpolation)
    if MP:
        pool.close()
        pool.join()
    print(f'time: {time.time() - start} done.')


if __name__ == '__main__':
    assert REF_MODALITY in [T1, T2, PD]
    print(f'processing data. reference modality: {REF_MODALITY}')
    
    if REF_MODALITY == T1:
        for (im, rm) in [(T2, T1), (PD, T1)]:
            main(root=SRC_TMP_ROOT, out_root=SRC_ROOT, in_modal=im, ref_modal=rm, interpolation=INTERPOLATION)
        move_files([T1])
    elif REF_MODALITY == T2:
        for (im, rm) in [(T1, T2)]:
            main(root=SRC_TMP_ROOT, out_root=SRC_ROOT, in_modal=im, ref_modal=rm, interpolation=INTERPOLATION)
        # move_files([T2, PD])
    else:
        for (im, rm) in [(T1, PD)]:
            main(root=SRC_TMP_ROOT, out_root=SRC_ROOT, in_modal=im, ref_modal=rm, interpolation=INTERPOLATION)
        move_files([T2, PD])

    # shutil.rmtree(SRC_TMP_ROOT)
