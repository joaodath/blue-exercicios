class Conta:
    def __init__(self, nome = '', saldo = 0):
        self.__titular_da_conta = nome
        self.__saldo = saldo
    
    def __str__(self):
        if self.__saldo > 0:
            return f'''
            Titular: {self.__titular_da_conta}
            Saldo: {self.__saldo}'''
        else:
            return f'''
            Titular: {self.__titular_da_conta}'''
    
    def __pode_sacar(self, valor_saque):
        return self.__saldo > valor_saque

    def sacar(self, valor):
        if self.__pode_sacar:
            self.__saldo -= valor
            return f'''
            O saldo em conta é R${self.__saldo + valor}.
            O valor sacado foi R${valor}.
            O novo saldo em conta é R${self.__saldo}.'''
        else:
            return f'''
            Valor em conta R${self.__saldo} insuficiente.
            Você não tem saldo suficiente para essa operação.'''
    
    def depositar(self, valor):
        self.__saldo += valor
        return f'''
        O saldo em conta é R${self.__saldo - valor}.
        O valor depositado foi R${valor}.
        O novo saldo em conta é R${self.__saldo}.'''
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular_da_conta

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor
    
    @titular.setter
    def set_titular(self, nome):
        self.__titular_da_conta = nome

cliente01 = Conta()
cliente01.set_titular('João')
cliente01.saldo()
saque = float(input(f'Informe o valor a ser sacado em Reais da conta de {cliente01.titular}. R$'))
print(cliente01.sacar(saque))
deposito = float(input(f'Informe o valor a ser depositado em Reais da conta de {cliente01.titular}. R$'))
print(cliente01.depositar(saque))
print('Fim do Programa!')