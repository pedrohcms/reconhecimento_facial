#coding: utf8
from tkinter import* #importa toda a biblioteca
import tkinter
import tkinter
import os
import images

def autenticacao():
    def process_name(name):
        name = name.strip()
        name = name.upper()
        name = name.replace(' ','_')
        return name

    from intelligence import train_neural_network, CATEGORIES
    from tensorflow.keras.models import load_model
    import cv2
    import numpy as np

    def autentica_Click():
        if not os.path.isdir('backup'):
            train_neural_network()

        cap = cv2.VideoCapture(0)
        model = load_model(os.path.join('backup', 'model.h5'))

        while True:    
            ret, frame = cap.read()

            if not ret:
                print('Error')
                break

            cv2.imshow('frame', frame)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            frame = np.array(frame).reshape(-1, 640, 480, 1)
            frame = frame/255

            result = model.predict([frame])
                
            print(CATEGORIES[int(np.argmax(result))])

            if cv2.waitKey(10) == 27:
                break
                
        cap.release()
        cv2.destroyAllWindows()

    janela = tkinter.Tk()
    janela.title("Sistema de Autenticação") #titulo janela
    #janela["bg"] = "null"  #background

    janela.geometry("400x500+500+100")# Organização da janela lxA+E+T

    #================LABEL===============
    lb = Label (janela, text="Para entrar, tire a foto")
    lb.place(x=130, y=150)
    #================/LABEL==============

    #=====================BOTÃO========================
    bt = Button(janela, width = 50, text = "Comparar Foto", command = autentica_Click)
    bt.place(x=20, y=200)
    #=====================/BOTÃO=======================
    janela.mainloop()
