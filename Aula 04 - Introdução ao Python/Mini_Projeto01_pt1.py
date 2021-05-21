#Mini Projeto 01 - Conversor de Moeda
#Contrua um programa que irá converter
#moedas do real para o dólar e do dólar para o real.
#Vamos considerar que $ 1,00 = R$ 5,75
#Parte 1
#Faça o conversor de moeda receber o valor em real
#e mostrar o valor convertido para dólar no formato $ XXXX.XX
vd = 5.75
vr = float(input('Digite o valor em R$: '))
conv = float(vr/vd)

print(f'R${vr:.2f} corresponde a ${conv:.2f}')
