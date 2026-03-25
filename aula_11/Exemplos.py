# variavel global
nome = 'Carlos'
print(nome)

def mostrar_nome():
    # esta dentro da função
    nome  =  'Julia'
    print(nome)

def mostrar_nome2():
    print(nome)

print(nome)
mostrar_nome()
mostrar_nome2()

def mostrar_nome3():
    global nome, idade
    nome  =  'carlos'
    idade  =  25
    print(nome, idade)

print(nome)
mostrar_nome3()