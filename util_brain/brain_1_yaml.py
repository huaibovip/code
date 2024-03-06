import os
import random
import yaml

from brain_config import T1GD, SLICE_ROOT, TYPE
from brain_config import (
    verio_with_segm,
    verio_without_segm,
    triotim1_with_segm,
    triotim1_without_segm,
    triotim3_with_segm,
    triotim3_without_segm,
)


def save_config_to_yaml(dict_value: dict, save_path: str):
    with open(save_path, 'w') as file:
        file.write(yaml.dump(dict_value, allow_unicode=True, sort_keys=False))

 
def get_config_from_from_yaml(yaml_path: str):
    with open(yaml_path) as file:
        dict_value = yaml.load(file.read(), Loader=yaml.FullLoader)
        return dict_value


def get_names(config):
    names = []
    dataset = config['dataset']
    for phase in dataset.keys():
        for sub in dataset[phase].values():
            names.append(sub['name'])
    return names


def get_slice_range(root):
    slices = os.listdir(root)
    slices = [int(s.split('_')[-1][:-4]) for s in slices]
    return slices


def get_slice_min_max(root):
    slice_range = get_slice_range(root)
    min_val, max_val = min(slice_range), max(slice_range)
    return min_val, max_val


def split_phase(fnames, splits=[0.7, 0.1, 0.2]):
    # assert sum(splits) == 1. and len(splits) == 3
    random.seed(100)
    random.shuffle(fnames)

    s1 = int(len(fnames) * splits[0])
    s2 = int(len(fnames) * (splits[0] + splits[1]))
    
    train_fnames = fnames[:s1]
    val_fnames = fnames[s1: s2]
    test_fnames = fnames[s2:]
    
    return {
        'train': train_fnames,
        'val': val_fnames,
        'test': test_fnames
    }


def split_phase_brain(fnames_with_segm, fnames_without_segm, splits=[0.7, 0.1, 0.2]):
    fnames_with_segm_dict = split_phase(fnames_with_segm, splits)
    fnames_without_segm_dict = split_phase(fnames_without_segm, splits)

    ret_fnames_dict = {}
    for k in fnames_with_segm_dict.keys():
        ret_fnames_dict[k] = fnames_with_segm_dict[k] + fnames_without_segm_dict[k]
    return ret_fnames_dict


def gen_config(root, ref_modality) -> list:
    subjects = {}
    fnames = os.listdir(root)    
    for idx, name in enumerate(fnames):
        sub_root = os.path.join(root, name, ref_modality)
        min_val, max_val = get_slice_min_max(sub_root)
        sub_dict = {
            'id': idx,
            'min': min_val,
            'max': max_val,
            'len': max_val - min_val + 1
        }
        subjects.update({name: sub_dict})
    return subjects


def gen_brain_config(root, ref_modality, fnames_with_segm, fnames_without_segm) -> list:
    datasets = {
        'name': 'Brain Dataset',
        'url': 'https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=70225642',
        'root': root,
        'modals': ['T1', 'T1GD', 'T2', 'FLAIR'],
        'synthesis_cfg':[
            'T1_T1GD',
            'T1GD_T1',
            'T2_FLAIR',
            'FLAIR_T2',
            'T1_T2__FLAIR',
            'T1_FLAIR__T2',
            'T2_FLAIR__T1',
            ],
        }
    assert sorted(fnames_with_segm + fnames_without_segm) == sorted(os.listdir(root))
    fnames_dict = split_phase_brain(fnames_with_segm, fnames_without_segm)
    dataset = {}
    for phase, fnames in fnames_dict.items():
        print(f'{phase} dataset size is {len(fnames)}')
        if len(fnames) == 0:
            continue
        
        data_dict = {}
        for idx, name in enumerate(fnames):
            sub_root = os.path.join(root, name, ref_modality)
            min_val, max_val = get_slice_min_max(sub_root)
            sub_dict = {
                'name': name,
                'min': min_val,
                'max': max_val,
                'len': max_val - min_val + 1
            }
            data_dict.update({idx: sub_dict})
        dataset.update({phase: data_dict})
    datasets.update({'dataset': dataset})
    
    return datasets


if __name__ == '__main__':
    fnames_with_segm = eval(f'{TYPE}_with_segm')
    fnames_without_segm = eval(f'{TYPE}_without_segm')

    ref_root = os.path.join(SLICE_ROOT, 'npy_clip_slice')
    # config = gen_config(ref_root, T1GD)
    # save_config_to_yaml(config, f'brain_{TYPE}_config_tmps1.yaml')
    config = gen_brain_config(ref_root, T1GD, fnames_with_segm, fnames_without_segm)
    save_config_to_yaml(config, f'brain_{TYPE}_config.yaml')
