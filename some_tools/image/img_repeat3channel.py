import os
import cv2
import numpy as np
from utils import mkdir_if_not_exist
rootpath='/usr/guandai/birdnest400+/datasets/VOC2007/VOC2007/'
sourcename='JPEGImages_depth'
sourcepath=os.path.join(rootpath,sourcename)
targetpath = os.path.join(rootpath,sourcename+'_3channel')
mkdir_if_not_exist(targetpath)

for file in os.listdir(sourcepath):
    img = cv2.imread(os.path.join(sourcepath,file),-1)
    size = img.shape
    img3 = np.zeros((size[0],size[1],3),dtype=np.uint8)
    img3[:,:,0] = img
    img3[:,:,1] = img
    img3[:,:,2] = img
    cv2.imwrite(os.path.join(targetpath,file), img3)

