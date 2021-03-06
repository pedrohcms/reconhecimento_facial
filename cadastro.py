#coding: utf8
import tkinter as tk
import os
import images
from db_interaction.User import User
from intelligence import train_neural_network
import shutil

def Cadastro():

    new_user = False

    def process_name(name):
        name = name.strip()
        name = name.upper()
        name = name.replace(' ','_')
        return name
			
    def foto_Click():
        name = campo.get()
        label = process_name(name)   

        folder = 'users'

        if not os.path.isdir(folder):
            os.mkdir(folder)
                
        folder = './users/'+name
            
        folder = os.path.join('users', label)

        if not os.path.isdir(folder):
            os.mkdir(folder) #Create the directory that stores the user's images
            images.take_pictures(label) #Invokes the function that take pictures and save user's imagem

            user = User() # Object of class User
            user.insert(name, var.get(), label)

            conf = tk.Label(janela, text="USUARIO CADASTRADO COM SUCESSO", bg="green")
            conf.pack(side='top', fill='x')    
            print(campo.get())

            global new_user
            new_user = True

            if len(os.listdir(folder)) == 0:
                print('Error registering user: '+ name+', try again')
                os.rmdir(folder) #We removed the folder that was created if the user does not register correctly
        else:
            print('User already registered! ')

    def on_close():
        global new_user
        if new_user == True:
            if os.path.isdir('backup'):
                shutil.rmtree('backup')
            train_neural_network()
        janela.destroy()

    janela = tk.Tk()
    janela.title("Sistema de Cadastro") #titulo janela

    # Organização da janela lxA+E+T
    janela.geometry("400x500+500+100")
    tk.Label(janela, text="Sistema de Cadastro").pack()

    #=====================CAMPO========================
    campo = tk.Entry(janela, width=60)
    campo.place(x=15, y=200)

    lb = tk.Label(janela, text="Para realizar Cadastro, insira seu nome, sua prioridade e tire a foto ")
    lb.place(x=20, y=150)
    #=====================/CAMPO=======================

    #=====================BOTÃO========================
    bt = tk.Button(janela, width = 50, text = "Tirar a foto", command = foto_Click)
    bt.place(x=20, y=300)
    #=====================/BOTÃO=======================

    #=====================OPÇÕES=======================
    #prioridade 1= qualquer pessoa, 2= dirigentes 3= ministro 
    var = tk.StringVar()
    var.set("1")

    pri = tk.OptionMenu(janela, var, "1","2","3") 
    pri.place(x=170, y=250)

    #====================/OPÇÕES=======================

    janela.protocol("WM_DELETE_WINDOW", on_close)

    janela.mainloop()