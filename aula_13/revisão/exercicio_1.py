#1

import random

num1 = random.randint(5, 10)
print(num1)

#2

def atividade2():
    x  =  random.randint(1,10)
    y  =  random.randint(1,10)
    z  =  random.randint(1,10)
    return x, y, z
#3

def atividade3():
    x = random.randrange(10,30)
    return x

#4

for i in range(10, 0, -1):
    print(i)

print("Fogo!")

#5

n = int(input("Digite um número inteiro positivo: "))


soma_pares = 0

for num3 in range(2, n + 1, 2):
    if num3 % 2 == 0:
        soma_pares  += num3

print(f"A soma de todos os números pares de 2 até {n} é: {soma_pares}")

#6

numero = int(input("Digite um número inteiro para ver sua tabuada: "))

print(f"Tabuada de {numero}:")


for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#7

for i in range(99, 0, -2):
    print(i)