#Crie um programa que leia nome, ano de nascimento
#e carteira de trabalho e cadastre-os (com idade) 
#em um dicionário. Se por acaso a CTPS for diferente
#de 0, o dicionário receberá também o ano de 
#contratação e o salário. Calcule e acrescente , 
#além da idade, com quantos anos a pessoa vai se aposentar.
#Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
from datetime import datetime
ano_atual = datetime.now().year
dados = dict()
dados['nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Nº da CTPS [se não tem, digite 0]: '))
if dados['ctps'] != 0:
    dados['ano_contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['idade_aposentadoria'] = dados['idade'] + ((dados['ano_contratacao'] + 35) - datetime.now().year)

for k, v in dados.items():
    print(f'{k}: {v}') 
