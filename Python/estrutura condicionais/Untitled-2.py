saldo = 2000

def sacar(valor_saque, saldo):
    if valor_saque > saldo:
        print('Saldo insuficiente.')
    else:
        saldo = saldo-valor_saque
        print("Saque realizado com sucesso.")
        print("Seu saldo atual é de:", saldo)

valor_saque = float(input("Digite o valor que deseja sacar: "))
sacar(valor_saque, saldo)