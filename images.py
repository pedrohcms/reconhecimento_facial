# -*- coding: utf8 -*-
#Author: Pedro Henrique Correa Mota da Silva

import cv2
import os

#Take the photos so the neural network can recognize them later
def take_picture(name):
    cap = cv2.VideoCapture(0)
    index = 0

    while True:    
        ret, frame = cap.read()

        if not ret:
            print('Error')
            break

        #TRESH_TRUNC was the best filter found, however there must be a better one
        #ret, frame = cv2.threshold(frame, 127, 255, cv2.THRESH_TRUNC) #We apply binarization
        cv2.imshow('frame', frame)
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #We transform the image to grayscale
        #Here we save the image in the directory, with the format: username_index

        cv2.imwrite(os.path.join('users', name, name+'_'+str(index)+'.jpeg'), frame)
        
        index += 1            

        k = cv2.waitKey(10)

        if k == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()