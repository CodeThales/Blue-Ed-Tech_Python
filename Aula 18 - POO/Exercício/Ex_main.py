# Faça um programa que simule um televisor criando-o como um objeto. ​
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.​
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
from Ex_televisor import Televisor
tv = Televisor(4, 50)
while True:
    opc_canal = 'S'
    opc = int(input('''Escolha uma opção:
    [1] TROCAR DE CANAL
    [2] MUDAR VOLUME
    [3] DESLIGAR'''))
    print(tv)
    if opc == 1:
        while True:
            if opc_canal == 'S':
                canal = int(input('Digite o número do canal: '))
                tv.trocar_canal(canal)
                print(tv)
            else:
                print(tv)
                break
            opc_canal = str(input('Deseja trocar de canal? [S/N] ')).strip().upper()[0]
    elif opc == 2:
        while True:
            print('''Escolha uma opção de volume:
        [1] AUMENTAR VOLUME
        [2] DIMINUIR VOLUME
        [3] MUTE  ''')
            opc_volume = int(input())    
            if opc_volume == 1:
                quant = int(input('Quanto deseja aumentar? '))
                tv.aumentar(quant)
                print(tv)
                break
            elif opc_volume == 2:
                quant = int(input('Quanto deseja diminuir? '))
                tv.diminuir(quant)
                print(tv)
                break
            elif opc_volume == 3:
                tv.mute()
                print(tv)
                break
            else:
                print('Opção inválida!')
    elif opc == 3:
        print('Desligando seu televisor...')
        break
