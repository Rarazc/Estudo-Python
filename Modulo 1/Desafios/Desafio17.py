import math

oposto = float(input("Digite o valor do cateto oposto: "))
adjacente = float(input("Digite o valor do cateto adjacente: "))

print(f"A hipotenusa resultante é: {math.hypot(oposto,adjacente):.2f}")