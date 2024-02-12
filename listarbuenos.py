#definir las lista
nombres=[]
notas=[]
mb=0
b=0
In=0
Ml=0
lista=[]

#llenar la lista
for x in range (1,5):
    nom = input(f"por favor ingresar el nombre del alumno {x} : ")
    nombres.append(nom)
    no = int(input(f"por favor ingresar la nota del alumno {x} : "))
    notas.append(no)
#recorrer la lista
for y in range(len(nombres)):
    print(nombres[y])
    print(notas[y])


    if notas[y]>=8:
        print("alumno muy bueno")
        mb += 1
        lista.append(nombres[y])
        print("nombre de los mejores estudiantes",lista)
    else:
        if notas[y]>=4:
            print("alumno bueno")
            b += 1
        else:
            print("alumno no aprueba la materia")
            In += 1 
print("listado inicial de los alumnos son :",nombres)
#mostrar solo los alumnos buenos
eliminar = []
for z in range(len(notas)):
    if 4 <= notas[z] <=7:
        #notas.pop(z)
        #nombres.pop(z)
        eliminar.append(z)
for d in sorted(eliminar,reserve=True):
        notas.pop(z)
        nombres.pop(z)

print("cantidad de alumnos muy buenos son: ",mb)
print("listado de alumnos ", nombres[z])



