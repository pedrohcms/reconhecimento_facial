#coding: utf8
import tkinter as tk
import os
import images

def process_name(name):
   name = name.strip()
   name = name.upper()
   name = name.replace(' ','_')
   return name

def foto_Click():
    print(var.get()) # exemplo para puxar o valor do options 
    name = campo.get()
    name = process_name(name)   

    folder = './users'

    if not os.path.isdir(folder):
        os.mkdir(folder)
            
    folder = './users/'+name
        
    if not os.path.isdir(folder):
        os.mkdir(folder) #Create the directory that stores the user's images
        images.take_picture(name) #Invokes the function that take pictures and save user's imagem
            
        if len(os.listdir(folder)) == 0:
            print('Error registering user: '+ name+', try again')
            os.rmdir(folder) #We removed the folder that was created if the user does not register correctly
    else:
        print('User already registered! ')
   
    conf = tk.Label(janela, text="USUARIO CADASTRADO COM SUCESSO", bg="green")
#pqp.place(x=10, y=10)
    conf.pack(side='top', fill='x')    
    print(campo.get())
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
janela.mainloop()