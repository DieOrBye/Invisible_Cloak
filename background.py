# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:01:58 2020

@author: Souhardya
"""

import cv2
cap=cv2.VideoCapture(1)

while cap.isOpened():
    ret,back=cap.read()
    if ret==True:
        cv2.imshow('image',back)
        
        if cv2.waitKey(5)==ord('q'):
            cv2.imwrite('image.jpg',back)
            break
cap.release()
cv2.destroyAllWindows()