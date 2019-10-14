# -*- coding: utf8 -*-
#Author: Pedro Henrique Correa Mota da Silva

import os
import images

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

        print('Recognizing user')
    elif op == 0:

        print('Exit')
        break
    else:
        print('Invalid option')