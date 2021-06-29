#Crie uma classe chamada Conta para simular as operações de uma conta corrente. Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe Conta e teste os atributos e métodos implementados.​ Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente para essa operação."
from .contabancaria import Conta

cliente01 = Conta(str(input('Informe o nome do novo cliente: ')), float(input('Informe o saldo inicial do novo cliente em Reais: R$')))
saque = float(input(f'Informe o valor a ser sacado em Reais da conta de {cliente01.Titular}. R$'))
print(cliente01.sacar(saque))
deposito = float(input(f'Informe o valor a ser depositado em Reais da conta de {cliente01.Titular}. R$'))
print(cliente01.depositar(saque))
print('Fim do Programa!')