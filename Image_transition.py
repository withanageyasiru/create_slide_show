import time

import cv2
import numpy as np
from PIL import Image as pil_image
from PIL import ImageDraw
import matplotlib.pyplot as plt


class Image:
    def __init__(self, path, size=(500,400), transition = (0,0), fade = False,fps = 25,  transition_time = 1, display_time = 1):
        self.image = pil_image.open(path).resize(size)
        self.image_size = size
        self.transition = transition
        self.fade = fade
        self.fps = fps
        self.transition_time = transition_time
        self.display_time = display_time

        self.faded = 0 if fade else 255
        self.fade_steps = int(255 / self.fps / self.transition_time) + 1
        self.display_frames = self.display_time * self.fps
        self.shift_per_frame = [0,0] # 0 menas no shift if shift < 0 left shifted if shift > 0 right shifted
        self.shifted = [0,0]
        self.decition_para = [False,False]
        self.finished = False

        for i in range(0,2):
            if self.transition[i] > 0:
                self.shifted[i] -= self.image_size[i]
                self.shift_per_frame[i] = self.image_size[i] / self.transition_time / self.fps
                self.decition_para[i] = True
            elif self.transition[i] < 0:
                self.shifted[i] += self.image_size[i]
                self.shift_per_frame[i] = - self.image_size[i] / self.transition_time / self.fps
                self.decition_para[i] = False
            else:
                self.shifted[i] = 0
                self.shift_per_frame[i] = 0
                self.decition_para[i] = False

    def get_frame(self):

        if self.faded < 255:
            self.faded += self.fade_steps
        else:
            self.faded = 255

        if (self.shifted[0] > 0) == self.decition_para[0]:
            self.shifted[0] = 0
            self.shift_per_frame[0] = 0

        if (self.shifted[1] > 0) == self.decition_para[1]:
            self.shifted[1] = 0
            self.shift_per_frame[1] = 0

        if self.shifted == [0,0] and self.faded == 255:
            self.display_frames -= 1
            if self.display_frames <= 0 :
                self.finished = True

        image = pil_image.new('RGBA', self.image_size, (0, 0, 0, 0))
        self.image.putalpha(self.faded)
        image.paste(self.image, self.shifted, self.image)
        self.shifted = [int(self.shifted[0] + self.shift_per_frame[0]), int(self.shifted[1] + self.shift_per_frame[1])]

        return image, self.finished



