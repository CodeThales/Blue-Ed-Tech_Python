#Crie um programa que leia nome, sexo e idade
#de várias pessoas, guardando os dados de cada
#pessoa em um dicionário e todos os dicionários
#em uma lista. No final, mostre:
#A) Quantas pessoas estão cadastradas.
#B) A média da idade.
#C) Uma lista com as mulheres.
#D) Uma lista com as idades que estão acima da média.
#OBS: O programa deve garantir que o sexo digitado
#seja válido, e que quando perguntar ao usuário se
#deseja continuar a resposta seja somente sim ou não.
pessoa = dict()
povo = list()
cont = 0
lmedia = list()
mulheres = list()
acimamedia = list()
while True:
    pessoa['nome'] = str(input("Digite o nome: ")).strip().capitalize()
    pessoa['idade'] = int(input('Digite a idade: '))
    lmedia.append(pessoa['idade'])
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    povo.append(pessoa.copy())
    cont += 1
    while True:
        opc = str(input('Deseja adicionar mais alguém? [S/N] ')).strip().upper()[0]
        if opc in 'SN':
            break
        print('Opção inválida!')                
    if opc == 'N':
        break
print('CADASTRO FINALIZADO')
print(f'Foram cadastradas {len(povo)} pessoas na lista.')
media = sum(lmedia) / cont
print(f'A média de idade do grupo cadastrado é de {media:.2f}')
print(f'Lista de mulheres cadastradas: {mulheres}')
for i in lmedia:
    if i > media:
        acimamedia.append(i)
print(f'Idades que estão acima da média: {acimamedia}')
