#Faça um programa que peça dois números, imprima
#o maior deles ou imprima "Numeros iguais" se os números forem iguais.
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 > num2:
    print(f'O numero {num1} é o maior')
else:
    if num1 == num2:
        print("Os numeros são iguais!")
    else:
        print(f'O numero {num2} é o maior')
