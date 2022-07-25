'''                  Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
'''
'''
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
 Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobrTe o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''



tipo_carne = str (input("escolha o tipo de carne [F]-File Duplo  [A]-Alcatra [P]-Picanha : "))
quantidade = float (input("Informe a quantidade em [Kg] : "))



if (tipo_carne == "File" and quantidade <= 2):
    valor_compra = quantidade * 4.90
    

elif (tipo_carne == "File" and quantidade >= 2):
    valor_compra = quantidade * 5.80
    

elif (tipo_carne == "Alcatra" and quantidade <= 2):
    valor_compra = quantidade * 5.90


elif (tipo_carne == "Alcatra" and quantidade >= 2):
    valor_compra = quantidade * 6.80
    

elif (tipo_carne == "Picanha" and quantidade <= 2):
    valor_compra = quantidade * 6.90
    

elif (tipo_carne == "Picanha" and quantidade >= 2):
    valor_compra = quantidade * 7.80
   

desconto = ""


tipo_pagamento = str (input("Escolha tipo de Pagamento: [Cartão Tabajara] ou [Outro Tipo De Pagamento]  : "))

if tipo_pagamento == "Cartão Tabajara":
    desconto = 5 / 100
    valor_compra = valor_compra * (1-desconto)
elif tipo_pagamento == "Outro Tipo De Pagamento":
    print("Outro Tipo De Pagamento")



valor_total = valor_compra

print()
print()
print("---------------CUPOM_FISCAL------------")
print("Tipo de Carne : ",tipo_carne)
print("Quantidade : ",quantidade, "[Kg]")
print("O preço total : ",valor_compra,"[R$]")
print("Tipo de Pagamento : ",tipo_pagamento,"")
print("Desconto :",desconto)
print("Valor a Pagar :",valor_total,"[R$]")
print()
print()