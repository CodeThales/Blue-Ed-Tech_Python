#Crie um programa que leia uma frase qualquer
#e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).strip().lower().replace(' ', '')
inverso = ''
for letra in range(len(frase)-1, -1, -1):
    inverso += frase[letra]
if frase == inverso:
    print(f'A frase: {frase} - É um palíndromo.')
else:
    print(f'A frase {frase} - NÃO é um palíndromo')
