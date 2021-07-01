# Fazer o método sacar(), se o saldo for menor ou igual a 0, retorne uma mensagem dizendo que o saldo é insuficiente, caso o contrário, realize a operação de saque e mostre o saldo atual dessa conta;
from conta import Conta
if __name__ == '__main__':
    banco = list()
    while True:
        conta = Conta(input('Informe o Titular: ').strip().capitalize())
        banco.append(conta)
        continuar = input('Deseja cadastrar uma nova conta? S/N ').strip().upper()[0]
        while continuar not in ['S', 'N']:
            continuar = input('Não entendi! Deseja cadastrar uma nova conta? S/N').strip().upper()[0]
        if continuar != 'S':
            break
    for c in range(len(banco)):
        print(banco[c])
        print()
