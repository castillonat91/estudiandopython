suma = 0
promediomañana = 0
promediotarde = 0
promedionoche = 0

for i in range (6):
    edad = int(input("ingresar edad de estudiantes mañana"))
    suma = suma+edad

promediomañana=suma/6
print("mostrar cantidad de edad de estudiantes ingresados ",promediomañana)

for i in range (7):
    edad = int(input("ingrese edad de estudiantes tarde"))
    suma = suma+edad

promediotarde=suma/7
print("mostrar cantidad de edad de estudiantes ingresados ",promediotarde)

for i in range (12):
    edad = int(input("mostrar cantidad de estudiantes ingresados noche"))
    suma = suma+edad

promedionoche=suma/12
print("mostrar cantidad de edad de estudiantes ingresados ",promedionoche)

if promediomañana > promediotarde and promediomañana > promedionoche:
    print("el promedio de la mañana es mayor que los otros ")

elif promediotarde > promediomañana and promediotarde > promedionoche:
    print("el promedio de la tarde es mayor a todos")

else:
    print("el promedio de la noche es mayor que los otros")