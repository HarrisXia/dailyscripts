import os
import shutil
import math  
import re
import random
import pdb


ori_file = './xxx.txt'
target_file = './train.txt' 

count = 0
#while count <= 294:
#a = range(10)
#while a:
#while count <= 2:
target_file_list =['' for n in range(294)]
for count in range(294):
    f1=open(ori_file,'r+')
    ori_file_list=f1.readlines()
    #line_num = random.randint(0,len(ori_file_list))
    num_count = count * 1.752
    line_num = math.floor(num_count)
    #pdb.set_trace()#####################
    target_file_list[count] = ori_file_list[line_num]
    f2=open(target_file,'w+')
    f2.writelines(target_file_list)

    with open(ori_file, 'r') as old_file:
        with open(ori_file, 'r+') as new_file:
            current_line = line_num
            # 定位到需要删除的行
            while current_line < (del_line - 1):
                old_file.readline()
                current_line += 1
            # 当前光标在被删除行的行首，记录该位置
            seek_point = old_file.tell()
            # 设置光标位置
            new_file.seek(seek_point, 0)
            # 读需要删除的行，光标移到下一行行首
            old_file.readline()
            # 被删除行的下一行读给 next_line
            next_line = old_file.readline()
            # 连续覆盖剩余行，后面所有行上移一行
            while next_line:
                new_file.write(next_line)
                next_line = old_file.readline()
            # 写完最后一行后截断文件，因为删除操作，文件整体少了一行，原文件最后一行需要去掉
            new_file.truncate()

    #ori_file_list[line_num] = 'xxxxxxxxx\n'
    #f3=open(ori_file,'w+')
    #f3.writelines(ori_file_list)
    #count += 1
    #a = a[:len(a)-1]


