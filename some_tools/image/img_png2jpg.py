# coding=UTF-8
import numpy as np  
import os, os.path  
import cv2  
import os

path=os.path.abspath('.')
dir_name='D_VOC2007_NYUD2'
path=os.path.join(path,dir_name)

for images in os.listdir(path):
    #if header in images:
    rgb = cv2.imread(path+'/'+images, -1)
    images_unit=images.split('.')
    images_name=images_unit[0]
    print images_name
    cv2.imwrite('/home/guan/RGBD/VOC2007_D/%s.jpg' % images_name, rgb,[int( cv2.IMWRITE_JPEG_QUALITY), 100]) 