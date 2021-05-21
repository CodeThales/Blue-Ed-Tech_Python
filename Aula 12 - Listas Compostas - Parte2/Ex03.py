#03 - Aprimore o desafio anterior, mostrando no final:
   # A) A soma de todos os valores pares digitados.
   # B) A soma dos valores da terceira coluna. 
   # C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior = somapar = somacoluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número para linha {[linha]}, coluna {[coluna]} : '))
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^3}]', end='')
    print()
for coluna in range(0, 3):
    if coluna == 0 or matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
for linha in range(0, 3):
    somacoluna += matriz[linha][2]
print()
print(f'O maior valor da segunda linha é: {maior}')
print(f'A soma dos valores pares é: {somapar}')
print(f'A soma dos valores da terceira coluna é: {somacoluna}.')
