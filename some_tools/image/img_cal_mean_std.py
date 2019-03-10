# coding=UTF-8
import os
import cv2
import numpy as np
path='/usr/data/fashionai/base/Images/'
num=0


meanall=np.zeros(3)
stdall=np.zeros(3)
#imgmean=imgstd=np.zeros(3)

for classes in os.listdir(path):
	classname=os.path.join(path,classes)
	for imagename in os.listdir(classname):
		img = cv2.imread(classname+'/'+imagename, -1).astype('Float64')
		rgb_224=img
		#print(rgb_224.shape)
		##calculate mean and std
		normalize_img=rgb_224/255
		for i in range(0,3):
			imgstd=np.std(normalize_img[:,:,i])
			imgmean=np.mean(normalize_img[:,:,i])
			meanall[i]=meanall[i]+imgmean
			stdall[i]=stdall[i]+imgstd
		num=num+1
		#print(num)
print('Mean is %s\t%s\t%s'%(meanall[0]/num,meanall[1]/num,meanall[2]/num))#bgr?
print('The number of images is %s'%num)
print('Std is %s\t%s\t%s'%(stdall[0]/num,stdall[1]/num,stdall[2]/num))
			



			
