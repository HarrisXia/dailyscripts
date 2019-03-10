import random
import numpy as np
import math
from PIL import Image

class RandomErasing(object):
    """ Randomly selects a rectangle region in an image and erases its pixels.
        'Random Erasing Data Augmentation' by Zhong et al.
        See https://arxiv.org/pdf/1708.04896.pdf
    Args:
         probability: The probability that the Random Erasing operation will be performed.
         sl: Minimum proportion of erased area against input image.
         sh: Maximum proportion of erased area against input image.
         r1: Minimum aspect ratio of erased area.
         mean: Erasing value. 
    """
    
    def __init__(self, probability = 0.5, sl = 0.02, sh = 0.4, r1 = 0.3, mean=[0.4914, 0.4822, 0.4465]):
        self.probability = probability
        self.mean = mean
        self.sl = sl
        self.sh = sh
        self.r1 = r1
       
    def __call__(self, img):

        if random.uniform(0, 1) > self.probability:
            return img

        for attempt in range(100):
            #print(img.getpixel((100,100)))
            img = np.array(img)
            W = img.shape[0]
            H = img.shape[1]
            area = W * H
       
            target_area = random.uniform(self.sl, self.sh) * area
            aspect_ratio = random.uniform(self.r1, 1/self.r1)

            h = int(round(math.sqrt(target_area * aspect_ratio)))
            w = int(round(math.sqrt(target_area / aspect_ratio)))

            if w < W and h < H:
                x1 = random.randint(0, H - h)
                y1 = random.randint(0, W - w)
                # if img.size()[0] == 3:
                img[x1:x1+h, y1:y1+w, 0] = self.mean[0]
                img[x1:x1+h, y1:y1+w, 1] = self.mean[1]
                img[x1:x1+h, y1:y1+w, 2] = self.mean[2]
                # else:
                #     img[0, x1:x1+h, y1:y1+w] = self.mean[0]
                img= Image.fromarray(img)
                return img

        return img