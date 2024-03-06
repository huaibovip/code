import ants

fix_path = 'mni_icbm152_nlin_asym_09a/mni_icbm152_t1_tal_nlin_asym_09a.nii'
mov_path = 'T1w.nii.gz'

fix = ants.image_read(fix_path)
mov = ants.image_read(mov_path)

moved = ants.registration(
        fixed=fix,
        moving=mov,
        type_of_transform='Affine',
        initial_transform=None,
        outprefix="moved_",
        mask=None,
        moving_mask=None,
        mask_all_stages=False,
        grad_step=0.2,
        flow_sigma=3,
        total_sigma=0,
        aff_metric="MI",
        aff_sampling=32,
        aff_random_sampling_rate=0.2,
        syn_metric="mattes",
        syn_sampling=32,
        reg_iterations=(40, 20, 0),
        aff_iterations=(2100, 1200, 1200, 10),
        aff_shrink_factors=(6, 4, 2, 1),
        aff_smoothing_sigmas=(3, 2, 1, 0),
        write_composite_transform=False,
        random_seed=None,
        verbose=True,
        multivariate_extras=None,
        restrict_transformation=None,
        smoothing_in_mm=False,
)

# # ants.resample_image_to_target()
# # print(moved)
# ants.image_write(moved['warpedmovout'], filename='moved_T1w.nii.gz')
# # ants.image_write(moved['fwdtransforms'], filename='moved_T1w.nii.gz')
