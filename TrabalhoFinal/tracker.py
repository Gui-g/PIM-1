from operator import index
from PIL import Image
from pathlib import Path
import os
import cv2 as cv
import numpy as np
from skimage import color
from matplotlib import pyplot as plt

def result_directory(method, type = '-'):
    res = 'result_images/'
    
    match method:
        case 'cv.TM_SQDIFF':
            res = res + 'TM_SQDIFF/'
        case 'cv.TM_SQDIFF_NORMED':
            res = res + 'TM_SQDIFF_NORMED/'
        case 'cv.TM_CCORR':
            res = res + 'TM_CCORR/'
        case 'cv.TM_CCORR_NORMED':
            res = res + 'TM_CCORR_NORMED/'
        case 'cv.TM_CCOEFF':
            res = res + 'TM_CCOEFF/'
        case 'cv.TM_CCOEFF_NORMED':
            res = res + 'TM_CCOEFF_NORMED/'
    match type:
        case 'match':
            res = res + 'match/'
        case 'track':
            res = res + 'track/'
    return res

## melhor metodo: 
file_directory = Path("fundo_branco_pt/")
# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
MIN_MAX_VALUES = list()

for current_file in file_directory.iterdir():
    if current_file.is_file():
        with open(current_file, 'r') as data_file:
            img = cv.imread("fundo_branco_pt/" + os.path.basename(current_file),0)
            img2 = img.copy() 
            template = cv.imread('brancoTemplate.png',0)
            w, h = template.shape[::-1]

            for meth in methods:
                img = img2.copy()
                method = eval(meth)
                # Apply template Matching
                res = cv.matchTemplate(img,template,method)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
                MIN_MAX_VALUES.append((min_val, max_val))
                # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
                if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
                    top_left = min_loc
                else:
                    top_left = max_loc
                bottom_right = (top_left[0] + w, top_left[1] + h)
                cv.rectangle(img,top_left, bottom_right, 255, 2)
                save_dir = result_directory(meth, 'track')
                print(save_dir + os.path.basename(current_file))
                cv.imwrite(save_dir + os.path.basename(current_file), img)
                save_dir = result_directory(meth, 'match')
                gs = plt.get_cmap('gray')
                gs_res = gs(res)
                plt.imsave(save_dir + os.path.basename(current_file), res)

#for method in methods:
#    i = 1
#    max_len_n = len('1000')
#    max_len_v_min = len('1000000')
#    max_len_v_max = len('1000000')
#    directory = open(result_directory(method) + "min_max_v.txt", "w")
#    for num in range (299):
#        directory.write("{0} {1} {2}\n".format(
#            str(num+2).ljust(max_len_n),
#            str(MIN_MAX_VALUES[i + num*6][0]).ljust(max_len_v_min),
#            str(MIN_MAX_VALUES[i + num*6][1]).ljust(max_len_v_max)
#        ))
#    i = i+1
#    directory.close()
#
#for meth in methods:
#    for type in ['match', 'track']:
#        generate_video(meth, type)
