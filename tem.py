from PIL import Image
# import scipy
import matplotlib.pyplot as plt
import numpy as np
import re
import scipy.misc
import pdb
import random
#import cv2
import scipy.signal as signal


def del_redunparts(del_file):
    with open(del_file, "r+") as f:
        lines = f.readlines()
        line_list =['' for n in range(len(lines))]
        count = 0
        splict_line = re.split(r'[ ]',lines[0])
        splict_line.remove('')
        numbers = list(map(float, splict_line))
        
        numbers = np.array(numbers).reshape(320,240)
        print(numbers)
        pdb.set_trace()#################
        data=numbers
        data1 = signal.medfilt(data,3)
        new_im = MatrixToImage(data)
        plt.imshow(data, cmap=plt.cm.gray)
        new_im = MatrixToImage(data1)
        plt.imshow(data1, cmap=plt.cm.gray)
        new_im.show()
        scipy.misc.imsave('meelo.jpg', data)



#def ImageToMatrix(filename):
#    # 读取图片
#    im = Image.open(filename)
#    # 显示图片
##     im.show()  
#    width,height = im.size
#    im = im.convert("L") 
#    data = im.getdata()
#    data = np.matrix(data,dtype=‘float‘)/255.0
#    #new_data = np.reshape(data,(width,height))
#    new_data = np.reshape(data,(height,width))
#    return new_data
##     new_im = Image.fromarray(new_data)
##     # 显示图片
##     new_im.show()
def MatrixToImage(data):
    data = data*255
    new_im = Image.fromarray(data.astype(np.uint8))
    return new_im



#filename = ‘lena.jpg‘
#data = ImageToMatrix(filename)
#print data 


del_file = "/home/xia/2-datasets/1.txt"
del_redunparts(del_file)