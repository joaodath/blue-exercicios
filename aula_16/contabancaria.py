class Conta:
    def __init__(self, titular, saldo):
        self.Titular = titular
        self.Saldo = saldo
    def sacar(self, valor):
        if self.Saldo > 0 and valor < self.Saldo:
            self.Saldo -= valor
            return f'''
            O saldo em conta é R${self.Saldo + valor}.
            O valor sacado foi R${valor}.
            O novo saldo em conta é R${self.Saldo}.'''
        else:
            return f'''
            Valor em conta R${self.Saldo} insuficiente.
            Você não tem saldo suficiente para essa operação.'''
    def depositar(self, valor):
        self.Saldo += valor
        return f'''
        O saldo em conta é R${self.Saldo - valor}.
        O valor depositado foi R${valor}.
        O novo saldo em conta é R${self.Saldo}.'''