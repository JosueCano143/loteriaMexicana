from random import shuffle
from PIL import Image
question = input("¿Quieres volver a jugar a la lotería?")
while question == 'si':
    loteria = ['El gallo','El diablito','La dama','El catrín','El paraguas','La sirena','La escalera','La botella',
           'El barril','El árbol','El melón','El valiente','El gorrito','La muerte','La pera','La bandera',
           'El bandolón','El violoncello','La garza','El pájaro','La mano','La bota','La luna','El cotorro',
           'El borracho','El negrito','El corazón','La sandía','El tambor','El camarón','Las jaras','El músico',
           'La araña','El soldado','La estrella','El cazo','El mundo','El apache','El nopal','El alacrán',
           'La rosa','La calavera','La campana','El cantarito','El venado','El sol','La corona','La chalupa',
           'El pino','El pescado','La palma','La maceta','El arpa','La rana' ]
    shuffle(loteria)
    iK = 0
    for i in range(1,55):
        answer = input("Para terminar esta jugada teclea loteria")
        if answer != 'loteria':
            print(loteria[iK])
            idPicture = loteria[iK] +'.jpg'
            try:
                imagen = Image.open(idPicture)
                imagen.show()
            except:
                print("No ha sido posible cargar la imagen")
            iK = iK + 1
        else:
            break
    question = input("¿Quieres volver a jugar a la lotería?")
        

   

    
