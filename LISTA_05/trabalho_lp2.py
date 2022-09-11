
cartao = int(input('Digite a quantidade total de cartões : '))

cartao_new = cartao - 2
multa = 0


for j in range(2):
    print('Cartão ' + str(j+1) + 'º  : 0' )


for i in range(cartao_new):

    multa += 500
    print('Cartão ' + str(i+3) + 'º  :' ,multa)



Soma = (500 + multa )* cartao_new / 2
print('Total R$ : ',Soma)

