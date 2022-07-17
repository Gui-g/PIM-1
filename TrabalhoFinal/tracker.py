from pathlib import Path
import os
import cv2 as cv
from matplotlib import pyplot as plt

def result_directory(method, video = '', type = ''):
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
    match video:
        case 'branco':
            res = res + 'fundo_branco/'
        case 'vermelho':
            res = res + 'fundo_vermelho/'
    match type:
        case 'match':
            res = res + 'match/'
        case 'track':
            res = res + 'track/'
    return res

def main():
    ## melhor metodo:
    # All the 6 methods for comparison in a list
    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 
                'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
    videos = ['branco', 'vermelho']
    MIN_MAX_VALUES = list()

    for video in videos:
        if video == 'branco':
            file_directory = Path("fundo_branco_gs/")
        else:
            file_directory = Path("fundo_vermelho_gs/")
        for current_file in file_directory.iterdir():
            if current_file.is_file():
                with open(current_file, 'r') as data_file:
                    img = cv.imread(str(file_directory) + '/' + os.path.basename(current_file), 0)
                    img2 = img.copy() 
                    template = cv.imread('Template.png',0)
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
                        save_dir = result_directory(meth, video, 'track')
                        print(save_dir + os.path.basename(current_file))
                        cv.imwrite(save_dir + os.path.basename(current_file), img)
                        save_dir = result_directory(meth, video, 'match')
                        plt.imsave(save_dir + os.path.basename(current_file), res)
        
        if video == 'branco':
            MIN_MAX_VALUES_W = MIN_MAX_VALUES.copy()
            MIN_MAX_VALUES = list()

    #organizar a tabela
    for video in videos:
        i = 0

        if video == 'branco':
            VALUES_LIST = MIN_MAX_VALUES_W.copy()
        else:
            VALUES_LIST = MIN_MAX_VALUES.copy()

        for method in methods:
            max_len_n = len('frame_300')
            max_len_v = 20
            directory = open(result_directory(method, video = video) + "min_max_v.txt", "w")

            directory.write("{0} {1} {2}\n".format(
                'frame'.ljust(max_len_n),
                'min value'.ljust(max_len_v),
                'max_value'.ljust(max_len_v)
            ))
            directory.write("--------------------------------------------------\n")

            for num in range (299):
                if num < 8:
                    row_name = 'frame_00' + str(num+2)
                elif num < 98:
                    row_name = 'frame_0' + str(num+2)
                else:
                    row_name = 'frame_' + str(num+2)
                directory.write("{0} {1} {2}\n".format(
                    row_name.ljust(max_len_n),
                    str(VALUES_LIST[i + num*6][0]).ljust(max_len_v),
                    str(VALUES_LIST[i + num*6][1]).ljust(max_len_v)
                ))
            i = i+1
            directory.close()

if __name__ == "__main__":
    main()