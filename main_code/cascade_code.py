import os
import re
import time
import cv2
import numpy as np
from os.path import isfile, join

tree_classifier = cv2.CascadeClassifier('C:\\Users\\titan\\Desktop\\cv_detect\\cascade.xml')
cap = cv2.VideoCapture('C:\\Users\\titan\\Desktop\\cv_detect\\DJI_0017.MP4')
out = cv2.VideoWriter('results.avi',cv2.VideoWriter_fourcc(*'XVID'), 20, (3840, 2160))

while True:
    time.sleep(.05)
    ret, frame = cap.read()

    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        trees = tree_classifier.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in trees:
            image = cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)
            cv2.namedWindow('Trees',cv2.WINDOW_NORMAL)
            cv2.putText(image, 'Tree', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.imshow('Trees', image)
            cv2.resizeWindow('Trees', 900,600)
            out.write(image)
            cv2.waitKey(1)

    else:
        break

out.release()
cap.release()
cv2.destroyAllWindows()
