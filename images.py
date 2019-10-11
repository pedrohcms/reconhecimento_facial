# -*- coding: utf8 -*-

import cv2

#Tira as fotos para que a rede neural possa reconhece-las mais tarde
def take_picture(name):
    cap = cv2.VideoCapture(0)
    index = 0

    while True:    
        ret, frame = cap.read()

        if not ret:
            print('Erro')
            break

        #TRESH_TRUNC foi o melhor filtro encontrado, no entanto deve haver um muito melhor
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Transformamos a imagem em escala de cinza
        #ret, frame = cv2.threshold(frame, 127, 255, cv2.THRESH_TRUNC) #Aplicamos a binarização
        cv2.imshow('frame', frame)

        k = cv2.waitKey(10)

        if k == 27:
            break
        elif k == ord('s'):
            cv2.imwrite('./users/'+name+'/'+name+'_'+str(index)+'.jpeg', frame)
            index += 1
        
    cap.release()
    cv2.destroyAllWindows()