import cv2
import glob
import os
import numpy as np
from PIL import Image as pil_image
from Image_transition import Image

# image = Image('images/ice-cube.jpg',fps=60, transition_time=5,display_time=3 , transition=(-1,0))
# image2 = Image('images/ice-cube.jpg', transition_time=5,display_time=3 , transition=(-1,0))
#
#
# for i in range(2000):
#     result, finished = image.get_frame()
#     if finished:
#         break
#     previous_image = pil_image.open('images/ice-cube.jpg').resize(size)
#     previous_image.paste(result, (0,0), result.convert('RGBA'))
#     open_cv_image = cv2.cvtColor(np.asarray(previous_image), cv2.COLOR_RGB2BGR)
#     image_stack.append(open_cv_image)
#     cv2.imshow('sa',open_cv_image)
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), FPS, size)
#
# for image_i in image_stack:
#     out.write(image_i)
# out.release()





def process():
    image_stack = []
    size = (1000, 667)
    FPS = 60
    transitions = [(0,0),(1,1),(0,0),(-1,0),(1,1)]
    transition_times = [2,1,3,4,3]
    display_times = [2,3,1,3,2]
    fade = [True,False,True,False,True]
    path = "images"
    filenames = glob.glob(os.path.join(path, "*.png"))
    previous_image = pil_image.new('RGBA', size, (0, 0, 0, 0))
    # previous_image = cv2.cvtColor(np.asarray(previous_image), cv2.COLOR_RGB2BGR)

    for i,image in enumerate(filenames):
        image = Image(image, fps=FPS,size=size, transition_time=transition_times[i], display_time=display_times[i], transition=transitions[i],fade=fade[i])
        while True:
            result, finished = image.get_frame()
            previous_image.paste(result, (0, 0), result)
            open_cv_image = cv2.cvtColor(np.asarray(previous_image), cv2.COLOR_RGB2BGR)
            if finished:
                previous_image = result
                break
            image_stack.append(open_cv_image)
            cv2.imshow('sa', open_cv_image)
            if cv2.waitKey(1) == ord('q'):
                break

        out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), FPS, size)

        for image_i in image_stack:
            out.write(image_i)
        out.release()

process()
