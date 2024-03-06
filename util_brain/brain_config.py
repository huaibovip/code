import os

MP = False

T1 = 'T1'
T2 = 'T2'
T1GD = 'T1GD'
FLAIR = 'FLAIR'

TYPE = 'triotim1'

ROOT = r'G:\datasets\Brain'
SRC_ROOT = os.path.join(ROOT, 'images_structural', TYPE)

# slice
IMG_CLIP = True
SAVE_IMG_PNG = False
SLICE_ROOT = os.path.join(ROOT, 'dataset', 'slice', TYPE)

# dataset
DST_ROOT = os.path.join(ROOT, 'dataset', 'dst', TYPE)
DATASET_TYPE = 'npy' # hdf5, png


triotim1_with_segm = [
    'UPENN-GBM-00002_11', 
    'UPENN-GBM-00006_11', 
    'UPENN-GBM-00008_11', 
    'UPENN-GBM-00009_11', 
    'UPENN-GBM-00011_11', 
    'UPENN-GBM-00013_11', 
    'UPENN-GBM-00014_11', 
    'UPENN-GBM-00016_11', 
    'UPENN-GBM-00018_11', 
    'UPENN-GBM-00021_11', 
    'UPENN-GBM-00029_11', 
    'UPENN-GBM-00031_11', 
    'UPENN-GBM-00033_11', 
    'UPENN-GBM-00040_11', 
    'UPENN-GBM-00043_11', 
    'UPENN-GBM-00059_11', 
    'UPENN-GBM-00060_11', 
    'UPENN-GBM-00062_11', 
    'UPENN-GBM-00066_11', 
    'UPENN-GBM-00073_11', 
    'UPENN-GBM-00076_11', 
    'UPENN-GBM-00080_11', 
    'UPENN-GBM-00101_11', 
    'UPENN-GBM-00105_11', 
    'UPENN-GBM-00106_11', 
    'UPENN-GBM-00107_11', 
    'UPENN-GBM-00113_11', 
    'UPENN-GBM-00154_11', 
    'UPENN-GBM-00158_11', 
    'UPENN-GBM-00166_11', 
    'UPENN-GBM-00173_11', 
    'UPENN-GBM-00174_11', 
    'UPENN-GBM-00178_11', 
    'UPENN-GBM-00189_11', 
    'UPENN-GBM-00192_11', 
    'UPENN-GBM-00193_11', 
    'UPENN-GBM-00206_11', 
    'UPENN-GBM-00208_11', 
    'UPENN-GBM-00217_11', 
    'UPENN-GBM-00226_11', 
    'UPENN-GBM-00227_11', 
    'UPENN-GBM-00228_11', 
    'UPENN-GBM-00249_11', 
    'UPENN-GBM-00251_11', 
    'UPENN-GBM-00252_11', 
    'UPENN-GBM-00253_11', 
    'UPENN-GBM-00254_11', 
    'UPENN-GBM-00256_11', 
    'UPENN-GBM-00259_11', 
    'UPENN-GBM-00266_11', 
    'UPENN-GBM-00270_11', 
    'UPENN-GBM-00272_11', 
    'UPENN-GBM-00274_11', 
    'UPENN-GBM-00275_11', 
    'UPENN-GBM-00277_11'
]

triotim1_without_segm = [
    'UPENN-GBM-00001_11', 
    'UPENN-GBM-00003_11', 
    'UPENN-GBM-00004_11', 
    'UPENN-GBM-00005_11', 
    'UPENN-GBM-00007_11', 
    'UPENN-GBM-00010_11', 
    'UPENN-GBM-00012_11', 
    'UPENN-GBM-00015_11', 
    'UPENN-GBM-00019_11', 
    'UPENN-GBM-00023_11', 
    'UPENN-GBM-00025_11', 
    'UPENN-GBM-00039_11', 
    'UPENN-GBM-00061_11', 
    'UPENN-GBM-00063_11', 
    'UPENN-GBM-00064_11', 
    'UPENN-GBM-00067_11', 
    'UPENN-GBM-00071_11', 
    'UPENN-GBM-00074_11', 
    'UPENN-GBM-00079_11', 
    'UPENN-GBM-00085_11', 
    'UPENN-GBM-00103_11', 
    'UPENN-GBM-00111_11', 
    'UPENN-GBM-00153_11', 
    'UPENN-GBM-00155_11', 
    'UPENN-GBM-00157_11', 
    'UPENN-GBM-00181_11', 
    'UPENN-GBM-00188_11', 
    'UPENN-GBM-00199_11', 
    'UPENN-GBM-00214_11', 
    'UPENN-GBM-00218_11', 
    'UPENN-GBM-00222_11', 
    'UPENN-GBM-00223_11', 
    'UPENN-GBM-00229_11', 
    'UPENN-GBM-00230_11', 
    'UPENN-GBM-00248_11', 
    'UPENN-GBM-00250_11', 
    'UPENN-GBM-00255_11', 
    'UPENN-GBM-00257_11', 
    'UPENN-GBM-00258_11', 
    'UPENN-GBM-00276_11'
]

triotim1 = triotim1_with_segm + triotim1_without_segm


triotim3_with_segm = [
    'UPENN-GBM-00020_11', 
    'UPENN-GBM-00030_11', 
    'UPENN-GBM-00035_11', 
    'UPENN-GBM-00054_11', 
    'UPENN-GBM-00075_11', 
    'UPENN-GBM-00082_11', 
    'UPENN-GBM-00086_11', 
    'UPENN-GBM-00088_11', 
    'UPENN-GBM-00091_11', 
    'UPENN-GBM-00096_11', 
    'UPENN-GBM-00115_11', 
    'UPENN-GBM-00117_11', 
    'UPENN-GBM-00121_11', 
    'UPENN-GBM-00122_11', 
    'UPENN-GBM-00124_11', 
    'UPENN-GBM-00131_11', 
    'UPENN-GBM-00134_11', 
    'UPENN-GBM-00135_11', 
    'UPENN-GBM-00136_11', 
    'UPENN-GBM-00138_11', 
    'UPENN-GBM-00139_11', 
    'UPENN-GBM-00141_11', 
    'UPENN-GBM-00143_11', 
    'UPENN-GBM-00144_11', 
    'UPENN-GBM-00147_11', 
    'UPENN-GBM-00148_11', 
    'UPENN-GBM-00149_11', 
    'UPENN-GBM-00176_11', 
    'UPENN-GBM-00196_11', 
    'UPENN-GBM-00197_11', 
    'UPENN-GBM-00201_11', 
    'UPENN-GBM-00205_11', 
    'UPENN-GBM-00215_11', 
    'UPENN-GBM-00261_11', 
    'UPENN-GBM-00262_11', 
    'UPENN-GBM-00264_11', 
    'UPENN-GBM-00284_11', 
    'UPENN-GBM-00290_11', 
    'UPENN-GBM-00312_11', 
    'UPENN-GBM-00330_11', 
    'UPENN-GBM-00344_11', 
    'UPENN-GBM-00351_11', 
    'UPENN-GBM-00356_11', 
    'UPENN-GBM-00360_11', 
    'UPENN-GBM-00362_11', 
    'UPENN-GBM-00367_11', 
    'UPENN-GBM-00368_11', 
    'UPENN-GBM-00371_11', 
    'UPENN-GBM-00373_11', 
    'UPENN-GBM-00375_11', 
    'UPENN-GBM-00376_11', 
    'UPENN-GBM-00380_11', 
    'UPENN-GBM-00384_11', 
    'UPENN-GBM-00390_11', 
    'UPENN-GBM-00391_11', 
    'UPENN-GBM-00398_11', 
    'UPENN-GBM-00404_11', 
    'UPENN-GBM-00418_11', 
    'UPENN-GBM-00430_11', 
    'UPENN-GBM-00437_11', 
    'UPENN-GBM-00438_11'
]

triotim3_without_segm = [
    'UPENN-GBM-00022_11', 
    'UPENN-GBM-00024_11', 
    'UPENN-GBM-00027_11', 
    'UPENN-GBM-00028_11', 
    'UPENN-GBM-00032_11', 
    'UPENN-GBM-00034_11', 
    'UPENN-GBM-00036_11', 
    'UPENN-GBM-00036_21', 
    'UPENN-GBM-00037_11', 
    'UPENN-GBM-00038_11', 
    'UPENN-GBM-00042_11', 
    'UPENN-GBM-00042_21', 
    'UPENN-GBM-00044_11', 
    'UPENN-GBM-00045_11', 
    'UPENN-GBM-00045_21', 
    'UPENN-GBM-00046_11', 
    'UPENN-GBM-00047_11', 
    'UPENN-GBM-00048_11', 
    'UPENN-GBM-00049_11', 
    'UPENN-GBM-00050_11', 
    'UPENN-GBM-00051_11', 
    'UPENN-GBM-00051_21', 
    'UPENN-GBM-00052_11', 
    'UPENN-GBM-00052_21', 
    'UPENN-GBM-00053_11', 
    'UPENN-GBM-00055_11', 
    'UPENN-GBM-00055_21', 
    'UPENN-GBM-00057_11', 
    'UPENN-GBM-00058_11', 
    'UPENN-GBM-00065_11', 
    'UPENN-GBM-00068_11', 
    'UPENN-GBM-00070_11', 
    'UPENN-GBM-00077_11', 
    'UPENN-GBM-00081_11', 
    'UPENN-GBM-00084_11', 
    'UPENN-GBM-00084_21', 
    'UPENN-GBM-00086_21', 
    'UPENN-GBM-00087_11', 
    'UPENN-GBM-00088_21', 
    'UPENN-GBM-00089_11', 
    'UPENN-GBM-00092_11', 
    'UPENN-GBM-00093_21', 
    'UPENN-GBM-00095_11', 
    'UPENN-GBM-00097_11', 
    'UPENN-GBM-00098_11', 
    'UPENN-GBM-00099_11', 
    'UPENN-GBM-00116_11', 
    'UPENN-GBM-00122_21', 
    'UPENN-GBM-00125_11', 
    'UPENN-GBM-00128_11', 
    'UPENN-GBM-00128_21', 
    'UPENN-GBM-00129_21', 
    'UPENN-GBM-00132_11', 
    'UPENN-GBM-00133_11', 
    'UPENN-GBM-00133_21', 
    'UPENN-GBM-00140_21', 
    'UPENN-GBM-00141_21', 
    'UPENN-GBM-00142_11', 
    'UPENN-GBM-00145_11', 
    'UPENN-GBM-00145_21', 
    'UPENN-GBM-00148_21', 
    'UPENN-GBM-00150_11', 
    'UPENN-GBM-00150_21', 
    'UPENN-GBM-00159_11', 
    'UPENN-GBM-00160_11', 
    'UPENN-GBM-00162_11', 
    'UPENN-GBM-00163_11', 
    'UPENN-GBM-00164_11', 
    'UPENN-GBM-00165_11', 
    'UPENN-GBM-00167_11', 
    'UPENN-GBM-00168_11', 
    'UPENN-GBM-00169_11', 
    'UPENN-GBM-00170_11', 
    'UPENN-GBM-00171_11', 
    'UPENN-GBM-00175_11', 
    'UPENN-GBM-00177_11', 
    'UPENN-GBM-00179_11', 
    'UPENN-GBM-00183_11', 
    'UPENN-GBM-00183_21', 
    'UPENN-GBM-00185_11', 
    'UPENN-GBM-00186_11', 
    'UPENN-GBM-00187_11', 
    'UPENN-GBM-00190_11', 
    'UPENN-GBM-00191_11', 
    'UPENN-GBM-00194_11', 
    'UPENN-GBM-00195_11', 
    'UPENN-GBM-00197_21', 
    'UPENN-GBM-00198_11', 
    'UPENN-GBM-00200_11', 
    'UPENN-GBM-00202_11', 
    'UPENN-GBM-00203_11', 
    'UPENN-GBM-00204_11', 
    'UPENN-GBM-00207_11', 
    'UPENN-GBM-00209_11', 
    'UPENN-GBM-00210_11', 
    'UPENN-GBM-00211_11', 
    'UPENN-GBM-00212_11', 
    'UPENN-GBM-00213_11', 
    'UPENN-GBM-00216_11', 
    'UPENN-GBM-00219_21', 
    'UPENN-GBM-00220_11', 
    'UPENN-GBM-00221_11', 
    'UPENN-GBM-00224_11', 
    'UPENN-GBM-00225_11', 
    'UPENN-GBM-00231_11', 
    'UPENN-GBM-00232_11', 
    'UPENN-GBM-00233_11', 
    'UPENN-GBM-00239_11', 
    'UPENN-GBM-00241_11', 
    'UPENN-GBM-00243_11', 
    'UPENN-GBM-00245_11', 
    'UPENN-GBM-00246_11', 
    'UPENN-GBM-00260_11', 
    'UPENN-GBM-00263_11', 
    'UPENN-GBM-00265_11', 
    'UPENN-GBM-00267_11', 
    'UPENN-GBM-00267_21', 
    'UPENN-GBM-00268_11', 
    'UPENN-GBM-00269_11', 
    'UPENN-GBM-00271_11', 
    'UPENN-GBM-00279_11', 
    'UPENN-GBM-00282_11', 
    'UPENN-GBM-00285_21', 
    'UPENN-GBM-00286_11', 
    'UPENN-GBM-00288_11', 
    'UPENN-GBM-00291_11', 
    'UPENN-GBM-00295_11', 
    'UPENN-GBM-00295_21', 
    'UPENN-GBM-00300_11', 
    'UPENN-GBM-00301_11', 
    'UPENN-GBM-00302_21', 
    'UPENN-GBM-00303_11', 
    'UPENN-GBM-00304_11', 
    'UPENN-GBM-00305_11', 
    'UPENN-GBM-00306_11', 
    'UPENN-GBM-00307_21', 
    'UPENN-GBM-00310_11', 
    'UPENN-GBM-00311_11', 
    'UPENN-GBM-00312_21', 
    'UPENN-GBM-00313_11', 
    'UPENN-GBM-00315_11', 
    'UPENN-GBM-00316_11', 
    'UPENN-GBM-00317_11', 
    'UPENN-GBM-00320_11', 
    'UPENN-GBM-00320_21', 
    'UPENN-GBM-00321_11', 
    'UPENN-GBM-00323_11', 
    'UPENN-GBM-00324_11', 
    'UPENN-GBM-00325_11', 
    'UPENN-GBM-00329_11', 
    'UPENN-GBM-00332_21', 
    'UPENN-GBM-00334_11', 
    'UPENN-GBM-00335_11', 
    'UPENN-GBM-00337_11', 
    'UPENN-GBM-00338_11', 
    'UPENN-GBM-00340_11', 
    'UPENN-GBM-00344_21', 
    'UPENN-GBM-00345_11', 
    'UPENN-GBM-00346_11', 
    'UPENN-GBM-00348_11', 
    'UPENN-GBM-00349_11', 
    'UPENN-GBM-00350_11', 
    'UPENN-GBM-00352_11', 
    'UPENN-GBM-00352_21', 
    'UPENN-GBM-00353_11', 
    'UPENN-GBM-00354_11', 
    'UPENN-GBM-00354_21', 
    'UPENN-GBM-00355_11', 
    'UPENN-GBM-00358_11', 
    'UPENN-GBM-00359_11', 
    'UPENN-GBM-00361_11', 
    'UPENN-GBM-00363_11', 
    'UPENN-GBM-00364_11', 
    'UPENN-GBM-00365_11', 
    'UPENN-GBM-00369_11', 
    'UPENN-GBM-00370_11', 
    'UPENN-GBM-00372_11', 
    'UPENN-GBM-00374_11', 
    'UPENN-GBM-00377_11', 
    'UPENN-GBM-00378_11', 
    'UPENN-GBM-00379_11', 
    'UPENN-GBM-00381_11', 
    'UPENN-GBM-00382_11', 
    'UPENN-GBM-00385_11', 
    'UPENN-GBM-00386_11', 
    'UPENN-GBM-00389_11', 
    'UPENN-GBM-00394_11', 
    'UPENN-GBM-00395_11', 
    'UPENN-GBM-00397_11', 
    'UPENN-GBM-00399_11', 
    'UPENN-GBM-00400_11', 
    'UPENN-GBM-00403_11', 
    'UPENN-GBM-00405_11', 
    'UPENN-GBM-00407_11', 
    'UPENN-GBM-00408_11', 
    'UPENN-GBM-00409_11', 
    'UPENN-GBM-00410_11', 
    'UPENN-GBM-00411_11', 
    'UPENN-GBM-00412_11', 
    'UPENN-GBM-00413_11', 
    'UPENN-GBM-00415_11', 
    'UPENN-GBM-00416_11', 
    'UPENN-GBM-00419_11', 
    'UPENN-GBM-00421_11', 
    'UPENN-GBM-00422_11', 
    'UPENN-GBM-00425_11', 
    'UPENN-GBM-00427_11', 
    'UPENN-GBM-00429_11', 
    'UPENN-GBM-00431_11', 
    'UPENN-GBM-00432_11', 
    'UPENN-GBM-00433_11', 
    'UPENN-GBM-00434_11', 
    'UPENN-GBM-00435_11', 
    'UPENN-GBM-00436_11', 
    'UPENN-GBM-00442_11', 
    'UPENN-GBM-00443_11', 
    'UPENN-GBM-00445_11', 
    'UPENN-GBM-00446_11', 
    'UPENN-GBM-00447_11', 
    'UPENN-GBM-00448_11', 
    'UPENN-GBM-00449_11', 
    'UPENN-GBM-00450_11', 
    'UPENN-GBM-00451_11', 
    'UPENN-GBM-00453_11', 
    'UPENN-GBM-00454_11', 
    'UPENN-GBM-00455_11', 
    'UPENN-GBM-00456_11', 
    'UPENN-GBM-00457_11', 
    'UPENN-GBM-00458_11', 
    'UPENN-GBM-00459_11', 
    'UPENN-GBM-00460_11', 
    'UPENN-GBM-00461_11', 
    'UPENN-GBM-00462_11', 
    'UPENN-GBM-00463_11', 
    'UPENN-GBM-00464_11', 
    'UPENN-GBM-00465_11', 
    'UPENN-GBM-00466_11', 
    'UPENN-GBM-00467_11', 
    'UPENN-GBM-00468_11', 
    'UPENN-GBM-00469_11', 
    'UPENN-GBM-00470_11', 
    'UPENN-GBM-00471_11', 
    'UPENN-GBM-00472_11', 
    'UPENN-GBM-00473_11', 
    'UPENN-GBM-00475_11', 
    'UPENN-GBM-00477_11', 
    'UPENN-GBM-00490_11', 
    'UPENN-GBM-00491_11', 
    'UPENN-GBM-00496_11', 
    'UPENN-GBM-00499_11', 
    'UPENN-GBM-00502_11', 
    'UPENN-GBM-00504_11', 
    'UPENN-GBM-00505_11', 
    'UPENN-GBM-00508_11', 
    'UPENN-GBM-00514_11', 
    'UPENN-GBM-00516_11', 
    'UPENN-GBM-00518_11', 
    'UPENN-GBM-00520_11', 
    'UPENN-GBM-00521_11', 
    'UPENN-GBM-00523_11', 
    'UPENN-GBM-00526_11', 
    'UPENN-GBM-00529_11', 
    'UPENN-GBM-00533_11', 
    'UPENN-GBM-00534_11', 
    'UPENN-GBM-00535_11', 
    'UPENN-GBM-00538_11', 
    'UPENN-GBM-00541_11', 
    'UPENN-GBM-00543_11', 
    'UPENN-GBM-00545_11', 
    'UPENN-GBM-00546_11', 
    'UPENN-GBM-00550_11', 
    'UPENN-GBM-00551_11', 
    'UPENN-GBM-00553_11', 
    'UPENN-GBM-00556_11', 
    'UPENN-GBM-00559_11', 
    'UPENN-GBM-00560_11', 
    'UPENN-GBM-00561_11', 
    'UPENN-GBM-00565_11', 
    'UPENN-GBM-00566_11', 
    'UPENN-GBM-00567_11', 
    'UPENN-GBM-00568_11', 
    'UPENN-GBM-00569_11', 
    'UPENN-GBM-00572_11', 
    'UPENN-GBM-00577_11', 
    'UPENN-GBM-00578_11', 
    'UPENN-GBM-00582_11', 
    'UPENN-GBM-00583_11', 
    'UPENN-GBM-00587_11', 
    'UPENN-GBM-00588_11', 
    'UPENN-GBM-00592_11', 
    'UPENN-GBM-00593_11', 
    'UPENN-GBM-00594_11', 
    'UPENN-GBM-00596_11', 
    'UPENN-GBM-00597_11', 
    'UPENN-GBM-00599_11', 
    'UPENN-GBM-00600_11', 
    'UPENN-GBM-00601_11', 
    'UPENN-GBM-00602_11', 
    'UPENN-GBM-00603_11', 
    'UPENN-GBM-00606_11', 
    'UPENN-GBM-00607_11', 
    'UPENN-GBM-00611_11', 
    'UPENN-GBM-00612_21', 
    'UPENN-GBM-00613_21', 
    'UPENN-GBM-00614_21', 
    'UPENN-GBM-00616_21', 
    'UPENN-GBM-00617_21', 
    'UPENN-GBM-00618_21', 
    'UPENN-GBM-00619_21', 
    'UPENN-GBM-00620_21', 
    'UPENN-GBM-00621_21', 
    'UPENN-GBM-00622_21', 
    'UPENN-GBM-00623_21', 
    'UPENN-GBM-00624_21', 
    'UPENN-GBM-00626_21', 
    'UPENN-GBM-00627_21', 
    'UPENN-GBM-00629_21', 
    'UPENN-GBM-00630_21'
]

triotim3 = triotim3_with_segm + triotim3_without_segm


verio_with_segm = [
    'UPENN-GBM-00083_11', 
    'UPENN-GBM-00119_11', 
    'UPENN-GBM-00137_11', 
    'UPENN-GBM-00151_11', 
    'UPENN-GBM-00238_11', 
    'UPENN-GBM-00240_11', 
    'UPENN-GBM-00285_11', 
    'UPENN-GBM-00307_11', 
    'UPENN-GBM-00428_11'
]

verio_without_segm = [
    'UPENN-GBM-00072_11', 
    'UPENN-GBM-00078_11', 
    'UPENN-GBM-00090_11', 
    'UPENN-GBM-00127_11', 
    'UPENN-GBM-00129_11', 
    'UPENN-GBM-00130_21', 
    'UPENN-GBM-00160_21', 
    'UPENN-GBM-00161_11', 
    'UPENN-GBM-00182_11', 
    'UPENN-GBM-00234_11', 
    'UPENN-GBM-00235_11', 
    'UPENN-GBM-00236_11', 
    'UPENN-GBM-00242_11', 
    'UPENN-GBM-00244_11', 
    'UPENN-GBM-00247_11', 
    'UPENN-GBM-00278_11', 
    'UPENN-GBM-00280_21', 
    'UPENN-GBM-00287_11', 
    'UPENN-GBM-00293_11', 
    'UPENN-GBM-00301_21', 
    'UPENN-GBM-00302_11', 
    'UPENN-GBM-00308_11', 
    'UPENN-GBM-00314_11', 
    'UPENN-GBM-00328_11', 
    'UPENN-GBM-00332_11', 
    'UPENN-GBM-00366_11', 
    'UPENN-GBM-00417_11', 
    'UPENN-GBM-00420_11', 
    'UPENN-GBM-00426_11', 
    'UPENN-GBM-00444_11', 
    'UPENN-GBM-00492_11', 
    'UPENN-GBM-00525_11', 
    'UPENN-GBM-00528_11', 
    'UPENN-GBM-00549_11', 
    'UPENN-GBM-00552_11', 
    'UPENN-GBM-00564_11', 
    'UPENN-GBM-00615_21', 
    'UPENN-GBM-00625_21', 
    'UPENN-GBM-00628_21'
]

verio = verio_with_segm + verio_without_segm


if __name__ == '__main__':
    from natsort import natsorted
    
    segm_root = r'G:\datasets\Brain\images_segm'
    names = os.listdir(segm_root)
    names = [name[:-12] for name in names]

    names_with_segm = []
    names_without_segm = []
    for n in natsorted(triotim3):
        if n in names:
            names_with_segm.append(n)
        else:
            names_without_segm.append(n)
    
    print(names_with_segm)
    print('\n\n\n')
    print(names_without_segm)
    