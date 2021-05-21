#02 - Crie um programa que declare uma matriz
#de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com essa formatação:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):  
        matriz[linha][coluna]= int(input(f'Digite um número para linha [{linha}], coluna [{coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^3}]', end='')
    print()
