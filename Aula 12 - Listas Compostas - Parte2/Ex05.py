#01 - Crie um programa que leia dois
#valores e mostre um menu na tela:
   # [ 1 ] somar
   # [ 2 ] multiplicar
   # [ 3 ] maior
   # [ 4 ] novos números
   # [ 5 ] sair do programa
#Seu programa deverá realizar a operação
#solicitada em cada caso. (utilizar while sem break)

from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''Estas são as opções:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opção = int(input('>>>>>Qual é a sua opção? '))
    if opção == 1:
        print('A soma entre os números {} e {} é {}'.format(n1, n2, (n1+n2)))
    elif opção == 2:
        print('O resultado da multiplicação entre os números {} e {} é {}'. format(n1, n2, (n1*n2)))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))   
    elif opção == 4:
        print('Informe os novos valores: ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente: ')
    print('*'*20)
    sleep(2)  
print('Fim do programa! Volte sempre!')
