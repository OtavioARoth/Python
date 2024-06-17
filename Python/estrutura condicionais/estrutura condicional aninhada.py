conta_normal = False
Conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 500
if conta_normal:
    if saldo >= saque:
        print ( "saque realizado com sucesso")
    elif saque <= ( saldo + cheque_especial):
        print ( "saque realizado  com uso do cheque especial")
    else:
        print ("não foi possivel realizar o saque, saldo insuficiente")
elif Conta_universitaria:
        if saldo >=saque:
             print ( "saque realizado com sucesso!")
        else:
             print ("saldo insuficiente")
else:
     print ( "não foi identificado o tipo de conta!")