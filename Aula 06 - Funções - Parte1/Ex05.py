#Faça um programa que calcule através de uma
#função o IMC de uma pessoa que tenha 1,68 e pese 75kg.
def f_imc(peso, altura):
    imc = peso / altura ** 2
    print(f'Seu IMC é de {imc:.1f}')  
    if imc < 18.5:
        print('Abaixo do peso normal.') 
    elif imc <= 24.9:
        print('Dentro da faixa de peso normal')
    elif imc <= 29.9:
        print('Sobrepeso')
    elif imc <= 34.9:
        print('Obesidade Grau I')
    elif imc <= 39.9:
        print('Obesidade Grau II')
    elif imc >= 40:
        print('Obesidade Mórbida.')


peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
f_imc(peso,altura)
