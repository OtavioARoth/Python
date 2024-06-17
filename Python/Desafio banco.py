menu = """
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3
while True:
    opcao = input(menu) #selecao do menu acima
    if opcao == "d":
        valor = float(input("informe o valor a ser depositado: ")) #float valor variavel INT
        if valor > 0:
            print(f"depoisitov realizado com sucesso R$ {valor:.2f} \n")
            saldo+=valor #adiciona valor ao saldo +=
            extrato += f"depósitov realizado: {valor:.2f}\n"
        else: #lembre-se dos "doispontos"
                 print ("Operação falhou: O valor informado é invalido")
    elif opcao =="s":
                 
        valor = float(input("informe o valor de saque"))
        excedeu_saldo = valor > limite
        excedeu_limite = valor >limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print ("Operação falhou! Você não tem saldo suficiente.")
                  
        elif excedeu_limite:
            print("Operação falhou, O valor excede o limite")
        elif excedeu_saques:
            print ("Operação falhou O numero maximo de saques foi atingido")
        elif valor >0:
             print(f"Saque realizado com sucesso R$ {valor:.2f}\n")
    elif opcao == "e":
             print("============================== EXTRATO ==============================")
             print("Não foram realizadas movimentações na conta." if not extrato else extrato)
             print(f"\nSaldo: R$ {saldo:.2f}")
             print("=====================================================================")               
    elif opcao == "q":
            break
    else:
            print ("operação inválida, por favor selecione um comando válido")