# pedir o tamanho em metros quadrados da área a ser pintada
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# tinta é vendida em latas de 18 litros
# vendidas a 80,00
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total

area = float (input("Informe em (m²) da área a ser pintada: "))
litros = float (area / 3)

latas = (litros / 18)
preco = latas * 80

print("---------------------NOTA----------------------")
print("-----------------------------------------------")

print ("Seram ultilizados",litros,"litros de tinta")
print("A quantidade de latas a serem compradas são:",latas)
print("O preço total será de:",preco)

print("-----------------------------------------------")