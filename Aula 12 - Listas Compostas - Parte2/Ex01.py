#01 - Crie um programa onde o usuário possa digitar
# sete valores numéricos e cadastre-os em uma lista 
# única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[], []]
temp = 0
for i in range(1, 8):
    temp = int(input(f'Digite o {i}º valor: '))
    if temp % 2 == 0:
        valores[0].append(temp)
    else:
        valores[1].append(temp)

print(f'Os números digitados foram {valores}')
valores[0].sort()
valores[1].sort()
print(f'Os numeros pares são {valores[0]}')
print(f'Os números impares são {valores[1]}')
