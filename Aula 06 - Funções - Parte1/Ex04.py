#Faça um programa que calcule o salário de um colaborador na empresa XYZ. 
#O salário é pago conforme a quantidade de horas trabalhadas. 
# Quando um funcionário trabalha mais de 40 horas ele recebe um adicional 
# de 1.5 nas horas extras trabalhadas.
def salario(horas,valor_hora):
    if horas > 40:
        h_extra = (horas - 40) * 1.5
        pgto = (horas *valor_hora) + h_extra
    else:
        pgto = horas * valor_hora
    return pgto


horas = float(input(f'Quantas horas foram trabalhadas: '))
valor_hora = float(input(f'Digite o valor da hora trabalhada: '))
pgto = salario(horas,valor_hora)
print(f'O pagamento será de R${pgto:.2f}')
