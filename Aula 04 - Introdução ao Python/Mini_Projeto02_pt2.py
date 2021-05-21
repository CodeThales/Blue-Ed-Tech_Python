#Mini Projeto 02 - Calculadora de aumento de aluguel
#Parte 2
#Agora, altere sua calculadora para receber além
#do valor do aluguel, o percentual do reajuste no formato XX%.
valor = float(input('Digite o valor do aluguel: '))
print(f'O valor do aluguel atualmente é R$ {valor:.2f}')
per = float(input('Qual o percentual de reajuste? '))
print(f'PErcentual do reajuste = {per:.2f}%')
nvalor = valor + (valor*per/100)
print(f'O valor do aluguel reajustado é R$ {nvalor:.2f}')
