'''1. Crie um código em Python que pede 
qual tabuada o usuário quer ver, em
seguida imprima essa tabuada.'''
n = int(input('Digite um número para descobrir a sua tabuada: '))
if n < 0:
    print('Fim do programa!')
for c in range (0,10):
    c += 1
    tot = n*c
    print(f'{n} X {c} = {tot}')
