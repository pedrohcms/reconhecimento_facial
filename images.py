# -*- coding: utf8 -*-
#Author: Pedro Henrique Correa Mota da Silva

import cv2
import os
import time

#Take the photos so the neural network can recognize them later
def take_pictures(name):
    cap = cv2.VideoCapture(0)
    index = 0

    init_time = time.time()

    while True:    
        ret, frame = cap.read()

        if not ret:
            print('Error')
            break

        cv2.imshow('frame', frame)
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #We transform the image to grayscale
        #Here we save the image in the directory, with the format: username_index

        cv2.imwrite(os.path.join('users', name, name+'_'+str(index)+'.jpeg'), frame)
        
        index += 1            

        k = cv2.waitKey(10)

        end_time = time.time()

        print(end_time - init_time)
        
        if end_time - init_time >= 5:
            break
        
    cap.release()
    cv2.destroyAllWindows()

def take_photo():
    cap = cv2.VideoCapture(0)

    while True:    
        ret, frame = cap.read()

        if not ret:
            print('Error')
            break

        cv2.imshow('frame', frame)

        k = cv2.waitKey(10)

        if k == ord('s'):
            break
            
    cap.release()
    cv2.destroyAllWindows()
    return frame