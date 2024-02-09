enteros = []
def ingresar():
    for x in range(5):
        numero = int(input("ingresar el numero"))
        enteros.append(numero)

def imprimir(enteros):
    print("los datos de la lista son")
    for x in enteros:
        print(x)

def sumar(enteros):
    acumulador=0
    for x in enteros:
        acumulador += x
    print("la suma de los numeros es:  ",acumulador)

ingresar()
imprimir(enteros)
sumar(enteros)