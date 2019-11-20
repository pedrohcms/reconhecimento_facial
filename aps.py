#coding: utf8
from tkinter import* #importa toda a biblioteca
import tkinter
from cadastro import Cadastro
from autentica import autenticacao
#==============Function_cadastra 1==============

def cadastra_Click ():
    Cadastro()
    

#==============/Fuunction_cadastra 1==============

#==============Function autentica 2==============

def autentica_Click ():
    autenticacao()
    

#==============/Function autentica 2==============

#==============Function fecha 3==============

def fecha_Click ():
    sys.exit()

#==============/Function fecha 3==============
janela = tkinter.Tk()
janela.title("Sistema de Autenticação") #titulo janela
#janela["bg"] = "null"  #background
# Organização da janela lxA+E+T
janela.geometry("400x500+500+100")
Label (janela, text="sistema de autenticação").pack()

#===============Botão 1=================

bt = Button(janela, width = 50, text = "Cadastrar Usuário", command = cadastra_Click )
bt.place(x=20, y=100)
#===============/Botão 1=================

#===============Botão 2=================
lb = Label (janela, text="Para realizar o login:")
lb.place(x=140, y=150)
bt = Button(janela, width = 50, text = "Autenticar", command = autentica_Click )
bt.place(x=20, y=200)
#===============/Botão 2=================

#===============Botão 3=================

bt = Button(janela, width = 50, text = "Fechar Aplicação", command = fecha_Click )
bt.place(x=20, y=300)
#===============/Botão 3=================
janela.mainloop()
