# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 17:33:41 2019

@author: Nugliar
"""
import cv2
import numpy as np

prefix = "landmark_aligned_face."
metadata = ['fold_0_data.txt','fold_1_data.txt','fold_2_data.txt','fold_3_data.txt','fold_4_data.txt']
classes = ["(0, 2)", "(4, 6)", "(8, 12)", "(15, 20)", "(25, 32)", "(38, 43)", "(48, 53)", "(60, 100)"]
path_faces = "D:/Download/Data/aligned"

classes_to_fix = {'35': classes[5], '3': classes[0], '55': classes[7], '58': classes[7], 
'22': classes[3], '13': classes[2], '45': classes[5], '36': classes[5], 
'23': classes[4], '57': classes[7], '56': classes[6], '2': classes[0], 
'29': classes[4], '34': classes[4], '42': classes[5], '46': classes[6], 
'32': classes[4], '(38, 48)': classes[5], '(38, 42)': classes[5], '(8, 23)': classes[2],
 '(27, 32)': classes[4]}


def return_folder_info(textfile):
#    global none_count
    none_count = 0 
    # one big folder list
    folder = []
    # start processing metadata txt
    with open(r'D:/Download/Data/' +  textfile) as text:
        lines = text.readlines()
        for line in lines[1:]:
            line = line.strip().split("\t")
            # real image path
            img_path = path_faces + "/" + line[0]+"/"+prefix+line[2]+"."+line[1]
            if line[3] == "None":
                none_count += 1
                continue
            else:
                # We store useful metadata infos
                folder.append([img_path]+line[3:5])
                if folder[-1][1] in classes_to_fix:
                    folder[-1][1] = classes_to_fix[folder[-1][1]]
    return folder, none_count

def imread(path, width, height):
    img = cv2.imread(path, 1)/255
    img = cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)
    return np.float32(img)

def build_one_hot(age):
    label = np.zeros(len(classes), dtype=int)
    label[classes.index(age)] = 1
    return label
