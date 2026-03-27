#1
import os
with open('test.txt', 'w') as conteudo:
    c = conteudo.read()

    print(c)

with open('teste', 'r') as conteudo:
    c = conteudo.read()

    print(c)

#2
os.mkdir("meu_diretoria")

#3
os.rename("meu_diretorio", "novo_diretorio")

#4
with os.scandir('meu_diretorio') as entrada:
    for teste in entrada:
        if teste.is_file():
            print(f'Arquivo encontrado: {teste.name}')

#5
import shutil

shutil.copytree("teste.txt", "novo_diretorio/teste_copia.txt")

#6
import os
os.remove("teste.txt")