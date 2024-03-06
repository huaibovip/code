import monai
from monai import transforms


trans = transforms.Compose([
    transforms.LoadImage(image_only=True, ensure_channel_first=True),
    transforms.ForegroundMask(threshold=0.01, invert=True),
    transforms.SaveImage()
])

path = r'G:\datasets\IXI\raw\IXI-T2\Guys\IXI002-Guys-0828-T2.nii.gz'
data = trans(path)[0]
print(data.shape)
