import os
import yaml
import copy
import random
import argparse
from os.path import join as op_join
from typing import List

import numpy as np

from pelvis_1_slice import save_slice, slice_nib


################################################################ 
#                        config yaml                           #
################################################################
def save_dict_to_yaml(dict_value: dict, save_path: str):
    with open(save_path, 'w') as file:
        file.write(yaml.dump(dict_value, sort_keys=False, allow_unicode=True))
 
 
def get_config_from_yaml(yaml_path: str):
    with open(yaml_path) as file:
        dict_value = yaml.load(file.read(), Loader=yaml.FullLoader)
        return dict_value
    

def get_slice_range(root):
    slices = os.listdir(root)
    slices = [int(s.split('_')[-1].split('.')[0]) for s in slices]
    return slices


def get_slice_min_max(root):
    slice_range = get_slice_range(root)
    min_val, max_val = min(slice_range), max(slice_range)
    return min_val, max_val


def split_phase(fnames, splits: List=[0.7, 0.1, 0.2]):
    # assert sum(splits) == 1. and len(splits) == 3
    random.shuffle(fnames)
    
    s1 = int(len(fnames) * splits[0])
    s2 = int(len(fnames) * (splits[0] + splits[1]))
    
    train_fnames = sorted(fnames[:s1])
    val_fnames = sorted(fnames[s1: s2])
    test_fnames = sorted(fnames[s2:])
    
    return {
        'train': train_fnames,
        'val': val_fnames,
        'test': test_fnames
    }


def gen_pelvis_config(root) -> List:
    datasets = {
        'name': 'MR-CT Dataset',
        'url': 'https://zenodo.org/record/583096',
        'root': root,
        'modals': ['MR', 'CT'],
        'synthesis_cfg':[
            'MR_CT',
            ],
        }

    fnames_dict = split_phase(os.listdir(root))
    dataset = {}
    for phase, fnames in fnames_dict.items():
        print(f'{phase} dataset size is {len(fnames)}')
        if len(fnames) == 0:
            continue
        
        data_dict = {}
        for idx, name in enumerate(fnames):
            sub_root = os.path.join(root, name)
            min_val, max_val = get_slice_min_max(sub_root)
            sub_dict = {
                'name': name[:6],
                'min': min_val,
                'max': max_val,
                'len': max_val - min_val + 1
            }
            data_dict.update({idx: sub_dict})
        dataset.update({phase: data_dict})
    datasets.update({'dataset': dataset})
    
    return datasets


################################################################ 
#                       generate dataset                       #
################################################################
def print_config(cfg):
    if len(cfg) == 2:
        print(f'{cfg[0]} -> {cfg[1]}')
    elif len(cfg) > 2:
        msg = ''
        for i in range(len(cfg) - 1):
            if i != 0:
                msg += ' + '
            msg += cfg[i]
        msg += ' -> ' + cfg[-1]
        print(msg)


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


def parser_config(cfg):
    cfg_ = copy.deepcopy(cfg)
    cfg_ = cfg_.split('_')
    if '' in cfg_:
        cfg_.remove('')
    print_config(cfg_)
    return cfg_


def make_dataset(cfg_path, test):
    datasets = get_config_from_yaml(cfg_path)
    root = datasets.get('root')
    dataset = datasets.get('dataset')
    syn_cfg = datasets.get('synthesis_cfg')
    for cfg_name in syn_cfg:
        # cfg = parser_config(cfg_name)
        for phase, subjects in dataset.items():
            print(f'[{phase}] dataset size is {len(subjects)}')
            for idx, sub in subjects.items():
                name = sub.get('name')
                len_s = sub.get('len')
                print(f'\n[{name}] subject size is {len_s}')
                
                sdir = 'png_dst' if test else 'npy_dst'
                src_root = op_join(root, 'src', name)
                dst_root = op_join(root, sdir, phase, name)
                os.makedirs(dst_root, exist_ok=True)

                t2_arr = slice_nib('MR_T2', src_root)
                ct_arr = slice_nib('CTtoMR', src_root)
                for s in range(sub.get('min'), sub.get('max') + 1):
                    t2_slice = t2_arr[:, :, s - 1]
                    ct_slice = ct_arr[:, :, s - 1]
                    if test:
                        im_slice = np.concatenate([t2_slice, ct_slice], 1)
                    else:
                        im_slice = np.stack([t2_slice, ct_slice])
                    save_slice(op_join(dst_root, name + f'_{s}'), im_slice, test)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-g', '--generate_config', action='store_true', help='')
    parser.add_argument('-t', '--test', action='store_true', help='')
    args = parser.parse_args()

    root = r'G:/datasets/Pelvis/Gold-Atlas/data'
    if args.generate_config:
        config = gen_pelvis_config(os.path.join(root, 'png_dst'))
        save_dict_to_yaml(config, 'pelvis_config.yaml')
    else:
        make_dataset('./pelvis_config.yaml', test=args.test)
    