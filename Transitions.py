import cv2
import numpy as np
import glob
import os
import random
from Image_transition_old import Image


def process():
    path = "images/shutterstock"
    filenames = glob.glob(os.path.join(path, "*"))

    cnt = 0
    images = []
    for filename in filenames:
        print(filename)

        img = Image(filename)

        images.append(img)
        if cnt > 300:
            break
        cnt += 1

    prev_image = images[random.randrange(0, len(images))]
    prev_image.reset()

    while True:
        while True:
            img = images[random.randrange(0, len(images))]
            if img != prev_image:
                break
        img.reset()

        for i in range(100):
            alpha = i/100
            beta = 1.0 - alpha
            dst = cv2.addWeighted(img.get_frame(), alpha, prev_image.get_frame(), beta, 0.0)

            cv2.imshow("Slide", dst)
            if cv2.waitKey(1) == ord('q'):
                return

        prev_image = img
        for _ in range(300):
            cv2.imshow("Slide", img.get_frame())
            if cv2.waitKey(1) == ord('q'):
                return


process()