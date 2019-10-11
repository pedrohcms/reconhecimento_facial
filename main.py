import os
import images

op = 1

while op != 0:
    print('Digite 1 para cadastrar ')
    print('Digite 2 para reconhecer ')
    print('Digite 0 para sair ')

    op = int(input())

    if op == 1:
        name = input('Entre com o nome do usuário: ')
        name = name.lower()
            
        folder = './users/'+name
        
        if not os.path.isdir(folder):
            os.mkdir(folder)
                
            images.take_picture(name)
        else:
            print('Usuário já cadastrado! ')
        
    elif op == 2:
        print('Reconhecendo usuario')
    elif op == 0:
        break
    else:
        print('Opção inválida')