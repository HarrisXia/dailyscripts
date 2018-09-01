#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy
import os
from PIL import Image

def PIL_gray(img):

    im = Image.open(img)
    im.show()

######img2arrar
    im_array = numpy.array(im)

######rgb2gray
    L = im.convert('L')   #转化为灰度图
    #L = im.convert('1')   #转化为二值化图
    L.show()
    (filepath,tempfilename) = os.path.split(img)
    (filename,extension) = os.path.splitext(tempfilename)
    cur_dir = os.getcwd()
    L.save('new'+tempfilename)

print("keyword:please input the origin file")
img = input()
PIL_gray(img)