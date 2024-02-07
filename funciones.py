def inicio():



    print("menu principal")
    print("seleccione la opcion correcta")
    print("1. operacion sumar")
    print("2. operacion restar")
    print("3. operacion multiplicar")
    print("4. operacion dividir")

def main():
    while True:
        inicio()
        opcion = int(input("selecione la opcion"))
        if opcion ==1:
            print("ha selecionado la suma")
            num1 = int(input("ingrese el 1 numero"))
            num2 = int(input("ingrese el 2 numero"))
            sumar = num1+num2
            print("el resultado de la suma es: ",sumar)
        elif opcion == 2:
            print("ha selecionado la resta")
            num1 = int(input("ingrese el 1 numero"))
            num2 = int(input("ingrese el 2 numero"))
            restar = num1-num2
            print("el resultado de la resta es: ",restar)
        elif opcion == 3:
            print("ha selecionado operaccion multiplicar")
        elif opcion == 4:
            print("ha selecionado operaccion dividir")
        elif opcion == 5:
            print("hasta luego")
            break
        else:
            print("opcion no valida, seleccione una opccion valida")


main()




    
    

