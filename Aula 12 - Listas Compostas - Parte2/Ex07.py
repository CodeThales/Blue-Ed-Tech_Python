#03 - Crie um programa que leia o nome e o preço de
#vários produtos. O programa deverá perguntar se o 
#usuário vai continuar ou não. No final, mostre:
   # A) qual é o total gasto na compra.
   # B) quantos produtos custam mais de R$1000.
   # C) qual é o nome do produto mais barato.
total = maismil = menor = itens = 0
maisbarato = ''
maiscaro = list()
while True:
   produto = (str(input('Nome do produto: ').strip().capitalize()))
   preco = (float(input('Preço do produto: R$').replace(',',  '.')))
   total += preco
   itens += 1   
   if preco > 1000:
      maismil += 1
      maiscaro.append(produto)
   if itens == 1 or preco < menor:
      menor = preco
      maisbarato = produto         
   resp = str(input('Deseja adicionar mais algum item? [S/N]')).strip().upper()[0]
   if resp == 'N':
      break
print(f'O valor total das compras é de R${total:.2f}')
print(f'Houveram {maismil} produtos que custaram mais de R$1.000,00')
print(f'Estes produtos foram {maiscaro}')
print(f'O nome do produto mais barato foi {maisbarato} que custou R${menor:.2f}')
