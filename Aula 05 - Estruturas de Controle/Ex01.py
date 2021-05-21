#Exercício 01
#Faça um programa que pergunte ao usuário um
#número e valide se o numero é par ou impar:
#Crie uma variável para receber o valor,
#com conversão para int. 
numero = int(input('Digite o numero: '))

if numero % 2 == 0:
    print('Numero par')
else:
    print('Numero impar')
