'''Escreva um programa que pede a senha ao usuário, e só sai
do looping quando digitarem corretamente a senha:'''
senha = 0
while senha != 999:
    senha = int(input('Digite sua senha: '))
print('Saindo do programa.')
