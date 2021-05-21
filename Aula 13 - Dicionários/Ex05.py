#5.	Crie um programa que leia nome, 
#ano de nascimento e carteira de trabalho
#e cadastre-os (com idade) em um dicionário.
#Se por acaso a CTPS for diferente de 0, 
#o dicionário receberá também o ano de 
#contratação e o salário. Calcule e acrescente,
#além da idade , com quantos anos a pessoa vai
#se aposentar. Considere que o trabalhador 
#deve contribuir por 35 anos para se aposentar.
from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Nº da CTPS [Se não tem, digite 0]: '))
if dados['CTPS'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Idade em que vai se aposentar'] = dados['Idade'] + ((dados['Ano de contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f'{k}: {v}')
