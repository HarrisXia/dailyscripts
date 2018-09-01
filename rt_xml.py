#!/usr/bin/env python
# coding:utf-8

#from xml.etree.ElementTree import Element, SubElement, tostring
from lxml.etree import Element, SubElement, tostring
import pprint
from xml.dom.minidom import parseString


#! /usr/bin/python
# -*- coding:UTF-8 -*-
import os, sys
import glob
from PIL import Image

defbbx2xml(): 
# VEDAI 图像存储位置
    src_img_dir = "/home/xn/caffe/image/VEDAI/Vehicules1024_new"
    # VEDAI 图像的 ground truth 的 txt 文件存放位置
    src_txt_dir = "/home/xn/caffe/image/VEDAI/Annotations1024_new"
    src_xml_dir = "/home/xn/caffe/image/VEDAI/Annotations1024_xml"
     
    img_Lists = glob.glob(src_img_dir + '/*.png')
     
    img_basenames = [] # e.g. 100.jpg
    for item in img_Lists:
        img_basenames.append(os.path.basename(item))
     
    img_names = [] # e.g. 100
    for item in img_basenames:
        temp1, temp2 = os.path.splitext(item)
        img_names.append(temp1)
     
    for img in img_names:
        im = Image.open((src_img_dir + '/' + img + '.png'))
        width, height = im.size
     
        # open the crospronding txt file
        gt = open(src_txt_dir + '/' + img + '.txt').read().splitlines()
        #gt = open(src_txt_dir + '/gt_' + img + '.txt').read().splitlines()
     
        # write in xml file
        #os.mknod(src_xml_dir + '/' + img + '.xml')
        xml_file = open((src_xml_dir + '/' + img + '.xml'), 'w')
        xml_file.write('<annotation>\n')
        xml_file.write('    <folder>VOC2007</folder>\n')
        xml_file.write('    <filename>' + str(img) + '.png' + '</filename>\n')
        xml_file.write('    <size>\n')
        xml_file.write('        <width>' + str(width) + '</width>\n')
        xml_file.write('        <height>' + str(height) + '</height>\n')
        xml_file.write('        <depth>3</depth>\n')
        xml_file.write('    </size>\n')
     
        # write the region of image on xml file
        for img_each_label in gt:
            spt = img_each_label.split(' ') #这里如果txt里面是以逗号‘，’隔开的，那么就改为spt = img_each_label.split(',')。
            xml_file.write('    <object>\n')
            xml_file.write('        <name>' + str(spt[4]) + '</name>\n')
            xml_file.write('        <pose>Unspecified</pose>\n')
            xml_file.write('        <truncated>0</truncated>\n')
            xml_file.write('        <difficult>0</difficult>\n')
            xml_file.write('        <bndbox>\n')
            xml_file.write('            <xmin>' + str(spt[0]) + '</xmin>\n')
            xml_file.write('            <ymin>' + str(spt[1]) + '</ymin>\n')
            xml_file.write('            <xmax>' + str(spt[2]) + '</xmax>\n')
            xml_file.write('            <ymax>' + str(spt[3]) + '</ymax>\n')
            xml_file.write('        </bndbox>\n')
            xml_file.write('    </object>\n')
     
        xml_file.write('</annotation>')




    
node_root = Element('666')

node_folder = SubElement(node_root, 'folder')
node_folder.text = 'GTSDB'

node_filename = SubElement(node_root, 'filename')
node_filename.text = '000001.jpg'

node_size = SubElement(node_root, 'size')
node_width = SubElement(node_size, 'width')
node_width.text = '500'

node_height = SubElement(node_size, 'height')
node_height.text = '375'

node_depth = SubElement(node_size, 'depth')
node_depth.text = '3'

node_object = SubElement(node_root, 'object')
node_name = SubElement(node_object, 'name')
node_name.text = 'mouse'
node_difficult = SubElement(node_object, 'difficult')
node_difficult.text = '0'
node_bndbox = SubElement(node_object, 'bndbox')
node_xmin = SubElement(node_bndbox, 'xmin')
node_xmin.text = '99'
node_ymin = SubElement(node_bndbox, 'ymin')
node_ymin.text = '358'
node_xmax = SubElement(node_bndbox, 'xmax')
node_xmax.text = '135'
node_ymax = SubElement(node_bndbox, 'ymax')
node_ymax.text = '375'

xml = tostring(node_root, pretty_print=True)  #格式化显示，该换行的换行
dom = parseString(xml)
print (xml)

