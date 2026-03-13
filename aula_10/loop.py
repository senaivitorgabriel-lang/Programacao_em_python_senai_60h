# banco

banco = {
'autenticacao':{
'senha':'123',
'nome':'Isadora Alves'
},
'saldo': [5000.0],
'emprestimos':[10000],
'cdb':[20000]
}
# acessar

for chances in range(3):
    print('BANCO xxxxxx')
    senha  =  input('DIGITE SUA SENHA: ')
    if senha == banco['autenticacao']['senha']:


        
        print('Conta de ', banco['autenticacao']['nome'])
        acesso = input('Deseja acessar o menu? ')
        while acesso == 'sim':
            print('ESCOLHA A OPERAÇÃO: ' \
            '1 - dados da conta | 2 - saque | 3 - deposito | 4 - extrato | 5 investimentos | 6 emprestimos')
           
            operacao = input('operação>>>>> ')

            if operacao == '1':
                print('DADOS:')
                print(banco['autenticacao']['nome'])
                print('SALDO R$', banco['saldo'])
                print('EMPRESTIMOS R$', banco['emprestimos'])
                print('INVSTIMENTOS CDB R$', banco['cdb'])
               
         
            elif operacao == '2':
                valor =  float(input('Digite o valor de saque'))
                sobra = sum(banco['saldo']) -  valor
                banco['saldo'].clear()
                banco['saldo'].append(sobra)

                print('valor sacado', valor)
                print('Em conta', sobra)

            elif operacao == '3':
                valor =  float(input('Digite o valor de deposito'))
                sobra = sum(banco['saldo']) +  valor
                banco['saldo'].clear()
                banco['saldo'].append(sobra)

                print('valor depositado', valor)
                print('Em conta', sobra)
            elif operacao == '4':
                print('DADOS:')
                print(banco['autenticacao']['nome'])
                print('SALDO R$', banco['saldo'])
                print('EMPRESTIMOS R$', banco['emprestimos'])
                print('INVSTIMENTOS CDB R$', banco['cdb'])  
            elif operacao == '5':
                menu_invest = ['0 poupança',' 1 tesouro direto', ' 2 cdi', '3 cdb']
                print('OPÇÕES: ', menu_invest)
                escolher_investimento =  int(input('Escolha o investimento: '))
                if escolher_investimento == 0:
                    valor  = float(input('Digite p valor'))
                    banco['poupança'] = valor
                    print(banco)
                elif escolher_investimento == 1:
                    valor  = float(input('Digite p valor'))
                    banco['Tesouro Direto'] = valor
                    print(banco)
                elif escolher_investimento == 2:
                    valor  = float(input('Digite p valor'))
                    banco['CDI'] = valor
                    print(banco)
                elif escolher_investimento == 3:
                    valor  = float(input('Digite p valor'))
                    banco ['cdb'] = valor
                    print(banco)
            elif operacao =='6':
                 emprestimos_valor  =  float(input('Digite p valor do emprestimo'))
                 banco['emprestimos'].append(emprestimos_valor)
                 print('Emprestimos solicitados:', banco['emprestimos'])
            else:
                print('digite algo valido...')    


else:
    print('conta bloqueada entre em contato com banco')
