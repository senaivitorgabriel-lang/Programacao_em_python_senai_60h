import random # criar aleatoridade

maquina = ['','✂️','🪨','🧻'] # lista icones - 1 ->  
escolha_maquina = random.choice(maquina[1:]) # escolha
id_maquina = maquina.index(escolha_maquina) # a posição dos indices lista

# ------------------------------------
minhas = ['','✂️','🪨','🧻']
print("escolha '✂️ 1','🪨-2','🧻 - 3")
minha_escolha  = int(input('escolha o objeto -> '))

if minha_escolha == id_maquina:
    print('---------------------------------------------')
    print('EMPATE!!!😒😒😒 ')
    print('---------------------------------------------')
    print('Minha escolha -', minhas[minha_escolha])
    print('---------------------------------------------')
    print('Escolha da maquina 💀', escolha_maquina )

elif id_maquina == 1 and minha_escolha == 3:
    print('---------------------------------------------')
    print('Vitoria da maquina! 👽💀')    
    print('---------------------------------------------')
    print('Minha escolha - ❌ ', minhas[minha_escolha])
    print('Escolha da maquina', escolha_maquina )
elif id_maquina == 2 and minha_escolha == 1:
    print('---------------------------------------------')
    print('Vitoria da maquina! 👽💀')    
    print('---------------------------------------------')
    print('Minha escolha - ❌  ', minhas[minha_escolha])
    print('Escolha da maquina', escolha_maquina )
elif id_maquina == 3 and minha_escolha == 2:
    print('---------------------------------------------')
    print('Vitoria da maquina! 👽💀')    
    print('---------------------------------------------')
    print('Minha escolha - ❌ ', minhas[minha_escolha])
    print('Escolha da maquina', escolha_maquina )

elif id_maquina == 3 and minha_escolha == 1:
    print('---------------------------------------------')
    print('SUA Vitoria!')    
    print('---------------------------------------------')
    print('Minha escolha - 😍😘 ', minhas[minha_escolha])
    print('Escolha da maquina', escolha_maquina )
elif id_maquina == 1 and minha_escolha == 2:
    print('---------------------------------------------')
    print('SUA Vitoria!')    
    print('---------------------------------------------')    
    print('Minha escolha - 😍😘 ', minhas[minha_escolha])
    print('Escolha da maquina', escolha_maquina )
elif id_maquina == 2 and minha_escolha == 3:
    print('---------------------------------------------')    
    print('SUA Vitoria!')    
    print('---------------------------------------------')    
    print('Minha escolha - 😍😘 ', minhas[minha_escolha])
    print('Escolha da maquina', escolha_maquina )