import os
import math
import numpy as np
import pandas as pd
import os.path as osp
from tqdm import tqdm

label_warp = {'DESERT': 0,
              'OCEAN': 1,
              'MOUNTAIN': 2,
              'FARMLAND': 3,
              'LAKE': 4,
              'CITY': 5,
              }

# train data
data_path = 'data/train/images'
img_path, label = [], []

trainlist = pd.read_csv('data/train/imgname.csv',header=None)
for index, row in trainlist.iterrows():
  img_path.append(osp.join(data_path, row[0]))
  label.append(row[1])

label_file = pd.DataFrame({'img_path': img_path, 'label': label})
label_file['label'] = label_file['label'].map(label_warp)

label_file.to_csv('data/train.csv', index=False)

# test data
test_data_path = 'data/testa/images'
all_test_img = os.listdir(test_data_path)
test_img_path = []

for img in all_test_img:
    if osp.splitext(img)[1] == '.jpg':
        test_img_path.append(osp.join(test_data_path, img))

test_file = pd.DataFrame({'img_path': test_img_path})
test_file.to_csv('data/testa.csv', index=False)
