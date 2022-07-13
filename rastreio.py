from PIL import Image
from pathlib import Path
import os
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

''' 
file_directory = Path("fundo_branco/")

for current_file in file_directory.iterdir():
    if current_file.is_file():
        with open(current_file, 'r') as data_file:
            image = Image.open("fundo_branco/" + os.path.basename(current_file))
            # Gray
            image = image.convert('L')
            image.save("fundo_branco_pt/" + os.path.basename(current_file))

file_directory = Path("fundo_vermelho/")

for current_file in file_directory.iterdir():
    if current_file.is_file():
        with open(current_file, 'r') as data_file:
            image = Image.open("fundo_vermelho/" + os.path.basename(current_file))
            # Gray
            image = image.convert('L')
            image.save("fundo_vermelho_pt/" + os.path.basename(current_file))

## melhor metodo: cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED
file_directory = Path("fundo_vermelho_pt/")

for current_file in file_directory.iterdir():
    if current_file.is_file():
        with open(current_file, 'r') as data_file:
            img = cv.imread("fundo_vermelho_pt/" + os.path.basename(current_file),0)
            img2 = img.copy()
            template = cv.imread('vermelhoTemplate.png',0)
            w, h = template.shape[::-1]
            # All the 6 methods for comparison in a list
            methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
                        'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
            for meth in methods:
                img = img2.copy()
                method = eval(meth)
                # Apply template Matching
                res = cv.matchTemplate(img,template,method)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
                # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
                if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
                    top_left = min_loc
                else:
                    top_left = max_loc
                bottom_right = (top_left[0] + w, top_left[1] + h)
                cv.rectangle(img,top_left, bottom_right, 255, 2)
                plt.subplot(121),plt.imshow(res,cmap = 'gray')
                plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
                plt.subplot(122),plt.imshow(img,cmap = 'gray')
                plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
                plt.suptitle(meth)
                plt.show()

'''

## melhor metodo: 
file_directory = Path("fundo_branco_pt/")

for current_file in file_directory.iterdir():
    if current_file.is_file():
        with open(current_file, 'r') as data_file:
            img = cv.imread("fundo_branco_pt/" + os.path.basename(current_file),0)
            img2 = img.copy()
            template = cv.imread('brancoTemplate.png',0)
            w, h = template.shape[::-1]
            # All the 6 methods for comparison in a list
            methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
                        'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
            for meth in methods:
                img = img2.copy()
                method = eval(meth)
                # Apply template Matching
                res = cv.matchTemplate(img,template,method)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
                # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
                if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
                    top_left = min_loc
                else:
                    top_left = max_loc
                bottom_right = (top_left[0] + w, top_left[1] + h)
                cv.rectangle(img,top_left, bottom_right, 255, 2)
                plt.subplot(121),plt.imshow(res,cmap = 'gray')
                plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
                plt.subplot(122),plt.imshow(img,cmap = 'gray')
                plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
                plt.suptitle(meth)
                plt.show()