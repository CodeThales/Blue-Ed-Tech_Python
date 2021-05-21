#As empresas @.com resolveram dar um aumento de
#salário aos seus colaboradores e lhe contrataram
#para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador
#e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5%
#Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento."
atual = float(input('Digite o salário atual do funcionário: '))
if atual < 280:
    print(f'O salário atual do colaborador é de R${atual:.2f}')
    per_aumento = atual*20/100
    print('Este colaborador vai receber 20% de aumento.')
    aumento = atual * 20/100
    print(f'O valor do aumento será de {aumento:.2f}')
    novo = atual + per_aumento
    print(f'Seu novo salário será de R${novo:.2f}')
elif atual >= 280 and atual < 700:
    print(f'O salário atual do colaborador é de R${atual:.2f}')
    per_aumento = atual*15/100
    print('Este colaborador vai receber 15% de aumento.')
    aumento = atual * 15/100
    print(f'O valor do aumento será de {aumento:.2f}')
    novo = atual + per_aumento
    print(f'Seu novo salário será de R${novo:.2f}')
elif atual >= 700 and atual < 1500:
    print(f'O salário atual do colaborador é de R${atual:.2f}')
    per_aumento = atual*10/100
    print(f'Este colaborador vai receber 10% de aumento.')
    aumento = atual * 10/100
    print(f'O valor do aumento será de {aumento:.2f}')
    novo = atual + per_aumento
    print(f'Seu novo salário será de R${novo:.2f}')
else:
    print(f'O salário atual do colaborador é de R${atual:.2f}')
    per_aumento = atual*5/100
    print(f'Este colaborador vai receber 5% de aumento.')
    aumento = atual * 5/100
    print(f'O valor do aumento será de {aumento:.2f}')
    novo = atual + per_aumento
    print(f'Seu novo salário será de R${novo:.2f}')
