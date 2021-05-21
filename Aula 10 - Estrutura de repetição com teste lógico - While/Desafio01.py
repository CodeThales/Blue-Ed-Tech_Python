'''Em uma eleição presidencial existem quatro candidatos.
Os votos são informados por meio de código.
Os códigos utilizados são:
1 , 2, 3  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;'''
cand1 = cand2 = cand3 = cand4 = nulo = branco = 0
sair = 999
print('''Estas são as opções de candidatos:
  [1] JOSÉ
  [2] JOÃO
  [3] MARIA
  [4] CARLA
  [5] VOTO NULO
  [6] EM BRANCO
  [999] SAIR''')
opção = int(input('>>>>>Qual é a sua opção? '))
while opção != sair:
    opção = int(input('>>>>>Qual é a sua opção? '))
    if opção == 1:
        cand1 +=1
    elif opção == 2:
        cand2 +=1
    elif opção == 3:
        cand3 +=1
    elif opção == 4:
        cand4 +=1
    elif opção == 5:
        nulo +=1
    elif opção == 6:
        branco +=1
print(f'O candidato José recebeu {cand1} votos.')
print(f'O candidato João recebeu {cand2} votos.')
print(f'A candidata Maria recebeu {cand3} votos.')
print(f'A candidata Carla recebeu {cand4} votos.')
print(f'Foram {nulo} votos nulos.')
print(f'Foram {branco} votos em branco.')
