import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def imgshow(img):
    plt.figure()
    if len(img.shape) == 3:
        plt.imshow(img)
    else:
        plt.imshow(img,cmap ='gray') 
    plt.show() 

def sub_imgshow(i, img_rgb, img_avg, img_line, result_img):
    fig = plt.figure(i)
    #plt.ion()
    ax = fig.add_subplot(2,2,1)
    ax.set_title('RGB image')
    ax.imshow(img_rgb)
    ax = fig.add_subplot(2,2,2)
    ax.set_title('Segment image')
    ax.imshow(img_avg, cmap ='gray')
    ax = fig.add_subplot(2,2,3)
    ax.set_title('Line detect')
    ax.imshow(img_line) 
    ax = fig.add_subplot(2,2,4)
    ax.set_title('Result img')
    ax.imshow(result_img)
    # plt.ioff()
    plt.show() 