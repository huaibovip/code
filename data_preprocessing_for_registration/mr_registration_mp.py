import os
import glob
import multiprocessing as mp
import time
from nipype.interfaces.ants import Registration


MP = True


def get_args(
    ants_path, save_dir, fix_path, mov_path, fix_mask=None, mov_mask=None, verbose=False
):
    mov_name = os.path.basename(mov_path)

    reg = Registration()
    reg.inputs.fixed_image = fix_path
    reg.inputs.moving_image = mov_path
    reg.inputs.output_warped_image = os.path.join(save_dir, mov_name)
    # reg.inputs.fixed_image_masks = ['NULL', fix_path]
    # reg.inputs.initial_moving_transform = 'trans.mat'
    # reg.inputs.invert_initial_moving_transform = [False, False]
    # reg.inputs.output_transform_prefix = os.path.join(save_dir, 'warped_')
    reg.inputs.dimension = 3
    reg.inputs.interpolation = "Linear"
    reg.inputs.transforms = ["Rigid", "Affine"]
    reg.inputs.transform_parameters = [(0.1,), (0.1,)]
    reg.inputs.number_of_iterations = [[1000, 500, 250, 0], [1000, 500, 250, 100, 0]]
    reg.inputs.convergence_threshold = [1.0e-6, 1.0e-6]
    reg.inputs.convergence_window_size = [10, 10]
    reg.inputs.write_composite_transform = False
    reg.inputs.collapse_output_transforms = False
    reg.inputs.initialize_transforms_per_stage = False
    reg.inputs.metric = ["MI"] * 2
    reg.inputs.metric_weight = [1] * 2  # Default (value ignored currently by ANTs)
    reg.inputs.radius_or_number_of_bins = [32] * 2
    reg.inputs.sampling_strategy = ["Regular", "Random"]
    reg.inputs.sampling_percentage = [0.25, 0.25]
    reg.inputs.smoothing_sigmas = [[4, 3, 2, 1], [4, 3, 2, 1, 1]]
    reg.inputs.sigma_units = ["vox"] * 2
    reg.inputs.shrink_factors = [[12, 8, 4, 2], [12, 8, 4, 2, 1]]
    reg.inputs.use_estimate_learning_rate_once = [True, True]
    reg.inputs.use_histogram_matching = [True] * 2  # This is the default
    reg.inputs.winsorize_lower_quantile = 0.005
    reg.inputs.winsorize_upper_quantile = 0.995
    reg.inputs.float = True
    reg.inputs.verbose = verbose
    cmdline = reg.cmdline
    cmdline = cmdline.replace("--use-estimate-learning-rate-once 1", "")
    cmdline = cmdline.replace("--initialize-transforms-per-stage 0", "")
    cmdline = os.path.join(ants_path, cmdline)
    if verbose:
        print(cmdline)
    return cmdline


def register(**kwargs):
    print(kwargs['mov_path'], kwargs['fix_path'])
    args = get_args(**kwargs)
    os.system(args)


def main():
    ants_path = "/public/home/hb/softwares/ants/bin/"
    dataset_root = "/public/home/hb/datasets/i2i/IXI/outputs"

    modalities = ['T1', 'T2', 'PD']
    whole_brain = False
    verbose = False

    subdir = "reg_outputs_whole" if whole_brain else "reg_outputs"
    atlas_name = "atlases/mni_icbm152_nlin_asym_09a/mni_icbm152_{}_tal_nlin_asym_09a.nii" \
        if whole_brain else "atlases/mni_icbm152_nlin_asym_09a/brain/mni_icbm152_{}_tal_nlin_asym_09a_brain.nii"
    data_root = os.path.join(dataset_root, "bet_outputs")
    save_root = os.path.join(dataset_root, subdir)
    fix_path_template = os.path.join(
        os.path.split(__file__)[0],
        atlas_name
    )

    if MP:
        print(f'[cpu count] {mp.cpu_count()}')
        pool = mp.Pool(mp.cpu_count())

    start = time.time()
    for m in modalities:
        save_dir = os.path.join(save_root, "IXI-" + m)
        os.makedirs(save_dir, exist_ok=True)
        fix_path = fix_path_template.format(m.lower())
        # registration
        for mov_path in glob.glob(os.path.join(data_root, 'IXI-' + m, '*')):
            if MP:
                pool.apply_async(func=register, args=(ants_path,save_dir,fix_path,mov_path))
            else:
                register(
                    ants_path=ants_path,
                    save_dir=save_dir,
                    fix_path=fix_path,
                    mov_path=mov_path,
                    fix_mask=None,
                    mov_mask=None,
                    verbose=verbose,
                )
    if MP:
        pool.close()
        pool.join()
    print(f'time: {time.time() - start} done.')


if __name__ == "__main__":
    main()



"""
# python 3.10.13
pip install nipype==1.8.6
path_to_antsRegistration \
    --collapse-output-transforms 1 \
    --dimensionality 3 \
    --float 1 \
    --interpolation Linear \
    --output [output_, output_warped_t1.nii.gz] \
    --transform Rigid[0.1] \
    --metric MI[mni_icbm152_t1_tal_nlin_asym_09a.nii, input_t1w.nii.gz, 1, 32, Regular, 0.25] \
    --convergence [1000x500x250x0, 1e-06, 10] \
    --smoothing-sigmas 4.0x3.0x2.0x1.0vox \
    --shrink-factors 12x8x4x2 \
    --use-histogram-matching 1 \
    --transform Affine[0.1] \
    --metric MI[mni_icbm152_t1_tal_nlin_asym_09a.nii, input_t1w.nii.gz, 1, 32, Random, 0.25] \
    --convergence [1000x500x250x100x0, 1e-06, 10] \
    --smoothing-sigmas 4.0x3.0x2.0x1.0x1.0vox \
    --shrink-factors 12x8x4x2x1 \
    --use-histogram-matching 1 \
    --winsorize-image-intensities [0.005, 0.995] \
    --write-composite-transform 0
    --verbose 1
"""
