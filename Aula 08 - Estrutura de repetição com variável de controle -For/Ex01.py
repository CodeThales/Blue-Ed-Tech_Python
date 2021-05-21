'''Ex01 - Crie um programa que vai gerar cinco 
números aleatórios de 1 a 50 e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e 
também indique o menor e o maior valor que estão na tupla.
Sem utilizar repetições.'''
from random import randint
lista = (randint(1, 50),randint(1, 50),randint(1, 50),randint(1, 50),randint(1, 50))
print(f'Os números gerados foram: {lista}.')
print(f'O maior valor da lista é {max(lista)}.')
print(f'O menor valor da lista é {min(lista)}.')
