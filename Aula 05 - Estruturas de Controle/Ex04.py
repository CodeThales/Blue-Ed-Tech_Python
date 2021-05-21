#Crie um programa que verifique se uma letra
#digitada é "F" ou "M". Conforme a letra escrever:
#F - Feminino, M - Masculino, caso escreva outra letra: Sexo Inválido.
resposta = str(input('Digite M ou F: ')).strip().upper()[0]

if resposta == 'M':
    print('Masculino')
else:
    if resposta == 'F':
        print('Feminino')
    else:
        print('Sexo Inválido!')
