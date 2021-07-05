#Crie uma classe chamada Conta para simular as operações de uma conta corrente. Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe Conta e teste os atributos e métodos implementados.​ Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente para essa operação."
conta_import = str(input('Importar conta? S/N ').strip().upper())
if conta_import[0] == 'S':
    from contabancaria import *
    print('Importei!')
else:
    print('Não importei!')

cliente01 = Conta()
#cliente01.titular(input('Informe o nome completo do titular da conta: ').strip().capitalize())
cliente01.saldo()
saque = float(input(f'Informe o valor a ser sacado em Reais da conta de {cliente01.titular}. R$'))
print(cliente01.sacar(saque))
deposito = float(input(f'Informe o valor a ser depositado em Reais da conta de {cliente01.titular}. R$'))
print(cliente01.depositar(saque))
print('Fim do Programa!')