#<code class="language-java">
import os    
import shutil   
import pdb
  



def img_cp(new_path,paths):
    if not os.path.exists(new_path):
            os.makedirs(new_path)

    for path in paths:
             
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
                os.system('cp '+'\''+file_path+'\''+' '+'\''+new_path+'\'')    
                #shutil.copy(file_path,new_file_path)
                #pdb.set_trace()######### 
        #yn_close = input('是否退出？')</code>  

paths = ['/home/xia/1-huafei/tianchi/bu/new_bu_dataset/train_imgs_process2/train_imgs_process3/randomColor']
#path = '/home/xia/huafei/tianchi/bu/new_bu_dataset/rc_train_labels'
new_path = '/home/xia/1-huafei/tianchi/xbu/tf-faster-rcnn/bu_dataset/VOC2007/JPEGImages'

img_cp(new_path,paths)
