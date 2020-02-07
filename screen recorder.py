# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 18:51:00 2020

@author: Ankit Kurmi
"""
#importing libraries
import pyautogui
import numpy as np
import cv2
import pyscreenshot as pys

#initialising the variable
a=pyautogui.size()
forcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', forcc, 8, (a.width,a.height))


#capturing while it is true
while True:
    img= pys.grab()
    img_np=np.array(img)

    #frame= cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Screen', img_np)
    out.write(img_np)


    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

#output
out.release()
cv2.destroyAllWindows()
