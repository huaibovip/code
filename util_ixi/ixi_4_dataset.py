import os
import shutil

import cv2
import h5py
import numpy as np

from ixi_3_yaml import get_config_from_from_yaml
from ixi_config import (
    DATASET_TYPE,
    DST_ROOT,
    IMG_CLIP,
    SLICE_ROOT,
)


def print_write_info(path_a, path_b):
    b = os.path.basename(path_b)
    if isinstance(path_a, list) and len(path_a) > 1:
        a = [os.path.basename(p) for p in path_a]
        msg = ''
        for i in range(len(a)):
            if i != 0:
                msg += ' + '
            msg += a[i]
        msg += ' -> ' + b
        print(msg)
    else:
        a = os.path.basename(path_a)
        print(f'{a} -> {b}')


def image_write(path_a, path_b, ab_path):
    import cv2
    print_write_info(path_a, path_b)
    if isinstance(path_a, list) and len(path_a) > 1:
        im_a_list = []
        for p in path_a:
            im = cv2.imread(p, cv2.IMREAD_GRAYSCALE) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
            im_a_list.append(im)
        if len(im_a_list) == 2:
            im = np.zeros_like(im_a_list[0])
            im_a_list.append(im)
        im_a = np.stack(im_a_list, -1)
    else:
        im_a = cv2.imread(path_a, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
    im_b = cv2.imread(path_b, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
    im_ab = np.concatenate([im_a, im_b], 1)
    cv2.imwrite(ab_path, im_ab)


def make_png_dataset(cfg_path, src_root, dst_root):
    datasets = get_config_from_from_yaml(cfg_path)
    dataset = datasets.get('dataset')
    modals = datasets.get('modals')
    modals_name = '_'.join(modals)

    for phase, subjects in dataset.items():
        phase_root = os.path.join(dst_root, 'ixi_' + modals_name.lower(), phase)
        os.makedirs(phase_root, exist_ok=True)
        print(f'[{phase}] dataset size is {len(subjects)}')
        for idx, sub in subjects.items():
            name = sub.get('name')
            len_s = sub.get('len')
            print(f'\n[{name}] subject size is {len_s}')            
            ab_root = os.path.join(phase_root, name)
            os.makedirs(ab_root, exist_ok=True)
            modal_paths = {m: os.path.join(src_root, 'IXI-' + m, name + '-' + m, name + '-' + m + '_{}.npy') for m in modals}
            for idx, s in enumerate(range(sub.get('min'), sub.get('max') + 1)):
                # data = [cv2.imread(img_path.format(s), cv2.IMREAD_GRAYSCALE) for img_path in modal_paths.values()]
                data = [np.load(img_path.format(s)) * 255.0 for img_path in modal_paths.values()]
                cv2.imwrite(os.path.join(ab_root, str(idx) + '.png'), np.concatenate(data, axis=-1))


def make_npy_dataset(cfg_path, src_root, dst_root):
    datasets = get_config_from_from_yaml(cfg_path)
    dataset = datasets.get('dataset')
    modals = datasets.get('modals')
    modals_name = '_'.join(modals)

    for phase, subjects in dataset.items():
        phase_root = os.path.join(dst_root, 'ixi_' + modals_name.lower(), phase)
        os.makedirs(phase_root, exist_ok=True)
        print(f'[{phase}] dataset size is {len(subjects)}')
        for idx, sub in subjects.items():
            name = sub.get('name')
            len_s = sub.get('len')
            print(f'\n[{name}] subject size is {len_s}')            
            ab_root = os.path.join(phase_root, name)
            os.makedirs(ab_root, exist_ok=True)
            modal_paths = {m: os.path.join(src_root, 'IXI-' + m, name + '-' + m, name + '-' + m + '_{}.npy') for m in modals}
            for idx, s in enumerate(range(sub.get('min'), sub.get('max') + 1)):
                data = [np.load(img_path.format(s)) for img_path in modal_paths.values()]
                np.save(os.path.join(ab_root, str(idx)), np.stack(data))


def make_hdf5_dataset(cfg_path, src_root, dst_root):
    datasets = get_config_from_from_yaml(cfg_path)
    dataset = datasets.get('dataset')
    modals = datasets.get('modals')
    modals_name = '_'.join(modals)
    print(modals_name)
    for phase, subjects in dataset.items():
        phase_root = os.path.join(dst_root, phase)
        os.makedirs(phase_root, exist_ok=True)
        f = h5py.File(os.path.join(phase_root, f'ixi_{modals_name.lower()}_{phase}.hdf5'), 'w')
        group = f.create_group(name=modals_name)
        print(f'[{phase}] dataset size is {len(subjects)}')
        for idx, sub in subjects.items():
            name = sub.get('name')
            len_s = sub.get('len')
            print(f'\n[{name}] subject size is {len_s}')
            sub_group = group.create_group(name=name)
            modal_paths = {m: os.path.join(src_root, 'IXI-' + m, name + '-' + m, name + '-' + m + '_{}.npy') for m in modals}
            for idx, s in enumerate(range(sub.get('min'), sub.get('max') + 1)):
                slice_group = sub_group.create_group(name=str(idx))
                for name, img_path in modal_paths.items():
                    slice_group.create_dataset(
                        name=name,
                        shape=(256, 256),
                        dtype=np.float32,
                        data=np.load(img_path.format(s)))


if __name__ == '__main__':
    flag = 'clip' if IMG_CLIP else 'noclip'
    src_root = os.path.join(SLICE_ROOT, 'npy_' + flag + '_slice')
    dst_root = os.path.join(DST_ROOT, DATASET_TYPE + '_' + flag + '_dst')

    func = 'make_' + DATASET_TYPE + '_dataset(\'ixi_config.yaml\', src_root, dst_root)'
    eval(func)
    
    shutil.rmtree(SLICE_ROOT)
