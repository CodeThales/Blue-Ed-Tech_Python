'''#02 - Utilizando listas, faça um programa que faça
5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a 
participação da pessoa no crime. Se a pessoa responder 
positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".'''
quest = list()
p1 = str(input('Telefonou para a vítima? [S/N] ')).strip().upper()[0]
quest.append(p1)
p2 = str(input('Esteve no local do crime? [S/N] ')).strip().upper()[0]
quest.append(p2)
p3 = str(input('Mora perto da vítima? [S/N] ')).strip().upper()[0]
quest.append(p3)
p4 = str(input('Devia para a vítima? [S/N] ')).strip().upper()[0]
quest.append(p4)
p5 = str(input('Já trabalhou com a vítima? [S/N] ')).strip().upper()[0]
quest.append(p5)
quantS = quest.count('S')
quantN = quest.count('N')
if quantS == 0 or quantS == 1:
    print('Inocente!')
elif quantS == 2:
    print('Suseita!')
elif quantS == 3 or quantS == 4:
    print('Cúmplice!')
else:
    print('Assassino!')
