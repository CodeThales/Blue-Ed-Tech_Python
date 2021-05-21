#Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, 
# ‘N’, se seu argumento for negativo e ‘0’ se for 0.
def pos_neg(n):
    if n > 0:
        return 'P'
    elif n == 0:
        return 0
    else:
        return 'N'


n = int(input('Digite um número para saber se ele é positivo ou negativo: '))
pos_neg(n)
