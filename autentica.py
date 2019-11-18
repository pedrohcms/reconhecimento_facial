#coding: utf8
from tkinter import* #importa toda a biblioteca
import tkinter
import os
import cv2
import intelligence

def autentica_Click():

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            print('Error')
            break

        cv2.imshow('frame', frame)

        if cv2.waitKey(10) == ord('s'):
            user = intelligence.recognize_user(frame)
            break
            
    cap.release()
    cv2.destroyAllWindows()
    
    redirect_user(user)

def redirect_user(user):
    print(user)

janela = tkinter.Tk()
janela.title("Sistema de Autenticação") #titulo janela
#janela["bg"] = "null"  #background

janela.geometry("400x500+500+100")# Organização da janela lxA+E+T

#================LABEL===============
lb = Label (janela, text="Para entrar, tire a foto")
lb.place(x=130, y=150)
#================/LABEL==============

#=====================BOTÃO========================
bt = Button(janela, width = 50, text = "Analisar Foto", command = autentica_Click)
bt.place(x=20, y=200)
#=====================/BOTÃO=======================
janela.mainloop()
