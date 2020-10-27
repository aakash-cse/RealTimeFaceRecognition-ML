# -*- coding: utf-8 -*-

"""
Created on Thu Jun  4 13:30:27 2020

@author: Aakash Babu
"""


import cv2
import os

name = input("Enter the name:-")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")
image_dir = os.path.join(image_dir,name)


# ---------------------- #

cam = cv2.VideoCapture(0)

cv2.namedWindow("Capture")

# ---------------------- #

for root, dirs, files in os.walk(image_dir):
    img_counter = len(files)

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Capture", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "{}--{}.png".format(name,img_counter)
        img_dir = os.path.join(image_dir,img_name)
        cv2.imwrite(img_dir, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()


