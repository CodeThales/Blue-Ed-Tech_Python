class Conta:
    def __init__(self, titular = '', saldo = 0):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        if valor == 0:
            (f'Você não pode sacar R${valor:.2f}')
        if self.saldo < valor:
            print(f'Você não pode sacar R${valor:.2f}. Seu saldo é de R${self.saldo:.2f}. ')
        else:
            self.saldo -= valor
            print(f'Seu saldo agora é de R${self.saldo:.2f}')
        
    def depositar(self, valor):
        self.saldo += valor
        print(f'Seu saldo agora é de R${self.saldo:.2f}')
