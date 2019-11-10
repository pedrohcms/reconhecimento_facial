# -*- coding: utf8 -*-
#Author: Pedro Henrique Correa Mota da Silva

import os
import cv2
import numpy as np
import random
import pickle
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D

CATEGORIES = ['ADRIANA_DE_CASSIA_CORREA_MOTA_DA_SILVA', 'GUSTAVO_ALEXANDRE_MOIMAZ_COSTA', 'PEDRO_HENRIQUE_CORREA_MOTA_DA_SILVA']

#Load the images from the users folder and create the data for model training
def create_training_data():
    
    dirs = './users/'
    training_data = []

    for category in CATEGORIES:
        path = os.path.join(dirs, category)
        label = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                training_data.append([img, label])
            except Exception as e:
                print(e)
    
    random.shuffle(training_data)
    
    X = []
    y = []

    for features, label in training_data:
        X.append(features)
        y.append(label)
    
    X = np.array(X).reshape(-1, 640, 480, 1)
    y = tf.one_hot(y, len(CATEGORIES))#Cria um tensor que contem todas as labels para ser passada a model

    os.mkdir('backup')#Criamos uma pasta para receber o backup dos datasets

    data_file = open(os.path.join('backup', 'data.pickle'), "wb")
    pickle.dump(X, data_file)
    data_file.close()

    labels_file = open(os.path.join('backup', 'labels.pickle'), "wb")
    pickle.dump(y, labels_file)
    labels_file.close()

def train_neural_network():
    
    if not os.path.isdir('backup'):
        create_training_data()

    X = pickle.load(open(os.path.join('backup', 'data.pickle'), "rb"))
    y = pickle.load(open(os.path.join('backup', 'labels.pickle'), "rb"))

    X = X/255.0

    model = Sequential()
    model.add(Conv2D(64, (3,3), input_shape=X.shape[1:]))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3,3)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(64))

    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    model.compile(loss="categorical_crossentropy",
                 optmizer="adam",
                 metrics=['accuracy'])

    model.fit(X, y, batch_size=2, epochs=5, validation_split=0.2)

    #Here we make the backup of the neural network
    model.save(os.path.join('backup', 'model.h5'))