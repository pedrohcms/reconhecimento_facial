# -*- coding: utf8 -*-
#Author: Pedro Henrique Correa Mota da Silva

import os
import images
import cv2
from intelligence import train_neural_network, CATEGORIES
from tensorflow.keras.models import load_model
import numpy as np

def process_name(name):
   name = name.strip()
   name = name.upper()
   name = name.replace(' ','_')
   return name

op = 1

while op != 0:
    print('Press 1 to register ')
    print('Press 2 to activate recognition ')
    print('Press 0 to exit ')

    op = int(input())

    if op == 1:
        name = input('Enter username: ')
        name = process_name(name)   

        folder = './users'

        if not os.path.isdir(folder):
            os.mkdir(folder)
            
        folder = './users/'+name
        
        if not os.path.isdir(folder):
            os.mkdir(folder) #Create the directory that stores the user's images
            print('Press s key to take a picture')   
            print('Press Esc key to finish shooting')
            print('Please note that at least one photo is required for registration')
            images.take_picture(name) #Invokes the function that take pictures and save user's imagem
            
            if len(os.listdir(folder)) == 0:
                print('Error registering user: '+ name+', try again')
                os.rmdir(folder) #We removed the folder that was created if the user does not register correctly
        else:
            print('User already registered! ')

    elif op == 2:
        
        if not os.path.isdir('backup'):
            train_neural_network()
        
        model = load_model(os.path.join('backup', 'model.h5'))
        
        print(model)

        frame = cv2.imread('teste/pedro.jpeg')
        frame = np.array(frame).reshape(-1, 640, 480, 1)
        frame = frame/255.0
        prediction = model.predict(frame)
        print(prediction)
        print(CATEGORIES[int(prediction[0][0])])

        frame = cv2.imread('teste/gu.jpeg')
        frame = np.array(frame).reshape(-1, 640, 480, 1)
        frame = frame/255.0
        prediction = model.predict(frame)
        print(prediction)
        print(CATEGORIES[int(prediction[0][0])])

        frame = cv2.imread('teste/dri.jpeg')
        frame = np.array(frame).reshape(-1, 640, 480, 1)
        frame = frame/255.0
        prediction = model.predict(frame)
        print(prediction)
        print(CATEGORIES[int(prediction[0][0])])

        # cap = cv2.VideoCapture(0)

        # while True:    
        #     ret, frame = cap.read()

        #     if not ret:
        #         print('Error')
        #         break

        #     cv2.imshow('frame', frame)

        #     frame = np.array(frame).reshape(-1, 640, 480, 1)

        #     frame = frame/255.0

        #     prediction = model.predict([frame])            

        #     print(CATEGORIES[int(prediction[0][0])])

        #     k = cv2.waitKey(10)

        #     if k == 27:
        #         break
        
        # cap.release()
        # cv2.destroyAllWindows()
        
    elif op == 0:
        print('Exit')
        break

    else:
        print('Invalid option')