#Mini Projeto 03 - Calculadora de dano
#Parte 1
#O programa deve receber a vida e um monstro
#(entre 10 e 50) e o valor do ataque do
#jogador por turno (entre 5 e 10)
#Baseado nos valores, exiba a quantidade
#de turnos que o jogador irá demorar para
#conseguir derrotar o monstro.
vida = int(input('Digite a vida de um monstro [entre 10 e 50]: '))
ataque = int(input('Digite a sua força de ataque [entre 5 e 10]: '))
turnos = 1
while True:
    if vida > ataque:
        vida = vida - ataque
        turnos += 1     
    else:
        break  
print(f'O jogador vai precisar de {turnos} turnos para derrotar o monstro.') 
