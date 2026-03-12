cadastro = {}

cliente1 = input('Nome')
idade1 = input('Idade')
senha1 = input('Senha')

cliente2 = input('Nome')
idade2 = input('Idade')
senha2 = input('Senha')

cliente3 = input('Nome')
idade3 = input('Idade')
senha3 = input('Senha')

cadastro['nomes'] = [cliente1, cliente2, cliente3]
cadastro['idades'] = [idade1, idade2, idade3]
cadastro['senhas'] = [senha1, senha2, senha3]
print(cadastro)

#------------------------------------------------------------------------------------#
# PARA ACESSAR O O SITE PARA FAZER O LOGIN:

nome_login = input('Digite seu nome >>')
senha_acesso = input('Digite sua senha >> ')


if nome_login in cadastro ['nomes'] and senha_acesso in cadastro['senhas']:
    print('Seja Muito Bem Vindo Senhor(a)!')

    print('Escolha o seu quarto: ', cadastro['nomes'][0])
    quartos  = ['','Quarto Simples', 'Quarto Duplo', 'Quarto Luxo']
    valores  =  [0,1000,1500,2500]
    print('quartos:  ', quartos)
    escolha = int(input('Quarto Simples | Quarto Duplo | Quarto Luxo'))
    dias = int(input('Quantos Dias Ficara Hospedado'))
    calculo = dias * valores[escolha]
    print ('Parabens, Você escolhou o quarto', quartos[escolha], 'Quantos Dias')
    print('Valor total a pagar R$', round(calculo,2))

    #-----------------------------------------------------------------------------------------------------------#

    print('Escolha o quarto: ', cadastro['nomes'][1])
    quartos  = ['','Quarto Simples', 'Quarto Duplo', 'Quarto Luxo']
    valores  =  [0,1000,1500,2500]
    print('quartos:  ', quartos)
    escolha  =  int(input('Quarto Simples | Quarto Duplo | Quarto Luxo'))
    dias = int(input('Quantos Dias Ficara Hospedado'))
    calculo = dias * valores[escolha]
    print ('Parabens, Você escolhou o quarto', quartos[escolha], 'Quantos Dias')
    print('Valor total a pagar R$', round(calculo,2))

    #-----------------------------------------------------------------------------------------------------------#

    print('Escolha o quarto: ', cadastro['nomes'][2])
    quartos  = ['','Quarto Simples', 'Quarto Duplo', 'Quarto Luxo']
    valores  =  [0,1000,1500,2500]
    print('quartos:  ', quartos)
    escolha  =  int(input('Quarto Simples | Quarto Duplo | Quarto Luxo'))
    dias = int(input('Quantos Dias Ficara Hospedado'))
    calculo = dias * valores[escolha]
    print ('Parabens, Você escolhou o quarto', quartos[escolha], 'Quantos Dias')
    print('Valor total a pagar R$', round(calculo,2))

else:
    print('Digite algo Valido')
