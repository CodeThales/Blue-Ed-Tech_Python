#Faça um Programa para um caixa eletrônico.
#O programa deverá perguntar ao usuário a valor
#do saque e depois informar quantas notas de
#cada valor serão fornecidas. As notas disponíveis
# serão as de 1, 5, 10, 50 e 100 reais. O valor
#mínimo é de 10 reais e o máximo de 600 reais.
#O programa não deve se preocupar com a
#quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais,
#o programa fornece duas notas de 100, uma nota de 50,
#uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais,
#o programa fornece três notas de 100, uma nota de 50,
#quatro notas de 10, uma nota de 5 e quatro notas de 1.
saque = int(input('Digite o valor do saque: '))
if saque < 10:
    print('Valor de Saque abaixo do valor permitido!')    
elif saque > 600:
    print('Valor de Saque acima do valor permitido!')    
else:
    print(f'Para um saque de R${saque}:')
    cem = int(saque // 100)
    saque = saque % 100
    cinquenta = int(saque // 50)
    saque = saque % 50
    dez = int(saque//10)
    saque = saque % 10
    cinco = int(saque//5)
    saque = saque % 5
    um = int(saque//1)
    saque = saque % 1
    print(f'Você receberá {cem} cédula(s) de R$ 100,00.')
    print(f'Você receberá {cinquenta} cédula(s) de R$ 50,00.')
    print(f'Você receberá {dez} cédula(s) de R$ 10,00.')
    print(f'Você receberá {cinco} cédula(s) de R$ 5,00.')
    print(f'Você receberá {um} cédula(s) de R$ 1,00.')
