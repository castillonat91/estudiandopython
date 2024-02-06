import random

secreto = random.randint(1,10)

numero = int(input("adivinar el numero entre 1 a 10"))

while numero != secreto:
    if numero < secreto:
        print("el numero es mayo")
    else:
        print("el numero es menor")

    numero = int(input("intenta de nuevo :"))

print("felicitaciones adivinaste el numero secreto :",secreto)






