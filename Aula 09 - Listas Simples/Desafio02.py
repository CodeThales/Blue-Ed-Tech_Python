'''Faça um script que peça ao usuário
o número de matérias da escola,
ou seja, um inteiro positivo. Em seguida, ele
vai digitando o valor de cada nota, de
cada matéria e isso será armazenado numa lista.
Ao final, seu script deverá
fornecer a média geral do aluno.'''
i = int(input('quantas materias tem sua aula: '))
notas = list()
for c in range(i):
    notas.append(float(input('qual a nota: ').replace(',','.')))
soma = sum(notas)
media = soma/i
print(f'a media geral é: {media}')
