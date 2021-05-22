#Faça um programa que tenha uma função chamada contador(),
#  que receba três parâmetros: início, fim e passo.
#Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada,
from time import sleep
def contador (inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        print('O valor mínimo de passo é de 1 em 1, por isso, o valor foi ajustado para 1.')
        passo = 1
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}:')    
    sleep(2)
    if inicio < fim:
        cont = inicio
        while cont <= fim: 
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)            
            cont += passo
        print()
        print('*'*35)
    else:    
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= passo
        print()
        print('*'*35)


contador(1, 10, 1)     
contador(10, 0, 2)
print('Faça sua contagem personalizada: ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
