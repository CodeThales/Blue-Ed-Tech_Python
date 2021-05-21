#4.	Crie um programa em que 4 jogadores,
#joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário. 
#No final coloque esse dicionário em ordem, 
#sabendo que o vencedor tirou o maior número no dado.
#Dicas: procure sobre a função randint(), sleep()
#e itemgetter da biblioteca operator.
from random import randint as rd
from time import sleep
from operator import itemgetter
ranking = list()
jogo = {'jogador1': rd(1, 6),
'jogador2': rd(1, 6),
'jogador3': rd(1, 6),
'jogador4': rd(1, 6)}
print(f'{"*"*10}Dados Rolaram{"*"*10}')
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)
print()
print(f'{"*"*10}RANKING{"*"*10}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
