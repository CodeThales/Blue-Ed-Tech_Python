#Ex05: Faça um programa que tenha uma função chamada ficha(), 
# que receba dois parâmetros: 
#o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome=0, gols=0):
    print('-'*30)
    print('     FICHA DOS JOGADORES     ')
    print('-'*30)
    return f'{nome} fez {gols} gols.'
  

nome = str(input('Digite o nome do jogador: ')).strip().title()
gols = int(input('Quantos gols ele fez? '))
print(ficha(nome, gols))
