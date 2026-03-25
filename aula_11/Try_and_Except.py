try:
    l = [123,5,3]
    print(l[2] / 0)
except NameError:
    print('declare a variavel do dado')    
except TypeError:
    print('Dados no calculo aritmetico incorreto')    
except ValueError:
    print('Valor inserido incorretamente')
except ZeroDivisionError:
    print('A divisão não pode ser por zero')
except IndexError:
    print('Esse indice nãi existe')
else:
    print('Erro desconhecido')
finally:
    print('FIM de carregamento')