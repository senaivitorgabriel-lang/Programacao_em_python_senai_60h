print('SISTEMA DE VERIFICAÇÃO DE MÉDIA')

nome = input('Digite o nome do aluno:')

print('Digite as notas do aluno(a)', nome)
n1 = float(input('Digite sua Nota 1'))
n2 = float(input('Digite sua Nota 2'))
n3 = float(input('Digite sua Nota 3'))
print('***' * 15)
print('Média da Aluno(a)', nome)
media = (n1 + n2 + n3) / 3
print('Média do aluno(a)', nome)
print(media)
aprovada = media >= 7
recuperacao = media >=5 and media <7
reprovada = media < 5

print(f'''
SITUAÇÃO DO ALUNO(A) {nome}
Aprovada? - {aprovada}
Reprovada? - {reprovada}
Recuperação? - {recuperacao}

''')

