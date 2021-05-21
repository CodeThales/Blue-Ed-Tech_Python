#Mini Projeto 02 - Calculadora de aumento de aluguel
#Construa um programa que irá calcular
#o aumento anual do seu aluguel em duas partes:
#Parte 1
#A sua calculadora vai receber o valor do aluguel e calcular
#o aumento baseado no IGPM de 31%. A calculadora deve
#apresentar o aluguel reajustado no formato R$ XXXX.XX
valor = float(input('Digite o valor do aluguel: '))
print(f'O valor do aluguel atualmente é R$ {valor:.2f}')
nvalor = valor + (valor*31/100)
print(f'O valor do aluguel reajustado é R$ {nvalor:.2f}')
