e_commerce = {
	'secao' :{

    'Chuteira': {'Chuteira Pro 5':750.0,'Chuteira Bump':599.0},
    'Camisas': {'Camisa Oficial Palmeiras':729.99,'Camisa Oficial São Paulo':689.0},
    'Luvas': {'Luva de Goleiro Firmness |||| ':530.0,'Luva de Goleiro Poker Chanpion 8 Extended':800.0},
},

}
carrinho = []
valores  = []


secao = input('Digite o nome da seção: ')
produto_1 =  input('Digite o nome do produto: ')

secao = input('Digite o nome do seção: ')
produto_2 =  input('Digite o nome do produto: ')

secao = input('Digite o nome do seção: ')
produto_3 =  input('Digite o nome do produto: ')

carrinho.append(produto_1)
carrinho.append(produto_2)
carrinho.append(produto_3)
print(carrinho)

valores.append(e_commerce['secao'][secao][produto_1])
valores.append(e_commerce['secao'][secao][produto_2])
valores.append(e_commerce['secao'][secao][produto_3])

print('R$', valores)
somar  =  sum(valores)
print('R$', somar)

