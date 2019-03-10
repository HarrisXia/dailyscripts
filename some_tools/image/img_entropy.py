import math
def Imentropy(img):
    size = img.shape
    tmp = []  
    for i in range(size[0]*size[1]):  
        tmp.append(0)  
    val = 0  
    k = 0  
    res = 0 
    for i in range(len(img)):  
        for j in range(len(img[i])):  
            val = img[i][j]  
            tmp[val] = float(tmp[val] + 1)  
            k =  float(k + 1)  
    for i in range(len(tmp)):  
        tmp[i] = float(tmp[i] / k)  
    for i in range(len(tmp)):  
        if(tmp[i] == 0):  
            res = res  
        else:  
            res = float(res - tmp[i] * (math.log(tmp[i]) / math.log(2.0)))  
    return res