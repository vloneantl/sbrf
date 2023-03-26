import numpy as np
import cv2
import os
import sys
import glob

# data_set path
kitti_img_path = '/workspace/val/images/*'
kitti_label_path = '/workspace/val/labels/*'

# transformed lables path
kitti_label_tosave_path = '/workspace/val/yolo_labels/'

img_list = glob.glob(kitti_img_path)
lbl_list = glob.glob(kitti_label_path)

class_dict = {
    'person': 0,
    'face': 1,
    'license_plate': 2,
    'vehicle': 3,
    'head': 4,
    'truck': 5,
    'bus': 6,
    'motorcycle': 7
}


img_list.sort()
lbl_list.sort()

for lbl in lbl_list:
    with open(lbl, 'r') as infile:
        os.chdir(kitti_label_tosave_path)
        outfile = open(lbl[-20:], 'w')
        lines = infile.readlines()
        for line in lines:
            new_line = line.split(' ')
            new_line_str = str(class_dict[new_line[0]]) + ' '+ new_line[4] + " " + \
                           new_line[5] + ' ' + new_line[6] + ' ' + new_line[7] + '\n'
            print(new_line_str)
            print(kitti_label_tosave_path)
            outfile.write(new_line_str)
        outfile.close()



