#coding=utf-8
import os
import skimage
import io
import matplotlib.pyplot as plt
from PIL import Image,ImageEnhance
from PIL import ImageChops
import cv2
import pdb
import numpy as np
import skimage.io
import random

global ori_dir,dst_dir,count

def main():
    for root, dirs, files in os.walk(ori_dir):
        #os.path.join(dirpath, dirnames)
        print(root)
        #print(dirs)
        files.sort()
        print(files)
    count=0
    for file_name in files:
        count+=1
        pepper(file_name,6000)#pepper_num
        #flip(file_name)
        #move(file_name,500,500)#zuo1,zuo2
        aj_contrast(file_name)
        rotate_bound(file_name,90)
        rotate_bound(file_name,180)
        rotate_bound(file_name,270)
        randomGaussian(file_name, 0, 25)#mean and gamma
        randomColor(file_name)
        print("\t"+str(count)+"\timgs done")
        #pdb.set_trace()###############
        

def dst_file_saver(dst,dst_dir,newname,enhance_type):
    if not os.path.exists(dst_dir+"/"+enhance_type):
        os.makedirs(dst_dir+"/"+enhance_type)
    dst.save(newname)        

def pepper(file_name,pepper_num):
    enhance_type = "pepper"
    oldname=ori_dir+file_name
    img=np.array(Image.open(oldname)) 
    #随机生成pepper_num个椒盐
    rows,cols,dims=img.shape
    for i in range(pepper_num):
        x=np.random.randint(0,rows)
        y=np.random.randint(0,cols)
        img[x,y,:]=255
    img.flags.writeable = True  # 将数组改为读写模式
    dst=Image.fromarray(np.uint8(img))
    newname=dst_dir+"/"+enhance_type+"/pp_"+str(pepper_num)+'_'+file_name
    dst_file_saver(dst,dst_dir,newname,enhance_type)

def flip(file_name):
    enhance_type = "flip"
    img = Image.open(os.path.join(ori_dir, file_name))
    dst=img.transpose(Image.FLIP_LEFT_RIGHT)#左右互换
    newname=dst_dir+"/"+enhance_type+"/fz_"+file_name
    dst_file_saver(dst,dst_dir,newname,enhance_type)

def move(file_name,zuo1,zuo2): 
    enhance_type = "move"
    img = Image.open(os.path.join(ori_dir, file_name))
    dst = ImageChops.offset(img,zuo1,zuo2)
    newname=dst_dir+enhance_type+'/'+"_mv_"+str(zuo1)+'_'+str(zuo2)+'_'+file_name
    dst_file_saver(dst,dst_dir,newname,enhance_type)

def aj_contrast(file_name): 
    enhance_type = "aj_contrast"
    img = Image.open(os.path.join(ori_dir, file_name))
    image = skimage.io.imread(os.path.join(ori_dir, file_name))
    gam = skimage.exposure.adjust_gamma(image, 0.5)
    log = skimage.exposure.adjust_log(image)
    gamname=dst_dir+enhance_type+"/gm_"+file_name
    logname=dst_dir+enhance_type+"/lg_"+file_name
    dst_file_saver(img,dst_dir,gamname,enhance_type)
    dst_file_saver(img,dst_dir,logname,enhance_type)
    skimage.io.imsave(gamname,gam)
    skimage.io.imsave(logname,log)
    

    

def rotate_bound(file_name, angle):
    # grab the dimensions of the image and then determine the
    # center
    enhance_type = "rotation"+str(360-angle)
    image = cv2.imread(os.path.join(ori_dir, file_name))
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
 
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
 
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
 
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
 
    # perform the actual rotation and return the image
    dst = cv2.warpAffine(image, M, (nW, nH))
    newname=dst_dir+"/"+enhance_type+"/rt_"+str(360-angle)+'_'+file_name
    if not os.path.exists(dst_dir+"/"+enhance_type):
        os.makedirs(dst_dir+"/"+enhance_type)
    cv2.imwrite(newname,dst)
    #pdb.set_trace()##############



def randomGaussian(file_name, mean, sigma):
    root_path = ori_dir
    enhance_type = "randomGaussian"
    im = np.array(Image.open(os.path.join(ori_dir, file_name)))

    #r通道
    r = im[:,:,0].flatten()
    #g通道
    g = im[:,:,1].flatten()
    #b通道
    b = im[:,:,2].flatten()
    #计算新的像素值
    for i in range(im.shape[0]*im.shape[1]):
        pr = int(r[i]) + random.gauss(0,sigma)
        pg = int(g[i]) + random.gauss(0,sigma)
        pb = int(b[i]) + random.gauss(0,sigma)
        if(pr < 0):
            pr = 0
        if(pr > 255):
            pr = 255
        if(pg < 0):
            pg = 0
        if(pg > 255):
            pg = 255
        if(pb < 0):
            pb = 0
        if(pb > 255):
            pb = 255
        r[i] = pr
        g[i] = pg
        b[i] = pb
    im[:,:,0] = r.reshape([im.shape[0],im.shape[1]])
    im[:,:,1] = g.reshape([im.shape[0],im.shape[1]])
    im[:,:,2] = b.reshape([im.shape[0],im.shape[1]])
    dst = gaussian_image = Image.fromarray(np.uint8(im))
    newname=dst_dir+"/"+enhance_type+"/gs_"+file_name
    dst_file_saver(dst,dst_dir,newname,enhance_type)


def randomColor(file_name):
    """
    对图像进行颜色抖动
    :param image: PIL的图像image
    :return: 有颜色色差的图像image
    """
    enhance_type = "randomColor"
    image = Image.open(os.path.join(ori_dir, file_name))
    random_factor = np.random.randint(0, 31) / 10.  # 随机因子
    color_image = ImageEnhance.Color(image).enhance(random_factor)  
    # 调整图像的饱和度
    random_factor = np.random.randint(10, 21) / 10.  # 随机因子
    brightness_image = ImageEnhance.Brightness(color_image).enhance(random_factor)  
    # 调整图像的亮度
    random_factor = np.random.randint(10, 21) / 10.  # 随机因子
    contrast_image = ImageEnhance.Contrast(brightness_image).enhance(random_factor)  
    # 调整图像对比度
    random_factor = np.random.randint(0, 31) / 10.  # 随机因子
    dst = ImageEnhance.Sharpness(contrast_image).enhance(random_factor)  
    # 调整图像锐度
    newname=dst_dir+"/"+enhance_type+"/rc_"+file_name
    dst_file_saver(dst,dst_dir,newname,enhance_type)


def data_augment(ori_dir,dst_dir):
    for root, dirs, files in os.walk(ori_dir):
        #os.path.join(dirpath, dirnames)
        print(root)
        #print(dirs)
        files.sort()
        print(files)
    count=0
    for file_name in files:
        count+=1
        ##############pepper####################
        oldname=ori_dir+file_name
        newname=dst_dir+'aug_'+file_name
        img=np.array(Image.open(oldname)) 
        #随机生成pepper_num个椒盐
        rows,cols,dims=img.shape
        for i in range(4500):
            x=np.random.randint(0,rows)
            y=np.random.randint(0,cols)
            img[x,y,:]=255
        img.flags.writeable = True  # 将数组改为读写模式
        dst = Image.fromarray(np.uint8(img))
        dst.save(newname)

        ##############randomGaussian#################
        sigma = 0.2
        #im=img
        #r = im[:,:,0].flatten()#r通道
        #g = im[:,:,1].flatten()#g通道
        #b = im[:,:,2].flatten()#b通道
        #for i in range(im.shape[0]*im.shape[1]):#计算新的像素值
        #    pr = int(r[i]) + random.gauss(0,sigma)
        #    pg = int(g[i]) + random.gauss(0,sigma)
        #    pb = int(b[i]) + random.gauss(0,sigma)
        #    if(pr < 0):
        #        pr = 0
        #    if(pr > 255):
        #        pr = 255
        #    if(pg < 0):
        #        pg = 0
        #    if(pg > 255):
        #        pg = 255
        #    if(pb < 0):
        #        pb = 0
        #    if(pb > 255):
        #        pb = 255
        #    r[i] = pr
        #    g[i] = pg
        #    b[i] = pb
        #im[:,:,0] = r.reshape([im.shape[0],im.shape[1]])
        #im[:,:,1] = g.reshape([im.shape[0],im.shape[1]])
        #im[:,:,2] = b.reshape([im.shape[0],im.shape[1]])
        #dst = gaussian_image = Image.fromarray(np.uint8(im))
        #dst.save(newname)

        ##############random color####################
        #对图像进行颜色抖动
        #:param image: PIL的图像image
        #:return: 有颜色色差的图像image
        #image = Image.open(newname)
        #random_factor = np.random.randint(0, 51) / 10.  # 随机因子
        #color_image = ImageEnhance.Color(image).enhance(random_factor)  
        ## 调整图像的饱和度
        #random_factor = np.random.randint(10, 11) / 10.  # 随机因子
        #brightness_image = ImageEnhance.Brightness(color_image).enhance(random_factor)  
        ## 调整图像的亮度
        #random_factor = np.random.randint(10, 31) / 10.  # 随机因子
        #contrast_image = ImageEnhance.Contrast(brightness_image).enhance(random_factor)  
        ## 调整图像对比度
        #random_factor = np.random.randint(0, 41) / 10.  # 随机因子
        #final_img = ImageEnhance.Sharpness(contrast_image).enhance(random_factor)  
        ## 调整图像锐度
        #dst=Image.fromarray(np.uint8(final_img))
        #dst.save(newname)
    
        ##############aj_contrast######################
        #image = skimage.io.imread(newname)
        #gam = skimage.exposure.adjust_gamma(image, 0.5)        
        #skimage.io.imsave(newname,gam)
        #image = skimage.io.imread(newname)
        #log = skimage.exposure.adjust_log(image)
        #skimage.io.imsave(newname)

        ##############rotate########################
            # grab the dimensions of the image and then determine the center
        for angle in [90,180,270]:
            enhance_type = "rotation"+str(360-angle)
            image = cv2.imread(oldname)
            (h, w) = image.shape[:2]
            (cX, cY) = (w // 2, h // 2)
            # grab the rotation matrix (applying the negative of the
            # angle to rotate clockwise), then grab the sine and cosine
            # (i.e., the rotation components of the matrix)
            M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
            cos = np.abs(M[0, 0])
            sin = np.abs(M[0, 1])
            # compute the new bounding dimensions of the image
            nW = int((h * sin) + (w * cos))
            nH = int((h * cos) + (w * sin))
            # adjust the rotation matrix to take into account translation
            M[0, 2] += (nW / 2) - cX
            M[1, 2] += (nH / 2) - cY
            # perform the actual rotation and return the image
            dst = cv2.warpAffine(image, M, (nW, nH))
            newname=dst_dir+"/rt_"+str(360-angle)+'_'+file_name
            if not os.path.exists(dst_dir+"/"+enhance_type):
                os.makedirs(dst_dir+"/"+enhance_type)
            cv2.imwrite(newname,dst)

        print("\t"+str(count)+"\timgs done")



ori_dir = '/home/xia/1-huafei/tianchi/bu/fs/666/'
dst_dir = '/home/xia/1-huafei/tianchi/bu/fs/666/'
#main()
data_augment(ori_dir,dst_dir)