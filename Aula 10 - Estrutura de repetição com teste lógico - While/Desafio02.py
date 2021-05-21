'''Crie um programa que leia a idade e
o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não
continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
somaidade = 0
maioridadehomem = 0
nomehomemvelho = ''
menosvinte = 0
cadastro = 'CADASTRO'
mais18 = 0
totm = 0
menos20 = 0
while True:
    print('*'*25)
    print(f'{cadastro:^25}')
    print('*'*25)
    idade = int(input('Idade: '))
    if idade > 18:
        mais18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        totm += 1
    if sexo == 'F' and idade < 20:
        menos20 += 1    
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]
    if opção == 'N':
        break
print('*'*25)
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {totm} homems cadastrados.')
print(f'Ao todo temos {menos20} mulheres com menos de 20 anos.')
print('Fim dos cadastros.')
