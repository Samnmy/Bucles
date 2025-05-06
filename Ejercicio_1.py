print("Primeros 20 números pares (usando for):")
for i in range(1, 21):
    print(i * 2, end=" ")
print("\n")  
print("Primeros 15 números impares (usando while):")
contador = 0
numero = 1
while contador < 15:
    print(numero, end=" ")
    numero += 2
    contador += 1