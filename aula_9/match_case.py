#1
num1 = int(input('numero;'))
match num1:
    case num1 if num1 % 2 == 0:
        print('Par')
    case 1:
        print('impar')    


#2
num2 = int(input('numero'))
match num2:
    case num2 if num2 > 0:
        print('Positivo')
    case num2 if num2 < 0:
        print('Negativo')
    case _:
        print('Zero')   
        
#3
string = input('texto = ')

match string:
     case '':
         print('Vazio')
     case _:
         print('Cheio')

#4
match num2:
    case num2 if num2 > 10:
        print('maior que 10')
    case num2 if num2 < 10:
        print('Menor que 10') 
    case _:
        print('10')     

#5
idade  =  int(input('idade: '))

match idade:
    case x if x <13:
        print('Crianca')
    case x if x >14 and x < 17:
        print('Adolescente')
    case x if x >18 and x <35:
        print('jovem')
    case x if x >= 35 and x <64:
        print('Adulto')
    case _:
        print('Idoso ')                

