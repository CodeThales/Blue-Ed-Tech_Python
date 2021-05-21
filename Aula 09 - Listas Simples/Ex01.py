'''#01 - Dada a lista L = [5, 7, 2, 9, 4, 1, 3], 
escreva um programa que imprima as seguintes informações:
a) tamanho da lista.
b) maior valor da lista.
c) menor valor da lista.
d) soma de todos os elementos da lista.
e) lista em ordem crescente.
f) lista em ordem decrescente.'''
l = [5, 7, 2, 9, 4, 1, 3]
print(f'O tamanho da lista é {len(l)}')
print(f'O maior valor da lista é {max(l)}')
print(f'O menor valor da lista é {min(l)}')
print(f'O resultado da soma de todos os elementos da lista é {sum(l)}')
l = sorted(l)
print(f'A lista em ordem crescente é: {l}')
l = sorted(l, reverse=True)
print(f'A lista em ordem decrescente é: {l}')
