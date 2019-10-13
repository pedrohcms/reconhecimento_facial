# -*- coding: utf8 -*-

import os
import images

def process_name(name):
   name = name.strip()
   name = name.upper()
   name = name.replace(' ','_')
   return name

op = 1

while op != 0:
    print('Digite 1 para cadastrar ')
    print('Digite 2 para reconhecer ')
    print('Digite 0 para sair ')

    op = int(input())

    if op == 1:
        name = input('Entre com o nome do usuário: ')
        name = process_name(name)   

        folder = './users'

        if not os.path.isdir(folder):
            os.mkdir(folder)
            
        folder = './users/'+name
        
        if not os.path.isdir(folder):
            os.mkdir(folder) #Cria o diretório em que as imagens do usuário serão salvas
            print('Pressione a tecla s para tirar uma foto')   
            print('Pressione a tecla Esc para terminar de fotografar')
            images.take_picture(name) #Invoca a função que fotografa e salva as imagens do usuário
            
            if len(os.listdir(folder)) == 0:
                print('Erro ao cadastrar usuário: '+name+', tente novamente')
                os.rmdir(folder) #Removemos a pasta que foi criada caso o usuário não se cadastre corretamente
        else:
            print('Usuário já cadastrado! ')

    elif op == 2:

        print('Reconhecendo usuario')
    elif op == 0:

        print('Saindo')
        break
    else:
        print('Opção inválida')