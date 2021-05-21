#Escreva uma função que, dado um número nota
#representando a nota de um estudante,converte
#o valor de nota para um conceito (A, B, C, D, E e F).
def conv_nota(n):
    if nota >= 9.0:
        return 'A'
    elif nota >= 8.0:
        return 'B'
    elif nota >= 7.0:
        return 'C'
    elif nota >= 6.0:
        return 'D'
    elif nota >= 5.0:
        return 'E'
    elif nota <= 4.0:
        return 'F'


nota = float(input('Qual a nota: '))
conv_nota(n)
