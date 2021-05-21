'''Crie um jogo onde o computador vai “pensar” 
em um número entre 0 e 10. O jogador vai tentar 
adivinhar qual número foi escolhido até acertar, 
mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
pc = randint(0,10)
palpites = 1
acertou = False
print('''Olá, meu nome é Stark. 
Sou uma inteligência artificial criada pelo Thales.
Eu acabei de pensar em um número entre 0 e 10.
Consegue adivinhar qual foi? ''')
user = int(input('Qual o seu palpite: '))
while not acertou:
    user = int(input('Você errou. Tente novamente: '))
    palpites += 1
    if user == pc:
        acertou = True
print(f'Parabéns. Você acertou em {palpites} tentativas!')
