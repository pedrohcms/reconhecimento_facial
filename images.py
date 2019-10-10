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

        cv2.imshow('frame', frame)

        k = cv2.waitKey(10)

        if k == 27:
            break
        elif k == ord('s'):
            cv2.imwrite('./users/'+name+'/'+name+'_'+str(index)+'.jpeg', frame)
            index += 1
        
    cap.release()
    cv2.destroyAllWindows()