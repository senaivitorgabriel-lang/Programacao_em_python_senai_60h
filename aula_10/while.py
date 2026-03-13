#ATIVIDADE 1
#1
mil = 0

while mil <= 1000:
    print(mil)
    mil = mil + 1


#2
nomes = []


c = 10
while  c >0:
    n = input('nomes:')
    nomes.append(n) 
    print(nomes)   
    c = c - 1

#ATIVIDADE 2
#1

senha_correta = '8567'
notas = []
nome = []

c = 3
while c > 0:
    
    senha_professor = input('Digite a sua senha:')
    c = c -1
    if senha_correta != senha_professor:
        print('Senha Incorreta')
        
    else:
        print('SISTEMA NOTAS') 

        quantidade = int(input('quantidade:'))
        for n in  range(quantidade):
            dados = input('Digite seu nome: ')
            nome.append(dados)
            print('seu nome é', nome)
            nota = float(input('Digite sua nota: '))
            notas.append(nota)
            print('sua nota é' , nota )  
        media = sum(notas)/len(notas)   
        print('media sala', media)
        break      
    
else:
      print('Mande mensagem mais tarde')

        



