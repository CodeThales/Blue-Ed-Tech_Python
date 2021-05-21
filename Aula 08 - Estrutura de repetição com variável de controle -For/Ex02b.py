'''Ex02 - Dado uma string com uma frase informada
pelo usuário (incluindo espaços em branco), conte 
quantas vezes aparece as vogais a,e,i,o,u.'''
frase = str(input('Digite uma frase: ')).lower()
a = e = i = o = u = 0
for c in frase:
    if c == 'a':
        a += 1
    if c == 'e':
        e += 1
    if c == 'i':
        i += 1
    if c == 'o':
        o += 1
    if c == 'u':
        u += 1
print(f'A letra a foi encontrada {a} vezes na frase.')
print(f'A letra e foi encontrada {e} vezes na frase.')
print(f'A letra i foi encontrada {i} vezes na frase.')
print(f'A letra o foi encontrada {o} vezes na frase.')
print(f'A letra u foi encontrada {u} vezes na frase.')
