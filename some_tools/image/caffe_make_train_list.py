# encoding: utf-8
import os  
#path = "/home/guan/data/cifar/train"     
path = "/home/guan/data/cifar/train"  
path_exp = os.path.expanduser(path)
classes = [p for p in os.listdir(path_exp)]  
classes.sort()  
# nrof_classes一个数据集下有多少个文件夹,就是说有多少个人,多少个类别  
nrof_classes = len(classes)  
count=0  
files = open("train.txt",'w')  
#filets = open("test.txt",'w')  
count_u=0  
for i in range(nrof_classes):  
    class_name = str(classes[i])  
    count=count+1  
    count_u=count_u+1  
    facedir = os.path.join(path_exp, class_name)  
    prefix1 = path+class_name+"/"  
  
    if os.path.isdir(facedir):  
        images = os.listdir(facedir)  
        #print(images[0])  
        image_paths = [(class_name+"/"+img+' '+str(i)+'\n') for img in images]  

        #filets.writelines(image_paths)  
        files.writelines(image_paths)  
 
files.close()  
#filets.close()