enteros = []
def ingresar():
    

    for x in range(5):
        numero = int(input("ingresar el numero"))
        enteros.append(numero)

def imprimir(enteros):
    print("los datos de la lista son")
    for x in enteros:
        print(x)

ingresar()
imprimir(enteros)
