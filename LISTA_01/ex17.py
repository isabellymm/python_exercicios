# informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga 
# e sempre arredonde os valores para cima, isto é, considere latas cheias.


M2_POR_LITRO  = float (input("Informe em (m²) da área a ser pintada: "))

MARGEM_SEG = 1.1
CONSUMO_LITRO = float (M2_POR_LITRO  / 6 * MARGEM_SEG )

LITROS_LATA = (CONSUMO_LITRO / 18)
PRECO_LATA = LITROS_LATA * 80

LITROS_GALAO = (CONSUMO_LITRO / 3.6)
PRECO_GALAO =LITROS_GALAO * 25

LATA_MISTO = CONSUMO_LITRO // LITROS_LATA 
GALAO_MISTO = ((CONSUMO_LITRO - LATA_MISTO * LITROS_LATA) / LITROS_GALAO)

VALOR_LATA_MISTO = LATA_MISTO * PRECO_LATA

VALOR_GALAO_MISTO = GALAO_MISTO * PRECO_GALAO

print ()
print("---------------------NOTA----------------------")
print("-----------------------------------------------")
print ("Seram ultilizados",CONSUMO_LITRO,"litros de tinta")
print()
print()
print("A quantidade de latas de 18L a serem ultilizadas são de:",LITROS_LATA)
print("O preço total com latas de 18L será de:",PRECO_LATA)
print()
print()
print("A quantidade de latas de 3.6L a serem ultilizadas são de:",LITROS_GALAO)
print("O preço total com latas de 18L será de:",PRECO_GALAO)
print()
print('considerando o menor desperdíciode tinta, temos:')
print("A qunatidade de Latas:",LATA_MISTO)
print("A qunatidade de galões:",GALAO_MISTO)
print("quantidade total mistas:",{GALAO_MISTO + LATA_MISTO})
print("valor total considerando GALOES e LATAS é: R$:",{VALOR_GALAO_MISTO + VALOR_LATA_MISTO})
print()
print()
print("-----------------------------------------------")



