#Crie um programa que vai ler vários números e
#colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
valores = list()
cont = 0
while True:
    num = int(input('Digite um número: '))
    valores.append(num)
    cont += 1   
    while True:
        opc = str(input('Deseja adicionar outro número? [S/N]: ')).strip().upper()[0]
        if opc in 'SN':
            break
        print('Opção Inválida!')
    if opc == 'N':
        break
if 5 in valores:
    cinco = 'Encontrei'
else:
    cinco = 'Não encontrei'
print(f'foram adicionados {cont} números à lista.')
print(f'Estes valores (em ordem decrescente) foram: {sorted(valores, reverse=True)}')
print(f'{cinco} o números 5 na lista.')
