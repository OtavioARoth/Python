maior_idade = 18
idade_especial = 12
idade = int ( input( "informe sua idade: "))
if idade >= maior_idade:
    print ( "pode tirar CNH")
if idade < maior_idade:
    print ( "não pode tirar CNH")

if idade >= maior_idade:
    print ( "pode tirar CNH")
else:
    print ( "não pode tirar CNH")


if idade >= maior_idade:
    print ( "pode tirar CNH")
elif idade == idade_especial:
    print ( "pode fazer apenas aulas teoricas")
else:
    print ( "não pode tirar CNH")
