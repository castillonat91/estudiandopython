nombresalumnos = []
notasalumnos = []
notas = 1
i = 0
promedio = 0

numeroalum = int(input("ingresar la cantidad de alumnos"))

for x in range(numeroalum):
    nom = input(f"ingresar el nombre de alumnos {x+1} :")
    nombresalumnos.append(nom)

    while notas > 0:
        notas = float(input(f"ingrese la nota {i+1} :"))
        i += 1
        notasalumnos.append(notas)
    
    notasalumnos.pop()
    
    suma = 0
    for z in range(len(notasalumnos)):
        guardar = notasalumnos[z]
        suma += guardar
           


print(nombresalumnos)
print(notasalumnos)


    