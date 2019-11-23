#coding: utf8
import tkinter as tk

def bemVindo(nome, nivel):

    janela = tk.Tk()
    janela.title("Bem Vindo") #titulo janela
    # Organização da janela lxA+E+T
    janela.geometry("400x500+500+100")
    tk.Label(janela, text="sistema de autenticação").pack()
    str(nivel)
    lb = tk.Label(janela, text="Bem vindo ao Sistema ")
    lb.place(x=140, y=150)

    lb = tk.Label(janela, text= nome)
    lb.place(x=140, y=200)
    if nivel == 1:
        conf = tk.Label(janela, text="USUARIO NIVEL ACESSOR", bg="red")
        conf.pack(side='top', fill='x')    
    if nivel == 2:
        conf = tk.Label(janela, text="USUARIO NIVEL DIRETOR", bg="yellow")
        conf.pack(side='top', fill='x')  
    if nivel == 3:
        conf = tk.Label(janela, text="USUARIO NIVEL MINISTRO", bg="green")
        conf.pack(side='top', fill='x')    
    janela.mainloop()

#bemVindo("Bruce Wayne", 3)