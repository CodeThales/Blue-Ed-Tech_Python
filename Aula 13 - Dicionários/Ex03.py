#3.	Faça um programa que leia nome e média
#de um aluno, guardando também a situação
#em um dicionário. No final, mostre o 
#conteúdo sa estrutura na tela. A média
#para aprovação é 7. Se o aluno tirar entre
#5 e 6.9 está de recuperação, caso contrário
#é reprovado.
boletim = dict()
boletim['nome'] = str(input('Nome: ')).strip().title()
boletim['media'] = float(input(f'Media de {boletim["nome"]}: ').replace(',', '.'))
if boletim['media'] >= 7:
    boletim['situação'] = 'Aprovad@'
elif boletim['media'] >= 5 and boletim['media'] <= 7:
    boletim['situação'] = 'Em Recuperação'
else:
    boletim['situação'] = 'Reprovado'
for k, v in boletim.items():    
    print(f'{k}: {v}')
