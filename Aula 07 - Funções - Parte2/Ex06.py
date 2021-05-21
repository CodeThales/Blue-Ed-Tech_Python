#Ex06: Um professor, muito legal, fez 3 provas
#durante um semestre,mas só vai levar em conta
#as duas notas mais altas para calcular a média. 
#Faça uma aplicação que peça o valor das 3 notas,
#mostre como seria a média com essas 3 provas,a 
#média com as 2 notas mais altas, bem como sua
#nota mais alta e sua nota mais baixa.
def nova_media(n1=0, n2=0, n3=0):
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    media = (n1 + n2 + n3) / 3
    print(f'A média entre as notas {n1}, {n2}, e {n3} é {media:.2f}.')
    maior1 = 0
    maior2 = 0
    menor = 0
    if n1 > n2 and n2 > n3:
        maior1 = n1
        maior2 = n2
        menor = n3
        media = (maior1 + maior2) / 2
        print(f'As suas notas mais altas foram {maior1} e {maior2}, e por isso sua média é {media:.2f}')
        print(f'A sua nota mais baixa foi {menor}.')
        print(f'A sua maior nota foi {maior1}')
    elif n2 > n1 and n1 > n3:
        maior1 = n2
        maior2 = n1
        menor = n3
        media = (maior1 + maior2) / 2
        print(f'As suas notas mais altas foram {maior1} e {maior2}, e por isso sua média é {media:.2f}')
        print(f'A sua nota mais baixa foi {menor}.')
        print(f'A sua maior nota foi {maior1}')
    elif n2 > n1 and n3 > n2:
        maior1 = n3
        maior2 = n2    
        menor = n1
        media = (maior1 + maior2) / 2
        print(f'As suas notas mais altas foram {maior1} e {maior2}, e por isso sua média é {media:.2f}')
        print(f'A sua nota mais baixa foi {menor}.')
        print(f'A sua maior nota foi {maior1}')
    elif n3 > n1 and n1 > n2:
        maior1 = n3
        maior2 = n1    
        menor = n2
        media = (maior1 + maior2) / 2
        print(f'As suas notas mais altas foram {maior1} e {maior2}, e por isso sua média é {media:.2f}')
        print(f'A sua nota mais baixa foi {menor}.')
        print(f'A sua maior nota foi {maior1}')
    elif n2 > n3 and n3 > n1:
        maior1 = n2
        maior2 = n3    
        menor = n1
        media = (maior1 + maior2) / 2
        print(f'As suas notas mais altas foram {maior1} e {maior2}, e por isso sua média é {media:.2f}')
        print(f'A sua nota mais baixa foi {menor}.')
        print(f'A sua maior nota foi {maior1}')
    elif n1 > n3 and n3 > n2:
        maior1 = n1
        maior2 = n3    
        menor = n2
        media = (maior1 + maior2) / 2
        print(f'As suas notas mais altas foram {maior1} e {maior2}, e por isso sua média é {media:.2f}')
        print(f'A sua nota mais baixa foi {menor}.')
        print(f'A sua maior nota foi {maior1}')


nova_media(n1, n2, n3)
