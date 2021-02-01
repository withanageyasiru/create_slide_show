import cv2
import random

class Image:
    def __init__(self, filename, time=500, size=500):
        self.size = size
        self.time = time
        self.shifted = 0.0
        self.img = cv2.imread(filename)
        self.height, self.width, _ = self.img.shape
        if self.width < self.height:
            self.height = int(self.height*size/self.width)
            self.width = size
            self.img = cv2.resize(self.img, (self.width, self.height))
            self.shift = self.height - size
            self.shift_height = True
        else:
            self.width = int(self.width*size/self.height)
            self.height = size
            self.shift = self.width - size
            self.img = cv2.resize(self.img, (self.width, self.height))
            self.shift_height = False
        self.delta_shift = self.shift/self.time

    def reset(self):
        if random.randint(0, 1) == 0:
            self.shifted = 0.0
            self.delta_shift = abs(self.delta_shift)
        else:
            self.shifted = self.shift
            self.delta_shift = -abs(self.delta_shift)

    def get_frame(self):
        if self.shift_height:
            roi = self.img[int(self.shifted):int(self.shifted) + self.size, :, :]
        else:
            roi = self.img[:, int(self.shifted):int(self.shifted) + self.size, :]
        self.shifted += self.delta_shift
        if self.shifted > self.shift:
            self.shifted = self.shift
        if self.shifted < 0:
            self.shifted = 0
        return roi