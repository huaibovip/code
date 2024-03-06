import os

import tarfile
from ixi_config import T1, T2, PD, TAR_ROOT, SRC_TMP_ROOT
from ixi_3_yaml import get_config_from_from_yaml, get_names


def untar(tar_root, tar_name, yaml_path):
    cfg = get_config_from_from_yaml(yaml_path)
    names = get_names(cfg)
    dst_root = os.path.join(SRC_TMP_ROOT, tar_name)
    os.makedirs(dst_root, exist_ok=True)

    tar_path = os.path.join(tar_root, tar_name + '.tar')
    tar = tarfile.open(tar_path)
    for name in names:
        fname = name + '-' + tar_name[4:6] + '.nii.gz'
        tar.extract(fname, dst_root)
    tar.close()


if __name__ == "__main__":
    for m in [T1, T2, PD]:
        untar(TAR_ROOT, m, "ixi_config.yaml")
