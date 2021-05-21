'''Faça um programa que mostre os valores
numéricos inteiros ímpares situados
na faixa de 0 a 20.'''
num_i = list()
for i in range(20):
    if not i % 2 == 0:
        num_i.append(i)
print('Os números ímpares no intervalo de 0 e 20 são: ')
print(num_i, end='')
