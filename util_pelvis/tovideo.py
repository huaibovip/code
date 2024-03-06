import os
import cv2
import numpy as np

root = r'G:/datasets/Pelvis/Gold-Atlas/data/png_dst/train'
names = os.listdir(root)

idx = 0
path = os.path.join(root, names[0])
filelist = os.listdir(path)

fps = 12 #视频每秒24帧
# size = (640, 480) #需要转为视频的图片的尺寸
size = (1024, 512)
#可以使用cv2.resize()进行修改

video = cv2.VideoWriter(f"{names[idx]}.mp4", cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, size)
#视频保存在当前目录下

for item in filelist:
    if item.endswith('.png'):
    #找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
        item = os.path.join(path, item)
        img = cv2.imread(item)
        print(img.shape)
        video.write(img)

video.release()
cv2.destroyAllWindows()