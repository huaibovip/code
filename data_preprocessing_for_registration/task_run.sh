# step 1
nohup python -u mr_skull_strip.py > logs/mr_skull_strip.log 2>&1 &

# step 2
nohup python -u mr_registration.py > logs/mr_registration.log 2>&1 &

# step 3
nohup python -u crop_volume_gen_mask.py > logs/crop_volume_gen_mask.log 2>&1 &

# step 4
nohup python -u mr_n4_normalization.py > logs/mr_n4_normalization.log 2>&1 &

# step 5
nohup python -u synthseg.py >> logs/synthseg.log 2>&1 &

# step 6
nohup python -u make_dataset.py >> logs/make_dataset.log 2>&1 &

# step 7
nohup python -u split_dataset.py >> logs/split_dataset.log 2>&1 &
