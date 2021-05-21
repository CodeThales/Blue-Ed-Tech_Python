'''O Sr. Manoel Joaquim acaba de adquirir uma
panificadora e pretende implantar a metodologia
da tabelinha, que já é um sucesso na sua loja de 1,99.
Você foi contratado para desenvolver o programa que 
monta a tabela de preços de pães, de 1 até 50 pães, 
a partir do preço do pão informado pelo usuário,
conforme o exemplo abaixo: 
1 - 0.18
2 - 0.36
50 - 9.00'''
print('*'*30)
print('        PREÇO DO PÃO        ')
print('*'*30)
preço = 0.18
for c in range(0,50):
    c += 1
    tot = preço*c
    print(f'{c} - {tot:.2f}')
print('*'*30)
