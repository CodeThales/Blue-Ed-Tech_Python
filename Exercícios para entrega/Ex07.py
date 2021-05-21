#Crie um programa onde o usuário possa digitar sete
#valores numéricos e cadastre-os em uma lista única 
#que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.
lista = [[], []]
temp = 0
for i in range(0, 8):
    temp = int(input('Digite um número: '))
    if temp % 2 == 0:
        lista[0].append(temp)
    else:
        lista[1].append(temp)
lista[0].sort()
lista[1].sort()
print(f'Os valores PAR foram {lista[0]}.')
print(f'Os valores ÍMPAR foram {lista[1]}')
