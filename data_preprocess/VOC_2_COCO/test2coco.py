
"""
Created on Sun Jun 24 16:01:11 2018
对测试数据集生成coco格式
没有annotation
只有图片的信息和categories的信息
@author: wytwh
"""
 
import os
import json
import collections
import cv2 
 
coco = collections.OrderedDict()
coco['images'] = []
coco['type'] = 'instances'
coco['annotations'] = []
coco['categories'] = []
 
image_id = 2020000001 #对每张图片进行编号，初始编号
category_item_id = 1
#classname = ['small-vehicle', 'large-vehicle', 'plane','harbor', 'ship', 
#             'tennis-court', 'soccer-ball-field', 'ground-track-field',
#             'baseball-diamond', 'swimming-pool', 'roundabout', 'basketball-court', 
#             'storage-tank', 'bridge', 'helicopter']#更改为你自己的类别,与voc_2007_train中的一致
classname = ['defect_1', 'defect_2', 'defect_3','defect_4', 'defect_5', 
             'defect_6', 'defect_7', 'defect_8',
             'defect_9', 'defect_10']
 
 
def GetFileFromThisRootDir(dir,ext = None):
  allfiles = []
  needExtFilter = (ext != None)
  for root,dirs,files in os.walk(dir):   #files是文件夹下所有文件的名称
    for filespath in files:            #依次取文件名
      filepath = os.path.join(root, filespath)    #构成绝对路径
      extension = os.path.splitext(filepath)[1][1:]  #os.path.splitext(path)  #分割路径，返回路径名和文件后缀 其中[1]为后缀.png，再取[1:]得到png
      if needExtFilter and extension in ext:
        allfiles.append(filepath)
      elif not needExtFilter:
        allfiles.append(filepath)
  return allfiles   #返回dir中所有文件的绝对路径
 
 
def addCatItem(name):
    '''
    增加json格式中的categories部分
    '''
    global category_item_id
    category_item = collections.OrderedDict()
    category_item['supercategory'] = 'none'
    category_item['id'] = category_item_id
    category_item['name'] = name
    coco['categories'].append(category_item)
    category_item_id += 1
 
def addImgItem(img_name, size):
    '''
    增加json格式中的images部分
    '''
    global image_id
    if img_name is None:
        raise Exception('Could not find Picture file.')
    if size['width'] is None:
        raise Exception('Could not find width.')
    if size['height'] is None:
        raise Exception('Could not find height.')
    #image_item = dict()    #按照一定的顺序，这里采用collections.OrderedDict()
    image_item = collections.OrderedDict()
    image_item['file_name'] = img_name  
    image_item['width'] = size['width']   
    image_item['height'] = size['height']
    image_item['id'] = image_id
    coco['images'].append(image_item) 
    image_id = image_id+1
 
 
def WriteCOCOFiles(pic_path):
    for idx,path in enumerate(pic_path):
        size = {}
        imgname = os.path.basename(path) #得到除去后缀的名字
        img = cv2.imread(path)
        size['height'] = img.shape[0] 
        size['width'] = img.shape[1]  
        addImgItem(imgname, size)
        print('add image with {} and {}'.format(imgname, size))
    for idx, obj in enumerate(classname):
        addCatItem(obj)          
 
 
if __name__ == '__main__':
    pic_dir = '/home/xia/1-huafei/tianchi/bu/fs/fs_test_yolo'    #图片存放的路径
    json_file = '/home/xia/1-huafei/tianchi/bu/coco_json/voc_2007_test.json'  #生成的coco路径
    pic_path = GetFileFromThisRootDir(pic_dir,ext = None)  #每一个图片的路径
    WriteCOCOFiles(pic_path)
json.dump(coco, open(json_file, 'w'))