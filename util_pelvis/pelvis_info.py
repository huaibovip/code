
import os
from os.path import join as op_join

import numpy as np
import pydicom
import SimpleITK as sitk


def get_name(dcm):
    description = dcm.SeriesDescription.lower()
    modality = dcm.Modality.lower()

    name = None
    if modality == 'mr':
        if description.find('t1') != -1:
            name = 'MR_T1'
        elif description.find('t2') != -1:
            name = 'MR_T2'
        else:
            raise TypeError('Invaid MR type')
    elif modality == 'ct':
        if description.find('cttomr') != -1:
            name = 'CTtoMR'
        else:
            name = 'CT'
    else:
        raise TypeError('Invaid modality type')
    
    return name


def load_slices(num, dcm_dir):
    """
    Load dcm like images
    Return img array and [z,y,x]-ordered origin and spacing
    """
    # 获取该文件下的所有序列ID，每个序列对应一个ID， 返回的series_IDs为一个列表
    series_IDs = sitk.ImageSeriesReader.GetGDCMSeriesIDs(dcm_dir)

    msg = ''
    for id in series_IDs:
        msg += f'series ids: {id} '
    # print(msg)

    # 通过ID获取该ID对应的序列所有切片的完整路径， series_IDs[0]代表的是第一个序列的ID
    # 如果不添加series_IDs[0]这个参数，则默认获取第一个序列的所有切片路径
    for i in range(len(series_IDs)):
        series_file_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(dcm_dir, series_IDs[i])
        dcm = pydicom.dcmread(series_file_names[0])
        # print(dcm)
        name = get_name(dcm)
        if name == 'CT':
            continue

        series_reader = sitk.ImageSeriesReader()
        series_reader.SetFileNames(series_file_names)
        itkimage: sitk.Image = series_reader.Execute()

        numpyImage = sitk.GetArrayFromImage(itkimage)
        minv = np.min(numpyImage)
        maxv = np.max(numpyImage)
        minv_1 = np.percentile(numpyImage, 1)
        maxv_99 = np.percentile(numpyImage, 99)
        mean = np.mean(numpyImage)

        numpyOrigin = np.array(list(reversed(itkimage.GetOrigin())))
        numpySpacing = np.array(list(reversed(itkimage.GetSpacing())))
        numpySize = np.array(list(reversed(itkimage.GetSize())))
        print(f'{num}, {len(series_IDs)}, {dcm.PatientID}, {name}, {numpySize}, {numpySpacing}, {numpyOrigin}, {minv}, {maxv}, {minv_1}, {maxv_99}, {mean}')


def load_series(idx, nii_dir):
    """
    Load mhd, nii like images
    Return img array and [z,y,x]-ordered origin and spacing
    """
    dir_name = os.path.split(nii_dir)[-1]

    # t1_path = op_join(nii_dir, 'MR_T1.nii.gz')
    t2_path = op_join(nii_dir, 'MR_T2.nii.gz')
    ct_path = op_join(nii_dir, 'CTtoMR.nii.gz')
    mask_path = op_join(nii_dir, 'mask.nii.gz')

    # t1_img = sitk.ReadImage(t1_path)
    t2_img = sitk.ReadImage(t2_path)
    ct_img = sitk.ReadImage(ct_path)
    mask_img = sitk.ReadImage(mask_path)

    # t1_arr = sitk.GetArrayFromImage(t1_img)
    t2_arr = sitk.GetArrayFromImage(t2_img)
    ct_arr = sitk.GetArrayFromImage(ct_img)
    mask_arr = sitk.GetArrayFromImage(mask_img)

    t2_arr[mask_arr <= 0] = 0
    ct_arr[mask_arr <= 0] = -1000

    minv = np.min(ct_arr)
    maxv = np.max(ct_arr)
    minv_1 = np.percentile(ct_arr, 1)
    maxv_99 = np.percentile(ct_arr, 99.97)
    mean = np.mean(ct_arr)
    origin = np.array(list(reversed(ct_img.GetOrigin())))
    spacing = np.array(list(reversed(ct_img.GetSpacing())))
    size = np.array(list(reversed(ct_img.GetSize())))
    print(f'{idx}, {dir_name}, CT, {size}, {spacing}, {origin}, {minv}, {maxv}, {minv_1}, {maxv_99}, {mean}')

    minv = np.min(t2_arr)
    maxv = np.max(t2_arr)
    minv_1 = np.percentile(t2_arr, 1)
    maxv_99 = np.percentile(t2_arr, 99.97)
    mean = np.mean(t2_arr)
    origin = np.array(list(reversed(t2_img.GetOrigin())))
    spacing = np.array(list(reversed(t2_img.GetSpacing())))
    size = np.array(list(reversed(t2_img.GetSize())))
    print(f'{idx}, {dir_name}, MR_T2, {size}, {spacing}, {origin}, {minv}, {maxv}, {minv_1}, {maxv_99}, {mean}')


def main(root, func):
    dirs = os.listdir(root)

    if func == load_slices:
        print('num, series_IDs, PatientID, name, Size(zyx), Spacing(zyx), Origin(zyx), minv, maxv, minv_1, maxv_99, mean')
    elif func == load_series:
        print('num, name, modality, Size(zyx), Spacing(zyx), Origin(zyx), minv, maxv, minv_1, maxv_99, mean')
    for id, dir_name in enumerate(dirs):
        func(id, op_join(root, dir_name))


if __name__ == '__main__':
    # root = r'/public/home/hb/datasets/'
    # root = r'G:/datasets/Pelvis/Gold-Atlas/dicom'
    root = r'G:/datasets/Pelvis/Gold-Atlas/data/src'
    main(root, func=load_series)
