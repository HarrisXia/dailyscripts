# coding=UTF-8
import numpy as np  
import os, os.path  
import cv2  
import matplotlib.pyplot as plt

  
import os
import cv2
path=os.path.abspath('.')
dir_name='VOC2007'
path=os.path.join(path,dir_name)

for images in os.listdir(path):
    #if header in images:
    rgb = cv2.imread(path+'/'+images, -1)
    sp = rgb.shape
    print sp
    images_unit=images.split('.')
    images_name=images_unit[0]
    disp= cv2.imread('/home/guan/RGBD/depth_colorization/'+images_name+'.png', -1)
    sp = disp.shape
    print sp
    rgb = np.array(rgb)  
    disp = np.array(disp)  
    #combine  
    rgbd = np.zeros((sp[0],sp[1],4),dtype=np.uint8)  
    rgbd[:, :, 0] = rgb[:, :, 0]  
    rgbd[:, :, 1] = rgb[:, :, 1]  
    rgbd[:, :, 2] = rgb[:, :, 2]  
    rgbd[:, :, 3] = disp  
    dim = rgbd.shape
    print dim
    cv2.imwrite('/home/guan/RGBD/RGBD_VOC2007_NYUD2_GAN_colorization/%s.png' % images_name, rgbd)  
    print ("-----------------------------------") 
print ("success")