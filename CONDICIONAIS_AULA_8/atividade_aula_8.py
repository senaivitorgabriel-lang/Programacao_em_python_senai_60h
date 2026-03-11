#1
numero = int(input('Digite um numero:'))
if numero > 0:
    print('Positivo')
elif numero < 0:
    print('Negativo')
else:
    print('Igual a zero')

#2
idade  = int(input('Digite sua Idade:'))

if idade >= 16:
    print('Pode Votar')
elif idade < 16:
    print('Não Pode Votar')

3#
num = int(input('Digite um Numero'))
if num % 2 == 0:
    print('O numero é par')
else: print('O numero é impar')

4#
num1 = int(input('Digite um Numero'))
num2 = int(input('Digite o Segundo Numero'))
num3 = int(input('Digite O Terceiro Numero'))
if num1 == num2 == num3 == num1:
    print('Equilátero')
elif num1 != num2 != num3 != num1:
    print('Isósceles')
else:
    print('Escaleno')

#5
num4 = int(input('Digite um numero'))
if num4 % 7 == 0 and num4 % 5 == 0:
    print('Divisivel')
else:
    print('Não é Divisivel')

#6
num5 = int(input('Digite um Numero'))
if num5 > 0 and num5 > 10:
    print ('Positivo e Maior que 10')
else:
    print('Negativo')

#7
num6 = int(input('Digite um Numero'))
if num6 % 3 == 0 or num6 % 5 ==0:
    print(f"{num6} é divisivel por 3 ou 5")
else: print(f"{num6} não é divisivel por 3 nem por 5")



