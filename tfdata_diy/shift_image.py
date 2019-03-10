# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 20:37:11 2018

@author: lele
"""
import sys
import cv2
import math
import numpy as np

class Shift:
    def __init__(self,name):
        self.image = cv2.imread(name)
        cv2.imshow("demo",self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()        
        print(name)

    def light(self,i):
        while(m,n<w,d):
            image = self.image + i
        cv2.imshow("demo",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def contrast(self):
        pass

    def equalize(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        eq = cv2.equalizeHist(image)
        return eq
    
def cur():
    i = 64
    while(i<70):
        try:
            name = "rgb"+str(i)+".jpg"
            
            image_shift = Shift(name)
            image_shift.light(10)
            i += 1
        except IOError:
            print("Error: object() takes no parameters")

def png_to_jpg_sorting():
    i = 1
    j = 1
    temp_image = None
    while(i<400):
        try:
            name = "rgb"+str(i)+".png"
            temp_image = cv2.imread(name)
            if(temp_image is not None):
                temp_name = "rgb"+str(j)+".jpg"
                cv2.imwrite(temp_name,temp_image)
                j += 1
                temp_image = None
            i += 1
        except IOError:
            print("Error:没文件")
            

def jpg_to_png_sorting():
    i = 1
    j = 1
    temp_image = None
    while(i<400):
        try:
            name = "rgb"+str(i)+".jpg"
            temp_image = cv2.imread(name)
            if(temp_image is not None):
                temp_name = "rgb"+str(j)+".png"
                cv2.imwrite(temp_name,temp_image)
                j += 1
                temp_image = None
            i += 1
        except IOError:
            print("Error:没文件")
            
def rename():
    i = 1
    j = 1
    temp_image = None
	#i是原有的文件最大数字，可以改；j是实际数目，不用改

    while(i<372):
        try:
            name = "rgb"+str(i)+".jpg"
            temp_image = cv2.imread(name)
            if(temp_image is not None):
			    
                temp_name = "rgb"+str(j+371)+".jpg"
                cv2.imwrite(temp_name,temp_image)
                j += 1
                temp_image = None
            i += 1
        except IOError:
            print("Error:没文件")
			
def main():
    rename()

if __name__ == '__main__':
    main()
