class Conta:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo
    def __str__(self):
        return f'''
                Titular: {self.titular}.
                Saldo Disponível: R${self.saldo}.'''
    def sacar(self, valor):
        if self.saldo > 0 and valor < self.saldo:
            self.saldo -= valor
            return f'''
            O saldo em conta é R${self.saldo + valor}.
            O valor sacado foi R${valor}.
            O novo saldo em conta é R${self.saldo}.'''
        else:
            return f'''
            Valor em conta R${self.saldo} insuficiente.
            Você não tem saldo suficiente para essa operação.'''
    def depositar(self, valor):
        self.saldo += valor
        return f'''
        O saldo em conta é R${self.saldo - valor}.
        O valor depositado foi R${valor}.
        O novo saldo em conta é R${self.saldo}.'''