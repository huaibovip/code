import os
import random
import yaml

from ixi_config import T1, SLICE_ROOT


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
    slices = [int(s.split('_')[1][:-4]) for s in slices]
    return slices


def get_slice_min_max(root):
    slice_range = get_slice_range(root)
    min_val, max_val = min(slice_range), max(slice_range)
    return min_val, max_val


def split_phase(fnames, splits=[0.7, 0.1, 0.2]):
    # assert sum(splits) == 1. and len(splits) == 3
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


def gen_config(root) -> list:
    subjects = {}
    fnames = os.listdir(root)    
    for idx, name in enumerate(fnames):
        sub_root = os.path.join(root, name)
        min_val, max_val = get_slice_min_max(sub_root)
        sub_dict = {
            'id': idx,
            'min': min_val,
            'max': max_val,
            'len': max_val - min_val + 1
        }
        subjects.update({name[:-3]: sub_dict})
    return subjects


def gen_ixi_config(root) -> list:
    datasets = {
        'name': 'IXI Dataset',
        'url': 'http://brain-development.org/ixi-dataset',
        'root': root,
        'modals': ['T1', 'T2', 'PD'],
        'synthesis_cfg':[
            'T2_PD',
            'T1_T2__PD',
            'T1_PD__T2',
            'T2_PD__T1',
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
                'name': name[:-3],
                'min': min_val,
                'max': max_val,
                'len': max_val - min_val + 1
            }
            data_dict.update({idx: sub_dict})
        dataset.update({phase: data_dict})
    datasets.update({'dataset': dataset})
    
    return datasets


# if __name__ == '__main__':
#     ref_root = os.path.join(SLICE_ROOT, 'npy_clip_slice', T1)
#     config = gen_config(ref_root)
#     save_config_to_yaml(config, 'ixi_config_tmps.yaml')
#     config = gen_ixi_config(ref_root)
#     save_config_to_yaml(config, 'ixi_config.yaml')
