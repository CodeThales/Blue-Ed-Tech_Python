# Faça um programa que leia nome e peso de várias 
# pessoas, guardando tudo em uma lista, depois do dado
# inserido, pergunte ao usuário se ele quer continuar, 
# se ele não quiser pare o programa. No final mostre:
   # Quantas pessoas foram cadastradas
   # Mostre o maior peso
   # Mostre o menor peso

dados = list() #lista temporária
lista = list() #lista principal
tot = maior = menor = 0
while True: 
    dados.append(str(input('Digite o nome: ')))
    for p in dados:
        tot += 1
    dados.append(float(input('Digite o peso: ').replace(',', '.')))  
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]    
    if resp == 'N':
        break
print(f'Foram cadastradas {tot} pessoas.')
print(f'O maior peso foi {maior}Kg.')
print(f'O menor peso foi {menor}Kg.')
