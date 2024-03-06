import os
import glob
from utils.io import pkload
from utils.plot import plot_slices


if __name__ == "__main__":
    dataset_root = "/public/home/hb/datasets/i2i/IXI/outputs"

    data_root = os.path.join(dataset_root, 'final_outputs')
    save_root = os.path.join(dataset_root, 'check_outputs')
    modalities = ['T1', 'T2', 'PD']

    for m in modalities[:2]:
        save_dir = os.path.join(save_root, "IXI-" + m)
        os.makedirs(save_dir, exist_ok=True)
        for input_path in glob.glob(os.path.join(data_root, 'IXI-' + m, '*'))[:1]:
            output_path = os.path.join(save_dir, os.path.basename(input_path)[:-7] + '_slice.png')
            vols = pkload(input_path)
            # run
            fig, axs = plot_slices(vols)
            fig.savefig(output_path)
