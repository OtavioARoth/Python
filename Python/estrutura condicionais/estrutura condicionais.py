opcao = int ( input("informe uam opção : 1 = sacar 2 = extrato"))
if opcao == 1: 
    valor = float ( input("informe a quantia para saqu"))
    # ...
elif opcao == 2:
    print ("exibindo estrato")
else:
    sys.exit ("opcao invalida")
