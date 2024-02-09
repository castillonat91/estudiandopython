texto = "buenos dias definiendo un parametro en una funcion"
#funcion sin parametros
def mensaje ():
    N1 = int(input("ingrsar el primer numero"))
    N2 = int(input("ingresar el segundo numero"))
    calcularmayor(N1,N2)
    positivo(N1,N2)

#funcion con parametros
def calcularmayor(num1,num2):
    if num1 > num2:
        print("el primer numero es el mayor")
    elif num1==num2:
        print("son numeros iguales")
    else:
        ("el segundo numero es el mayor")

def positivo(p1,p2):
    if p1>0 and p2>0:
        print(" son numeros positivos")
    else:
        print("al menos unos de los numeros no es negativo")






mensaje()