#opcao = -1
#while True:
 #   opcao = int (input("informe um numero: "))
  #  if opcao == 10:
   #     break
    #print ( opcao)

#for numero in range (100):
 #   if numero == 100:
  #      break
   # print ( numero, end = " ")
while True: 
    numero = int ( input ("informe um numero: "))
    if numero == 10:
        break
    if numero % 2 == 0:
        continue
    print (numero)