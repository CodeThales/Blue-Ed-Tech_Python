#Parte 2
#Agora implemente a funcionalidade de não aceitar o número 0, no input.
valor = int(input('Digite o valor: '))
if valor == 0:
    print('Número inválido!')
else:
    if valor > 0:
        print('Número positivo')
    else:
        print('Número negativo')    
print('Programa finalizado!')
