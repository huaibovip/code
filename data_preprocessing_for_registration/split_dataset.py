import os
import random
import shutil
import pickle


def split_data(data_root, verbose=False):
    src_root = os.path.join(data_root, 'IXI-T2')
    # 403, 58, 115
    HH_fnames = [name[:-12] for name in os.listdir(src_root) if name.find('HH') != -1]
    IOP_fnames = [name[:-12] for name in os.listdir(src_root) if name.find('IOP') != -1]
    Guys_fnames = [name[:-12] for name in os.listdir(src_root) if name.find('Guys') != -1]
    fnames = HH_fnames + IOP_fnames + Guys_fnames

    random.shuffle(HH_fnames)
    random.shuffle(IOP_fnames)
    random.shuffle(Guys_fnames)

    # print(len(HH_fnames))   # 129, 19, 36
    # print(len(IOP_fnames))  # 51, 7, 15
    # print(len(Guys_fnames)) # 223, 32, 64
    # print(len(fnames))

    train_HH_fnames = HH_fnames[:129]
    val_HH_fnames = HH_fnames[129:129+19]
    test_HH_fnames = HH_fnames[129+19:]

    train_IOP_fnames = IOP_fnames[:51]
    val_IOP_fnames = IOP_fnames[51:51+7]
    test_IOP_fnames = IOP_fnames[51+7:]

    train_Guys_fnames = Guys_fnames[:223]
    val_Guys_fnames = Guys_fnames[223:223+32]
    test_Guys_fnames = Guys_fnames[223+32:]

    train_fnames = train_HH_fnames + train_IOP_fnames + train_Guys_fnames
    val_fnames = val_HH_fnames + val_IOP_fnames + val_Guys_fnames
    test_fnames = test_HH_fnames + test_IOP_fnames + test_Guys_fnames

    with open('ixi_split_fnames.pkl', 'wb') as f:
        pickle.dump((train_fnames, val_fnames, test_fnames), f)

    if verbose:
        print(len(fnames))
        print(len(train_fnames))
        print(len(val_fnames))
        print(len(test_fnames))
        for names in [train_fnames, val_fnames, test_fnames]:
            HH_count = 0
            IOP_count = 0
            Guys_count = 0
            for name in names:
                if name.find('HH') != -1:
                    HH_count += 1
                elif name.find('IOP') != -1:
                    IOP_count += 1
                elif name.find('Guys') != -1:
                    Guys_count += 1
            print(f'HH_count={HH_count}, IOP_count={IOP_count}, Guys_count={Guys_count}')
            print(f'HH_count={HH_count/len(names)}, IOP_count={IOP_count/len(names)}, Guys_count={Guys_count/len(names)}')


def move_data(root, ixi_fnames_path):
    train_root = os.path.join(root, 'Train')
    val_root = os.path.join(root, 'Val')
    test_root = os.path.join(root, 'Test')
    os.makedirs(train_root, exist_ok=True)
    os.makedirs(val_root, exist_ok=True)
    os.makedirs(test_root, exist_ok=True)

    with open(ixi_fnames_path, 'rb') as f:
        # train_fnames, val_fnames, test_fnames = pickle.load(f)
        fnames = pickle.load(f)

    for names, dst_root in zip(fnames, (train_root, val_root, test_root)):
        print(len(names))
        for name in names:
            src = os.path.join(root, name + '*')
            dst = dst_root
            try:
                os.system(f'mv {src} {dst}')
            except Exception as e:
                print(name, e)


if __name__ == '__main__':
    data_root = '/public/home/hb/datasets/i2i/IXI/outputs/final_outputs'
    pkl_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    ixi_split_fnames = os.path.join(pkl_root, 'ixi_split_fnames.pkl')
    if not os.path.exists(pkl_root):
        os.makedirs(pkl_root)

    modality = ['T1', 'T2', 'PD']
    for m in modality[2:]:
        move_data(os.path.join(data_root, f'IXI-{m}'), ixi_split_fnames)
