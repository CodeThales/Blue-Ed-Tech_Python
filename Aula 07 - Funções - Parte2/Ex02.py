#Ex02: Escreva uma função que recebe dois números (a e b) 
#como parâmetro e retorna True caso a soma dos dois seja 
#maior que um terceiro parâmetro, chamado limite.
def soma_ab(a, b, limite):
    soma = a + b
    print(f'A soma entre {a} e {b} é {soma}')
    if soma == limite:
        print(f'A soma entre {a} e {b} é igual ao terceiro número.')
    elif soma > limite:
        print('True')
    else:
        print('False')


a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
limite = float(input('Digite mais um número: '))
soma_ab(a, b, limite)
