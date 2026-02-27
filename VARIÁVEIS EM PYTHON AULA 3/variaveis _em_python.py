
print('hello word')


# 4 tipos de dados primitivos

#string - dados do tipo texto - "Texto"
#float - dados do tipom decimals - 5.0
#bool - dados do tipo lógico - True / False
#int - dados do tipo inteiro - 10 1 -2 0
#######################################################
# variáveis

#nome semântico, começar por letra, snak_case(palavra composta),
#não começa por número


#estrutura de dados
nome = "Vitor"
sobrenome = 'Barbosa'
idade = 25
endereco = 'Rua 20 nº 2'
peso = 65.5
solteiro = False

print(nome,sobrenome)
print('Idade', idade)
print('Endereco', endereco)
print('Peso', peso)
print('Estado Civil:', solteiro)

n1= 10
n2 = 20
#input()

nome = print('Nome: ')
sobrenome = print('Sobrenome: ')
idade = print('Idade: ')
endereco = print('Endereco: ' )
peso = print('Peso: ')
solteiro = print('Estado Civil: ')



#Pemdas       
x = 10 + 2 + (10*2) - 50 ** 2 
#Sinais aritméticos

print(10 + 1)
print(10 - 1)
print(10 * 1)
print(10 / 1)
print(10 // 1)
print(10 % 1)
print(10 ** 1)


#Sinais lógicos
print(10 > 1) # True
print(10 < 1) # False
print(10 >= 1) # > ou = 1 | 1 or 0 - True
print(10 <= 1) # 0 0 = False
print(10 == 1) # 0 = False
print(10 != 1) # True

#pular linha
print(nome)
print(sobrenome)


print(f'{nome}\n {sobrenome}')

print(f'''
{nome}
{sobrenome}

''')