# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 22:52:34 2021

@author: dhjun
"""

import cv2
#import cv2.aruco as aruco
#import numpy as np
#from math import pi, sqrt, atan2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()