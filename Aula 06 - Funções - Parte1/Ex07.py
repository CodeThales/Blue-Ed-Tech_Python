#Ex07: Escreva uma função que recebe dois
#parâmetros e imprime o menor dos dois. 
#Se eles forem iguais, imprima que eles são iguais.
def mai_men(n1, n2):
    if n1 == n2:
      return 'Os valores são iguais'
    elif n1 < n2:
      return 'O primeiro valor é menor'
    else:
      return('O segundo valor é menor')


n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
mai_men(n1, n2)
