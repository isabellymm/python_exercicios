# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:  R$ 1,90
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina: R$ 2,50 
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro

tipo =  (input ("Escolha entre [A]-Álcool ou [G]-Gasolina: "))
litro = float (input("Quntos litros foram vendidos:"))

preco_alcool =  (litro * 1.90)
preco_gaso =  (litro * 2.50)


if (tipo == "A" and litro <= 20):  
   desconto = (preco_alcool  * 0.03 )
   novo_preco =  preco_alcool - desconto
   print("O preco sem desconto sera:",preco_alcool)
   
  
elif (tipo == "A" and litro >= 20):
   desconto = (preco_alcool * 0.05)
   novo_preco = preco_alcool - desconto
   print("O preco sem desconto sera:",preco_alcool)

elif (tipo == "G" and litro <= 20):
   desconto = (preco_gaso * 0.04)
   novo_preco =  preco_gaso - desconto
   print("O preco sem desconto sera:",preco_gaso)
   

elif (tipo == "G" and litro >= 20):
    desconto = (preco_gaso * 0.06)
    novo_preco =  preco_gaso - desconto
    print("O preco sem desconto sera:",preco_gaso)


print("O desconto aplicado é de :",round(desconto))
print ("O total sera de :",round(novo_preco))