tupla = (2,4,6)
fecha = (9,"febrero",2024)

print(tupla)
print(fecha)

palabras = int(input("cuantas palabras deseas agregar"))

if palabras < 1:
    print("no es valido")
else:
    lista = []
    for i in range(palabras):
        palabra = input(f"escribir la palabra {i+1}:")
        lista +=[palabra]
    print(f"la lista creada es: {lista}")
    