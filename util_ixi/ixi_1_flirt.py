import os
import time
import shutil
import multiprocessing as mp

from ixi_config import (
    T1, T2, PD, MP,
    REF_MODALITY,
    INTERPOLATION,
    SRC_TMP_ROOT,
    SRC_ROOT
)

FLIRT = 'flirt'
# FLIRT = 'fsl5.0-flirt'


def move_files(modalities):
    for m in modalities:
        src = os.path.join(SRC_TMP_ROOT, m)
        dst = os.path.join(SRC_ROOT, m)
        shutil.move(src, dst)


def flirt_func(idx, in_path, ref_path, out_path, mat_path=None, interpolation='trilinear'):
    start = time.time()
    if mat_path is None:
        cmd = '{} -in {} -ref {} -out {} -bins 256 -cost mutualinfo -searchrx -90 90 -searchry -90 90 -searchrz -90 90 -dof 12 -interp {}'
        cmd_line = cmd.format(FLIRT, in_path, ref_path, out_path, interpolation)
    else:
        cmd = '{} -in {} -ref {} -out {} -omat {} -bins 256 -cost mutualinfo -searchrx -90 90 -searchry -90 90 -searchrz -90 90 -dof 12 -interp {}'
        cmd_line = cmd.format(FLIRT, in_path, ref_path, out_path, mat_path, interpolation)
    
    # print(cmd_line)
    ret = os.system(cmd_line)
    if ret == 0:
        print(f'{idx + 1} time: {time.time() - start}  {in_path}  ->  {out_path}')
    else:
        print(f'[error] idx: {idx + 1} {in_path} ret: {ret}')


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
        in_name = fnames[i][:-9] + in_modal[-2:]
        ref_name = fnames[i][:-9] + ref_modal[-2:]
        in_path = os.path.join(root, in_modal, in_name + '.nii.gz')
        ref_path = os.path.join(root, ref_modal, ref_name + '.nii.gz')

        if os.path.isfile(in_path) and os.path.isfile(ref_path):
            out_path = os.path.join(out_root, in_modal, in_name)
            mat_path = os.path.join(mat_root, in_modal, in_name + '.mat')
            if MP:
                pool.apply_async(func=flirt_func, args=(i, in_path, ref_path, out_path, mat_path, interpolation))
            else:
                flirt_func(i, in_path, ref_path, out_path, mat_path, interpolation)
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
        move_files([T2, PD])
    else:
        for (im, rm) in [(T1, PD)]:
            main(root=SRC_TMP_ROOT, out_root=SRC_ROOT, in_modal=im, ref_modal=rm, interpolation=INTERPOLATION)
        move_files([T2, PD])

    shutil.rmtree(SRC_TMP_ROOT)
