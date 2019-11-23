#coding: utf8
import tkinter as tk
from intelligence import recognize_user
from images import take_photo
from bem_vindo import bemVindo

def autenticacao():
    def autentica_Click():
        frame = take_photo()

        user = recognize_user(frame)
            
        redirect_user(user)

    def redirect_user(user):
        bemVindo(user[1], user[2])

    janela = tk.Tk()
    janela.title("Sistema de Autenticação") #titulo janela
    #janela["bg"] = "null"  #background

    janela.geometry("400x500+500+100")# Organização da janela lxA+E+T

    #================LABEL===============
    lb = tk.Label(janela, text="Para entrar, tire a foto")
    lb.place(x=130, y=150)
    #================/LABEL==============

    #=====================BOTÃO========================
    bt = tk.Button(janela, width = 50, text = "Tirar a foto", command = autentica_Click)
    bt.place(x=20, y=200)
    #=====================/BOTÃO=======================
    janela.mainloop()
    