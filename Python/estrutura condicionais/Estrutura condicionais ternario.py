saldo = 2000
saque = 5400
status = "sucesso" if saldo >= saque else "falha"
print (f"{status} ao realizar o saque")