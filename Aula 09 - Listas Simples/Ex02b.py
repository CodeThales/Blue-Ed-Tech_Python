'''Elaborar um programa para imprimir
os números de 1 até 10
em ordem decrescente.'''
n = list(range(1 , 11))
n = sorted(n, reverse=True)
print(n)
