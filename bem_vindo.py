#coding: utf8
import tkinter as tk

def bemVindo(nome, nivel):

    janela = tk.Tk()
    janela.title("Bem Vindo") #titulo janela
    # Organização da janela lxA+E+T
    janela.geometry("400x500+500+100")
    tk.Label(janela, text="Bem vindo ao Sistema").pack()
    
    lb = tk.Label(janela, text="José Roberto Adolfo Júnior")
    lb.place(x=120, y=150)
    
    lb = tk.Label(janela, text="Henler Mendes Pio Soares")
    lb.place(x=120, y=200)
    
    lb = tk.Label(janela, text="Pedro Henrique Correa Mota da Silva")
    lb.place(x=120, y=250)
    
    lb = tk.Label(janela, text="Gustavo Alexandre Moimaz Costa")
    lb.place(x=120, y=300)

    lb = tk.Label(janela, text=nome, bg='blue')
    
    lb.pack(side='top', fill='x')
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