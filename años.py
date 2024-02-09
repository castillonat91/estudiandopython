año = int(input("ingresar año"))

def bisiesto_año(año):
    if año  % 4 == 0:
        if año % 100 == 0:
            print("el año no es bisiesto",año)
        else:
            print("el año es bisiesto",año)
    else:
        print("el año no es bisiesto",año)
          
          

bisiesto_año(año)

