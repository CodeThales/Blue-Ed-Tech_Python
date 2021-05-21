#Elaborar um programa que receba 4 notas
#de um aluno e calcule a média dele.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
média = (n1 + n2 + n3 + n4) / 4
print(f'A média entre as notas {n1:.2f}, {n2:.2f}, {n3:.2f} e {n4:.2f} é {média:.2f}')
