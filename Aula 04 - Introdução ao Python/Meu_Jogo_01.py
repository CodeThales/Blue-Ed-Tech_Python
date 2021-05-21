#Meu game baseado na ideia da calculadora de dano:
from random import randint
from time import sleep
player = str(input('Digite seu nome para se alistar no Exército da Rainha: ')).strip().upper()
sleep(0.5)
print('*'*60)
print(f'''Parabéns {player}! 
Você foi aceit@ para lutar ao nosso lado nesta batalha.''')
weapons = ['Clava', 'Espada', 'Lança']
print('*'*60)
sleep(1)
while True:
  resp = str(input('''Deseja se preparar para a batalha?
[S/N]: ''')).strip().upper()[0]
  if resp == 'S':
    while True:
      print('*'*60)
      sleep(1)     
      weapon = int(input('''Escolha sua arma:
[0] Clava
[1] Espada
[2] Lança
''')) 
      if weapon >=0 and weapon <=2:
        break
      else:
        print('*'*60)
        print('Ítem inválido! Tente novamente.')
    force_weapon = randint(5,10)
    print('*'*60)
    sleep(1)
    print(f'''Você escolheu a {weapons[weapon]} como sua arma. 
Ela está com {force_weapon} pontos de poder de ataque!''')
    enemys = ['Dwarf', 'Orc', 'Wisdom']
    print('*'*60)
    sleep(1)
    while True:
      enemy = int(input('''Escolha seu oponente:
[0] Dwarf
[1] Orc
[2] Wisdom
'''))
      if enemy >=0 and enemy <=2:
        break
      else:
        print('*'*60)
        print('Ítem inválido! Tente novamente.')
    life_enemy = randint(10, 50)
    sleep(1)
    print('*'*60)
    print(f'''Você escolheu o {enemys[enemy]} como seu oponente. 
Ele está com {life_enemy} pontos de vida!''')
    print('*'*60)
    call = 'XXXXXX A BATALHA COMEÇOU! XXXXXXX'
    sleep(1)
    print(f'{call:^60}')
    print('*'*60)
    sleep(3)
    times = 1
    while True:
      if life_enemy > force_weapon:
        life_enemy -= force_weapon
        print(f'Em sua {times}ª ofensiva você deixou seu oponente com {life_enemy} pontos de vida!')
        sleep(1.5)
        times += 1     
      else:
        break 
    print('*'*60)
    print(f'''O INIMIGO FOI VENCIDO!!!
Finalmente a batalha acabou. 
Nós usamos {times} ofensivas para derrotar o oponente.''')
    print('*'*60)
    resp = str(input('Quer jogar novamente? [S/N]: ')).strip().upper()[0]
    print('*'*60)
    sleep(1)
  if resp == 'N':
    print('*'*60)
    print('<<< FIM DE JOGO! >>>')
    break
