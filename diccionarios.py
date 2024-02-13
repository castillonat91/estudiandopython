persona = {
    "nombre":"yuri natalia",
    "apellido":"castillo peña",
    "estatura":1.59,
    "edad":19,
    "email":"castillonat91@gmail.com",
    "ciudadnac":"bogota",
    "genero":["femenino","masculino","otro"]
}


print(persona)
#mostrar elemento del diccionario
print(f"el nombre de la persona es:",{persona["nombre"]})
#agregar elemento del diccionario
persona["telefono"]=654789521
print(persona)
#modificar valor del elemento diccionario
persona["telefono"]=678954321
print(persona)
#modificar la clave del elemento
persona["celular"]=persona.pop("telefono")
print(persona)
#eliminar un elemento del diccionario
del persona["celular"]
print(persona)

#iterar los itenm de las claves y valores
for clave,valor in persona.items():
    print(clave , ": " , valor)