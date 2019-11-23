#coding: utf8
import tkinter as tk
import os
import sys
from cadastro import Cadastro
from autentica import autenticacao
from db_interaction.drop_delete import drop_table
import shutil

#==============Function_cadastra 1==============

def cadastra_Click ():
    Cadastro()
    
#==============/Fuunction_cadastra 1==============

#==============Function autentica 2==============

def autentica_Click ():
    autenticacao()

#==============/Function autentica 2==============

#==============Function Apagar Tudo 3==============

def drop_all():

    drop_table

    if os.path.isdir('users'):
        shutil.rmtree('users')
    
    if os.path.isdir('backup'):
        shutil.rmtree('backup')

    print('Tudo foi apagado')

#==============/Function Apagar Tudo 3==============

#==============Function fecha 4==============

def fecha_Click ():
    sys.exit()

#==============/Function fecha 4==============

janela = tk.Tk()
janela.title("Sistema de Autenticação") #titulo janela
#janela["bg"] = "null"  #background
# Organização da janela lxA+E+T
janela.geometry("400x500+500+100")
tk.Label(janela, text="sistema de autenticação").pack()

#===============Botão 1=================

bt = tk.Button(janela, width = 50, text = "Cadastrar Usuário", command = cadastra_Click )
bt.place(x=20, y=100)
#===============/Botão 1=================

#===============Botão 2=================
lb = tk.Label(janela, text="Para realizar o login:")
lb.place(x=140, y=150)
bt = tk.Button(janela, width = 50, text = "Autenticar", command = autentica_Click )
bt.place(x=20, y=200)
#===============/Botão 2=================

#===============Botão 3=================

bt = tk.Button(janela, width = 50, text = "Fechar Aplicação", command = fecha_Click )
bt.place(x=20, y=300)
#===============/Botão 3=================
janela.mainloop()
