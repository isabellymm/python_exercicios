kg_maça = float(input("Informe a quantidade em [Kg] de Maça :"))
kg_morango = float(input("Informe a quantidade em [Kg] de Morango :"))

desconto = ""
preçototal = ""
valor_compras  = ""

maçamenor5 = 1.80
maçamaior5 = 1.50
morangomenor5 = 2.50
morangomaior5 = 2.20

if kg_maça <=5:
    preçototal = (kg_maça * 1.80)
    print()
    print("-------------------------------")
    print("--------------NOTA-------------")
    print("O [Kg] da Maça é de : ",maçamenor5)
    print("O Total é de : ",preçototal)



elif kg_maça >=5:
     preçototal = (kg_maça * 1.50)
     print()
     print("-------------------------------")
     print("--------------NOTA-------------")
     print("O [Kg] da Maça é de : ",maçamaior5)
     print("O Total é de : ",preçototal)



if kg_morango <=5:
    preçototal = (kg_morango * 2.50)
    print()
    print("-------------------------------")
    print("--------------NOTA-------------")
    print("O [Kg] do Morango é de : ",morangomenor5)
    print("O Total é de : ",preçototal)

elif kg_morango >=5:
    preçototal = (kg_morango * 2.20)
    print()
    print("-------------------------------")
    print("--------------NOTA-------------")
    print("O [Kg] do Morango é de : ",morangomaior5)
    print("O Total é de : ",preçototal)

desconto = (preçototal * 0.1)

if kg_maça >= 8 or preçototal >= 25:
    preçototal = (preçototal - desconto )
    print()
    print("-------------------------------")
    print("--------------NOTA_COM_DESCONTO-------------")
    print("O [Kg] da Maça é de : ",maçamaior5)
    print("O Total é de : ",preçototal)

elif kg_morango >= 8 or preçototal >= 25:
    preçototal = (preçototal - desconto )
    print()
    print("-------------------------------")
    print("--------------NOTA_COM_DESCONTO-------------")
    print("O [Kg] do Morango é de : ",morangomaior5)
    print("O Total é de : ",preçototal)



