opcao = -1
while opcao != 0:
    opcao = int (input("[1] Sacar \n [2] Extrato \n [0] Sair \n:"))
    if opcao ==1:
        print ("sacando...")
    elif opcao == 2: 
        print (" exibindo o extrato...")
    else:
        print ( "obrigado!")