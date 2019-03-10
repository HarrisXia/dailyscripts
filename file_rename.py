# -*- coding=utf-8 -*- 
import os
import shutil
import math  
import re
import pdb


#file_dir = './da_li/2017-10-30/2014'



file_dir = '/home/xia/0-github/2-fusion/xiahan/GAN/fusiondata/trainA'

    
def file_name(file_dir):
    #newnames = ['rt_90_','rt_180_','rt_270_','aug_']
    newnames = ['VIS']

    for newname in newnames:
        rename_dir = '/home/xia/0-github/2-fusion/xiahan/GAN/fusiondata/trainA'
    
        new_path = rename_dir
        if not os.path.exists(rename_dir):
            os.makedirs(rename_dir)

        path = file_dir
        for root, dirs, files in os.walk(path):
            #os.path.join(dirpath, dirnames)
            print(root)
            #print(dirs)
            files.sort()
            print(files)
            for file_name in files:
                #print(files[i])  
                #if (files[i][-3:] == 'jpg') or (files[i][-3:] == 'png') or (files[i][-3:] == 'JPG'):     
                file_path = root+'/'+file_name  
                new_file_path = new_path+ '/'+ file_name
                #os.system('cp '+'\''+file_path+'\''+' '+'\''+new_path+'\'')    
        #os.system('cp -r '+'\''+file_dir+'\''+' '+'\''+rename_dir+'\'')


        

        for root, dirs, files in os.walk(new_path):
            #os.path.join(dirpath, dirnames)
            #print(root)
            #print(dirs)
            files.sort()
            print(files)
            
    #############def rename()################
            count = 0           #file count of /multi_dataset
            os.chdir(new_path)
            for file_name in files:
        ##########split the filepath, filename and extension##########
                file_path = new_path+"/"+file_name
                (filepath,tempfilename) = os.path.split(file_path)
                (filename,extension) = os.path.splitext(tempfilename)
                #intfilename = re.sub("\D", "", filename)
                #intfilename = int(intfilename)
                #print(filename)
        
        ###########split the parts of filename to list############
                #new_names = filename.split("1104_")
                #print(new_names[1])
                #os.rename(file_name, new_names[1]+".jpg") 
        
        ###########re lib try by myself################
                #new_name = re.sub(r'^(\_20171030)*', "", filename)
                name_splict = re.split(r'(2018.06.)\s*',file_name)
                #pdb.set_trace()#########
                #new_name = newname+file_name
                #new_name = newname+name_splict[2]
        ##########for yolo train###################
                #sp_dot = re.split(r'[ ||.]',file_name) 
                sp_dot = re.split(r'[.]',file_name) 
                #sp = re.split(r'[.|| ]',file_name)
                #new_name = '_'.join(sp[0:4])+'.jpg'
                #new_name = '_'.join(sp_dot[:-1])+'.jpg'
                #pdb.set_trace()
        ########rename to form of 'x_y'###########
                x = count + 1
                #x = x // 2
                #y = count % 2 + 1
                #new_name = str(math.floor(x)) + '_' + str(y)
                #new_name = str(math.floor(x))+'.bmp'
                #print(sp_dot[1])
                new_name = 'A_'+str(math.floor(x))+'.'+sp_dot[1]
        
                print(new_name)
                
                os.rename(file_name, new_name)
        
                count += 1
    
file_name(file_dir)
    #rename()
        