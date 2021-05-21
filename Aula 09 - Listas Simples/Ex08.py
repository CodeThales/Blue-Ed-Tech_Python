'''Faça um script em Python que exiba todos 
os possíveis palpites da Mega-Sena.
#Dados:
● Cada palpite possui 6 dezenas
● As dezenas variam de 1 até 60
● Não pode repetir dezena'''
from random import randint
def mult_jog(jogo, num):
    jogo = list()
    num = (randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60))
    if num not in jogo: 
        jogo.append(num)    
        print(jogo)


jogo = list()
num = randint(1,60)
mult_jog(jogo, num)
mult_jog(jogo, num)
mult_jog(jogo, num)
mult_jog(jogo, num)
mult_jog(jogo, num)
mult_jog(jogo, num)

#não entendi bem o objetivo do programa, então fiz duas opçãoes diferentes:
for dez_1 in range(60):
    for dez_2 in range(dez_1+1, 60):
        for dez_3 in range(dez_2+1, 60):
            for dez_4 in range(dez_3+1, 60):
                for dez_5 in range(dez_4+1, 60):
                    for dez_6 in range(dez_5+1, 60):
                        print(dez_1+1, dez_2+1, dez_3+1, dez_4+1, dez_5+1, dez_6+1)
total = 0
for dez_1 in range(60):
    for dez_2 in range(dez_1+1, 60):
        for dez_3 in range(dez_2+1, 60):
            for dez_4 in range(dez_3+1, 60):
                for dez_5 in range(dez_4+1, 60):
                    for dez_6 in range(dez_5+1, 60):
                        total +=1
print(total)