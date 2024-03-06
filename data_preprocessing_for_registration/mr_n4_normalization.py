import os


def get_args(
    input,
    output,
    mask=None,
    bias_field=None,
    rescale_intensities=True,
    weight_image=None,
    shrink_factor=4,
    # convergence
    convergence=[50, 40, 30],
    convergence_threshold=0.0001,
    # bspline-fitting
    spline_distance=0,
    initial_mesh_resolution=[1, 1, 1],
    spline_order=3,
    # histogram-sharpening
    fwhm=0,
    wiener_noise=0,
    number_of_histogram_bins=0,
    verbose=False,
):

    rescale_intensities = 1 if verbose else 0
    convergence = 'x'.join(map(str, convergence))
    initial_mesh_resolution = 'x'.join(map(str, initial_mesh_resolution))
    verbose = 1 if verbose else 0

    cmd = "N4BiasFieldCorrection"
    cmd += " -d 3"
    cmd += f" -i {input}"
    if mask is not None:
        cmd += f" -x {mask}"
    cmd += f" -r {rescale_intensities}"
    if weight_image is not None:
        cmd += f" -w {weight_image}"
    cmd += f" -s {shrink_factor}"
    cmd += f" -c [{convergence},{convergence_threshold}]"
    cmd += f" -b [{spline_distance},{spline_order}] [{initial_mesh_resolution},{spline_order}]"
    cmd += f" -t [{fwhm},{wiener_noise},{number_of_histogram_bins}]"
    if bias_field is not None:
        cmd += f" -o [{output},{bias_field}]"
    else:
        cmd += f" -o [{output}]"
    cmd += f" -v {verbose}"
    return cmd


def n4_norm(ants_path, input, output, mask=None, bias_field=None):
    cmd = get_args(input, output, mask=mask, bias_field=bias_field)
    print(cmd)
    cmd = os.path.join(ants_path, cmd)
    os.system(cmd)


if __name__ == "__main__":
    ants_path = "~/softwares/ants/bin"

    # dataset_root = "/public/home/hb/datasets/i2i/IXI"
    # data_root = os.path.join(dataset_root, "raw")
    # save_root = os.path.join(dataset_root, "outputs2")
    # modalities = ["T1", "T2", "PD"]

    # for m in modalities:
    #     save_dir = os.path.join(save_root, "bet_outputs", "IXI-" + m)
    #     os.makedirs(save_dir, exist_ok=True)
    #     for input_path in glob.glob(os.path.join(data_root, "IXI-" + m, "*"))[:2]:
    #         output_path = os.path.join(save_dir, os.path.basename(input_path))
    #         n4_norm(
    #             input_path,
    #             output_path,
    #         )

    n4_norm(ants_path, input='/public/home/hb/datasets/i2i/IXI/outputs/reg_outputs/IXI-T1/IXI012-HH-1211-T1.nii.gz', output='./n4_t1.nii.gz')

    # N4BiasFieldCorrection -d 3 \
    # -i /public/home/hb/datasets/i2i/IXI/outputs/reg_outputs/IXI-T1/IXI012-HH-1211-T1.nii.gz \
    # -r 0 \
    # -s 4 \
    # -c [50x50x50x50,0.0001] \
    # -b [180,3] [1x1x1,3] \
    # -o [./n4_t1.nii.gz] \
    # -v 0