# EX01: Escreva uma função que recebe dois
#parâmetros (números) e imprime o menor dos dois. 
#Se eles forem iguais, imprima que são valores idênticos.
def men(n1, n2):
    if n1 == n2:
        print('Os valores são idênticos.')
    elif n1 < n2:
        print(f'O menor valor é {n1}')
    else:
        print(f'O menor valor é {n2}')


n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = 0
men(n1, n2)
