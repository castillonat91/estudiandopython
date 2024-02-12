nombres=[]
kilometros=[]
total_kms= []
sumatotal=0

for i in range(4):
    kilometros=[]
    sumatotal= 0

    nom = input(f"por favor ingresar el nombre del conductor {i+1}: ")
    nombres.append(nom)
    
    for i in range(7):
        kilom = float(input(f"por favor ingresar los kilometros conducido en el dia {i+1}: "))
        kilometros.append(kilom)

    for x in range(len(kilometros)):
        sumatotal += kilometros[x] 

    total_kms.append(sumatotal)

for y in range(len(nombres)):
    print(nombres[y])
    print(total_kms[y])



