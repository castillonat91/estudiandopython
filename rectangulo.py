ancho = int(input("ingresar el ancho del rectangulo"))
altura = int(input("ingresar la altura del rectangulo"))
caract = input("ingresar el caracter a utilizar")


def dibujar(an,al,letra):
    for i in range(an):
        for j in range(al):
            print(letra,end=" ")
        print()
    
dibujar(ancho,altura,caract)
        
