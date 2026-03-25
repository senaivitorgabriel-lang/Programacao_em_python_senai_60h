#1
while True:
    try:

        num = int(input('Digite um numero'))
        print(f'Você digitou o número: {num}')    
        break
    except ValueError:

        print('Error: Entrada inválida! por favor, digite um numero.')

#2
while True:
    try:

            num1 = int(input('Digite um primeiro número: '))
            num2 = int(input('Digite um primeiro número: '))
            cont = num1 / num2
            print(cont)
            break
    except ZeroDivisionError:
         print('Error: Operação Inválida! Por Favor, tente novamente.')

#3
try:
     
     lista1 = [10, 20, 30, 40, 50]
     indice1 = 7
     print(f"Elemento encontrado: {lista1[indice1]}")
except IndexError:
     print(f"Erro: Índice {indice1} é inválido para uma lista de tamanho {len(lista1)}.")

print(lista1, indice1)
print(lista1, 10)
