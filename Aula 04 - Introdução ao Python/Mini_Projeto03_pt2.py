#Mini Projeto 03 - Calculadora de dano
#Parte 2
#Alterar o programa para ao invés de receber
#a vida do monstro, gerar aleatoriamente
#um valor entre 10 e 50.
from random import randint
vida = randint(10,50)
print(f'A vida do monstro é de {vida}')
ataque = int(input('Digite a sua força de ataque [entre 5 e 10]: '))
turnos = 1
while True:
    if vida > ataque:
        vida = vida - ataque
        turnos += 1     
    else:
        break  
print(f'O jogador vai precisar de {turnos} turnos para derrotar o monstro.')
