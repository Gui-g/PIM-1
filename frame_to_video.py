from operator import index
import os
import cv2 as cv
from TrabalhoFinal.tracker import result_directory

def generate_video(method, type):
    image_dir = result_directory(method, type)
    
    video_name = result_directory(method, type) + "result_video.avi"

    images = [img for img in os.listdir(image_dir) if img.endswith(".png")]

    frame = cv.imread(os.path.join(image_dir, images[0]))
    height, width, layers = frame.shape
    video = cv.VideoWriter(video_name, 0, 25, (width, height))
    for image in images:
        video.write(cv.imread(os.path.join(image_dir, image)))
        
    cv.destroyAllWindows()
    video.release()

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
types = ['match', 'track']
for meth in methods:
    for type in types:
        generate_video(meth, type)