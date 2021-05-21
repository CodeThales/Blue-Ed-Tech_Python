#Ex03: Faça um programa com uma função chamada somaImposto. 
# A função possui dois parâmetros formais: taxaImposto, 
# que é a quantia de imposto sobre vendas expressa em porcentagem e custo, 
# que é o custo de um item antes do imposto. A função “altera” 
# o valor de custo para incluir o imposto sobre vendas.
def SomaImposto(taxaImposto = 0, custo = 0):
    custofinal = custo + (custo* taxaImposto / 100)
    return custofinal
  

custo = float(input('Qual o custo do produto? ')) 
taxaImposto = float(input('Qual a taxa de imposto sobre este produto (em %)? '))
print(f'O custo final incluido impostos será de R${SomaImposto(taxaImposto, custo):.2f}')
