'''Faça um programa que leia o estado civil
de 15 pessoas (Solteiro / Casado) e mostre ao
final a quantidade de pessoas de cada estado civil.'''
solteiro = list()
casado = list()
e_civil = list()
for i in range(1,16):
    e_civil = str(input('Qual seu estado civil? ')).strip().capitalize()
    if e_civil == 'Solteiro':
        solteiro.append(e_civil)
    elif e_civil == 'Casado':    
        casado.append(e_civil)
print(f'Temos {len(solteiro)} pessoas Solteiras.')
print(f'Temos {len(casado)} pessoas Casadas.')
