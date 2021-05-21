'''Faça um programa que leia o sexo biológico de 
uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente
até ter um valor correto.'''
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    if sexo not in 'MF':
        print('Valor inválido!')
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
print(f'Seu sexo é {sexo}.')
