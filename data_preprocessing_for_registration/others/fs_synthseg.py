import os
import glob


def get_args(
    input,
    output,
    parc=False,
    robust=True,
    fast=False,
    threads=4,
    cpu=False,
    v1=False,
    ct=False,
    # photo=None,
):
    cmd = "mri_synthseg"
    cmd += f" --i {input}"
    cmd += f" --o {output}"
    if parc:
        cmd += " --parc"
    if robust:
        cmd += " --robust"
    if fast:
        cmd += " --fast"
    if cpu:
        cmd += " --cpu"
    cmd += f" --threads {threads}"
    if v1:
        cmd += " --v1"
    if ct:
        cmd += " --ct"
    return cmd


def fs_synthseg(**kwargs):
    cmd = get_args(**kwargs)
    print(cmd)
    os.system(cmd)


if __name__ == "__main__":

    dataset_root = "/public/home/hb/datasets/i2i/IXI/outputs"

    data_root = os.path.join(dataset_root, 'n4_outputs')
    save_root = os.path.join(dataset_root, 'seg_outputs')
    modalities = ['T1', 'T2', 'PD']

    for m in modalities:
        save_dir = os.path.join(save_root, "IXI-" + m)
        os.makedirs(save_dir, exist_ok=True)
        for input_path in glob.glob(os.path.join(data_root, 'IXI-' + m, '*')):
            output_path = os.path.join(save_dir, os.path.basename(input_path))
            fs_synthseg(input=input_path,output=output_path, ct=False, cpu=False)
