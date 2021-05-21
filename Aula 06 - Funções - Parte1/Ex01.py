#Faça um programa, com uma função que necessite de três argumentos, 
# e que forneça a soma desses três argumentos.
def soma3(n1, n2, n3):
    soma = n1 + n2 + n3
    return f'{n1} + {n2} + {n3} = {soma} '


n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))
soma3(n1, n2, n3)
