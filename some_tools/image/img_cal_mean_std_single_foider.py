import os
import cv2
import numpy as np
path='/home/guan/github/depth-estimation/refinenet_resnet50_voc'
num=0

# class Employee:
# 	pass

# imgstd=Employee()
# imgmean=Employee()
# meanall=Employee()
# stdall=Employee()


# meanall=np.zeros(1)
# stdall=np.zeros(1)
meanall=[0]*3
stdall=[0] *3
#imgmean=imgstd=np.zeros(3)


for imagename in os.listdir(path):
	img = cv2.imread(path+'/'+imagename, -1).astype('Float32')
	rgb_224=img
	normalize_img=rgb_224/255
	if len(img.shape) == 2:
		imgstd=np.std(normalize_img)
		imgmean=np.mean(normalize_img)
		meanall=meanall+imgmean
		stdall=stdall+imgstd
	else:
		for i in range(0,3):
			imgstd=np.std(normalize_img[:,:,i])
			imgmean=np.mean(normalize_img[:,:,i])
			meanall[i]=meanall[i]+imgmean
			stdall[i]=stdall[i]+imgstd
	num=num+1
	#print(num)
if len(img.shape) == 2:
	print('Mean is %s'%(meanall/num))
	print('The number of images is %s'%num)
	print('Std is %s'%(stdall/num))
else:
	print('Mean is %s\t%s\t%s'%(meanall[0]/num,meanall[1]/num,meanall[2]/num))
	print('The number of images is %s'%num)
	print('Std is %s\t%s\t%s'%(stdall[0]/num,stdall[1]/num,stdall[2]/num))
			



			
