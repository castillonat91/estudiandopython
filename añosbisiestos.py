inicio = int(input("ingresar año"))
final = int(input("ingresar el ultimo año"))

contador = 0
contadorbisiesto = 0

for año in range(inicio, final+1):
    
    if año  % 4 == 0:
        if año % 100 == 0:
            contador += 1
        else:
            contadorbisiesto += 1
        
    else:
        contador += 1


print("Años no bisiestos:",contador)
print("cuantos años bisiestos hay",contadorbisiesto)