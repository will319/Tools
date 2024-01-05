import os
import shutil

i = 0
split = 'test'

# root_path = '/scratch/184/UnderWater21/VOC2007'
# /scratch/184/sonar2021/VOC2007
img_filepath = 'D:/UnderwaterDet/a3090/imgBlue'
# ann_filepath = os.path.join(root_path, 'Annotations')

img_savepath = 'D:/UnderwaterDet/a3090/testBlue'
# /scratch/181/zqx/_AnchorFree/pytorch_simple_CenterNet_45-Orginal/data/coco/
list_file = 'D:/UnderwaterDet/a3090/VOCx1000/ImageSets/Main/test.txt'
with open(list_file, 'r', encoding='utf-8')as f:
    lines = f.read().split()
    for file in lines:
        # print(file)
        name_img = img_filepath + '/' + file + ".bmp"
        shutil.copy(name_img, img_savepath)
        i += 1
print(i)