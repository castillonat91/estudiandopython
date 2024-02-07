nalturas = int(input("ingresar el numero de alturas"))
suma = 0
promedio = 0
contador = 0

while contador < nalturas:
    altura = float(input("ingresar altura"))
    suma = suma+altura
    promedio = suma/nalturas
    contador =contador+1
    
print("mostrar altura promedio del grupo",promedio)
