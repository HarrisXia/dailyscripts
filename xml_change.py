# -*- coding=utf-8 -*- 

import os
import shutil
import math  
import re
import pdb


def class2err(file_dir):
    for root, dirs, files in os.walk(file_dir):
        #os.path.join(dirpath, dirnames)
        print(root)
        print(dirs)
        files.sort()
        print(files)

    os.chdir(file_dir)
    for file_name in files:
        f=open(file_name,'r+')
        flist=f.readlines()
        for line in flist:
            #pdb.set_trace()################
            flist[1] = '\t<filename>'+re.split(r'(.xml)\s*',file_name)[0]+'.jpg</filename>\n'
            #p = re.compile(">0<")
            #if not p.search(line) is None:
                #pdb.set_trace()##############
            for label_num in range(20):
                label_num +=1
                labels = 12*label_num
                #pdb.set_trace()#############
                if len(flist) > labels:
                    flist[labels] = '\t\t<name>err</name>\n'
        f=open(file_name,'w+')
        #pdb.set_trace()#########
        f.writelines(flist)


def rt_bbx_change(file_dir):

    for root, dirs, files in os.walk(file_dir):
        #os.path.join(dirpath, dirnames)
        print(root)
        print(dirs)
        files.sort()
        print(files)

    os.chdir(file_dir)
    for file_name in files:
        bbx = {}
        f=open(file_name,'r+')
        flist=f.readlines()
        for label_num in range(20):
            labels = 12*label_num + 17
            
            #pdb.set_trace()#############
            if len(flist) > labels:
                for i in range(4):
                    p = re.compile(">0<")
                    #if not p.search(flist[labels+i]) is None:
                        #pdb.set_trace()#########
                    line_split = re.split(r'(>|<)\s*',flist[labels+i])
                    bbx[line_split[2]] = line_split[4]
###########rc_90_################
                
                if re.split(r'(J01)\s*',file_name)[0]=='rt_90_':
                    flist[labels]='\t\t\t<xmin>'+str(bbx['ymin'])+'</xmin>\n'                   
                    flist[labels+1]='\t\t\t<ymin>'+str(2560-int(bbx['xmax']))+'</ymin>\n'                    
                    flist[labels+2]='\t\t\t<xmax>'+str(bbx['ymax'])+'</xmax>\n'
                    flist[labels+3]='\t\t\t<ymax>'+str(2560-int(bbx['xmin']))+'</ymax>\n'
                    if int(bbx['ymin']) == 0:
                        flist[labels]='\t\t\t<xmin>1</xmin>\n'
                    if int(bbx['xmax']) == 2560:
                        flist[labels+1]='\t\t\t<ymin>1</ymin>\n'
                    if int(bbx['ymax']) == 0:
                        flist[labels+2]='\t\t\t<xmax>1</xmax>\n'
                    if int(bbx['xmin']) == 2560:
                        flist[labels+3]='\t\t\t<ymax>1</ymax>\n'
                if re.split(r'(J01)\s*',file_name)[0]=='rt_180_':
                    flist[labels]='\t\t\t<xmin>'+str(2560-int(bbx['xmax']))+'</xmin>\n'
                    flist[labels+1]='\t\t\t<ymin>'+str(1920-int(bbx['ymax']))+'</ymin>\n'
                    flist[labels+2]='\t\t\t<xmax>'+str(2560-int(bbx['xmin']))+'</xmax>\n'
                    flist[labels+3]='\t\t\t<ymax>'+str(1920-int(bbx['ymin']))+'</ymax>\n'
                    if int(bbx['xmax']) == 2560:
                        flist[labels]='\t\t\t<xmin>1</xmin>\n'
                    if 1920-int(bbx['ymax']) ==0:
                        flist[labels+1]='\t\t\t<ymin>1</ymin>\n'
                    if 2560-int(bbx['xmin']) == 0:
                        flist[labels+2]='\t\t\t<xmax>1</xmax>\n'
                    if 1920-int(bbx['ymin']) == 0:
                        flist[labels+3]='\t\t\t<ymax>1</ymax>\n'
                if re.split(r'(J01)\s*',file_name)[0]=='rt_270_':
                    flist[labels]='\t\t\t<xmin>'+str(1920-int(bbx['ymax']))+'</xmin>\n'
                    flist[labels+1]='\t\t\t<ymin>'+str(bbx['xmin'])+'</ymin>\n'
                    flist[labels+2]='\t\t\t<xmax>'+str(1920-int(bbx['ymin']))+'</xmax>\n'
                    flist[labels+3]='\t\t\t<ymax>'+str(bbx['xmax'])+'</ymax>\n'
                    if 1920-int(bbx['ymax']) == 0:
                        flist[labels]='\t\t\t<xmin>1</xmin>\n'
                    if int(bbx['xmin']) == 0:
                        flist[labels+1]='\t\t\t<ymin>1</ymin>\n'
                    if 1920-int(bbx['ymin']) == 0:
                        flist[labels+2]='\t\t\t<xmax>1</xmax>\n'
                    if  int(bbx['xmax']) == 0:
                        flist[labels+3]='\t\t\t<ymax>1</ymax>\n'
                #pdb.set_trace()###########
        f=open(file_name,'w+')
        
        f.writelines(flist)

file_dir = '/home/xia/1-huafei/tianchi/bu/bu_dataset/bu_new_labels/bu_new_labels'
#class2err(file_dir)
rt_bbx_change(file_dir)