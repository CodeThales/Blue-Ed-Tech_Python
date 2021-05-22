#Crie um programa onde o usuário possa digitar
#cinco valores numéricos e cadastre-os em uma lista,
#já na posição correta de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela.
valores = []
for i in range(1, 6):
    num = int(input(f'Digite o {1}º número: '))
    if i == 1 or num > valores[-1]:
        valores.append(num)
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:        
                valores.insert(pos, num)
                break
            pos += 1
print(f'Os números digitados, em ordem são: {valores}')
