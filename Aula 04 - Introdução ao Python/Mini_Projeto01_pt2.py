#Mini Projeto 01 - Conversor de Moeda
#Parte 2
#Alterar o conversor de moedas para receber
#o valor em dólar, converter para real e 
#mostrar o resultado no formato R$ XXXX.XX
vd = 5.75
quant = float(input('Digite o valor em $: '))
conv = float(quant*vd)
print(f'${quant:.2f} corresponde a R${conv:.2f}')
