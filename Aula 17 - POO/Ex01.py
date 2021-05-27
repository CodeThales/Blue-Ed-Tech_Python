#Crie uma classe chamada Conta para simular as operações
#de uma conta corrente. Sua classe deverá ter os atributos
#Titular e Saldo, e os métodos Sacar e Depositar. Crie um 
#objeto da classe Conta e teste os atributos e métodos implementados.
# Adicione uma regra no método Sacar, onde o usuário só poderá sacar
#se o Saldo for maior que zero, caso contrário mostre a mensagem na tela:
#"Você não tem saldo suficiente para essa operação."
from conta import Conta
nome = str(input('Nome do titular da conta: '))
saldo = float(input('Saldo da sua conta: '))
conta001 = Conta(nome, saldo)

while True:
    saque = float(input('Quanto você deseja sacar: '))
    conta001.sacar(saque)
    resp = str(input('Deseja sacar mais [S/N]? ')).strip().upper()[0]
    if resp in 'N':
        break

